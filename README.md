# USTC Grade Query

> 用于快速查询中科大学生成绩。

## 简介

用于快速查询中科大学生成绩，输入学号、密码后，能显示总体学分、总体 GPA 、本期学分、本期 GPA 以及本期的已出成绩。

分为前端和后端。前端使用 Bootstrap 框架，利用 Ajax 实现免刷新更新信息，前端接受用户输入的学号、密码，并负责显示成绩。后端使用 Python 脚本利用爬虫原理获取成绩，使用 Flask 搭建 API 并用 Nginx 将其转发到 80/443 端口，API 地址：https://yusanshi.com/api/get_grade/ 。

演示站：https://yusanshi.com/GPA

> 为了安全，请勿轻易在别人搭建的第三方网页上输入自己的学号、密码（包括上面的我自己的站点），除非您信任该站长。建议浏览代码确认没问题后自行搭建网站。



见 https://blog.yusanshi.com/2019-11-24-flask-api/ 。