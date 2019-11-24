import requests


def login(url, headers, data):
    session = requests.Session()
    html = session.post(url, headers=headers,
                        data=data, allow_redirects=False)
    session2 = requests.Session()
    session2.get(
        html.headers['location'], headers=headers, allow_redirects=False)
    return session2
