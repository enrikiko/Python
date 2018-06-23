import pymysql
conn = pymysql.connect(host='localhost', user='root', passwd='root', db='learning_over_here', port=8889)
cursor = conn.cursor()
users_query = ("SHOW DATABASES")
cursor.execute(users_query)
conn.commit()

users_query = ("CREATE DATABASE pythondb")
cursor.execute(users_query)
conn.commit()

users_query = ("USE pythondb")
cursor.execute(users_query)
conn.commit()

users_query = ("CREATE TABLE users(firstName VARCHAR(50) NOT NULL,lastName VARCHAR(50) NOT NULL,password VARCHAR(16) NOT NULL,email VARCHAR(50) NOT NULL,creationTime VARCHAR(50) NOT NULL)")
cursor.execute(users_query)
conn.commit()
