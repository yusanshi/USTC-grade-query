import json
import sys
from bs4 import BeautifulSoup
from login import login


def get_grade(username, password):
    semester_ID_url = 'https://jw.ustc.edu.cn/for-std/grade/sheet/getSemesters'
    grade_url_base = 'https://jw.ustc.edu.cn/for-std/grade/sheet/getGradeList?trainTypeId=1&semesterIds='
    url = 'https://passport.ustc.edu.cn/login?service=https://jw.ustc.edu.cn/ucas-sso/login'

    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    }
    data = {
        'model': 'uplogin.jsp',
        'service': 'https://jw.ustc.edu.cn/ucas-sso/login',
        'warn': '',
        'showCode': '',
        'username': username,
        'password': password,
        'button': '',
    }

    try:
        session = login(url, headers, data)
        semester_ID = session.get(semester_ID_url, headers=headers)
        semester_ID = BeautifulSoup(semester_ID.text, 'lxml')
        semester_ID = json.loads(semester_ID.p.string)
        semester_ID = sorted([unit['id'] for unit in semester_ID])
        assert len(semester_ID) > 0

        all_grade = process(session, semester_ID, headers, grade_url_base)
        latest_grade = process(session, semester_ID[-1:], headers, grade_url_base)
        integrate_grade = {}
        integrate_grade['record'] = latest_grade['record']
        integrate_grade['overview'] = {'all_gpa': all_grade['overview']['gpa'],
                                       'all_credits': all_grade['overview']['all_credits'],
                                       'latest_gpa': latest_grade['overview']['gpa'],
                                       'latest_credits': latest_grade['overview']['all_credits']}

        return json.dumps(integrate_grade)

    except BaseException:
        return json.dumps({})


def process(session, semester_ID, headers, grade_url_base):
    semester_ID = [str(unit) for unit in semester_ID]
    semester_ID = ','.join(semester_ID)

    grade_url = grade_url_base + semester_ID
    grade_info = session.get(grade_url, headers=headers)
    grade_info = BeautifulSoup(grade_info.text, 'lxml')
    grade_info = json.loads(grade_info.p.string)

    record = {}

    for idx in range(len(grade_info['semesters'])):
        record.update({x['courseNameCh']: {'score': x['score'], 'credits': x['credits'], 'gp': x['gp']}
                       for x in grade_info['semesters'][idx]['scores']})

    overview = {}
    overview['all_credits'] = grade_info['overview']['passedCredits']
    overview['gpa'] = grade_info['overview']['gpa']

    grade = {}
    grade['record'] = record
    grade['overview'] = overview
    return grade


if __name__ == "__main__":
    if (len(sys.argv) == 3):
        print(get_grade(sys.argv[1], sys.argv[2]), end='')
    else:
        print(json.dumps({}), end='')
