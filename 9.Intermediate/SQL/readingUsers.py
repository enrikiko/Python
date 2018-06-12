import pymysql
conn = pymysql.connect(host='localhost', user='root', passwd='root', db='learning_over_here', port=8889)
cursor = conn.cursor()
users_query = ('Select * from users')
cursor.execute(users_query)
users_db = cursor.fetchall()

for user in users_db:
    print user
