import pymysql


def Con():
    return pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='django',
        password='django',
        db='web_yunwei',
#		charset='utf8',
    )
