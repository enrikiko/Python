import pymysql
conn = pymysql.connect(host='localhost', user='root', passwd='root', db='learning_over_here', port=8889)
cursor = conn.cursor()
users_query = ("DELETE FROM `users`")
cursor.execute(users_query)
conn.commit()
