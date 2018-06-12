import pymysql
conn = pymysql.connect(host='localhost', user='root', passwd='root', db='learning_over_here', port=8889)
cursor = conn.cursor()
users_query = ("INSERT INTO `users`(`username`, `password`, `user_email`, `first_name`, `last_name`) VALUES ('enrikiko_91','123456','enrikiko_91@hotmail.com','Enrique','Ramos')")
cursor.execute(users_query)
conn.commit()
