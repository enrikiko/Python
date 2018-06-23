class User:
    """This is a description of th class"""
    def __init__(self, firstName, lastName, password, email):
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
        self.email = email
        import datetime
        self.time = datetime.datetime.now()
    def save(self):
        import pymysql
        conn = pymysql.connect(host='localhost', user='root', passwd='root', db='pythondb', port=8889)
        cursor = conn.cursor()
        users_query = ("""INSERT INTO users(firstName, lastName, password, email, creationTime)  VALUES ('{}','{}','{}','{}','{}')""".format(self.firstName, self.lastName, self.password, self.email, self.time))
        print(users_query)
        cursor.execute(users_query)
        conn.commit()
    def hello(self):
        print('Hello world this is {}'.format(self.firstName))



Enrique = User('Enrique', 'Ramos', '123456', 'e@e.com')
Enrique.save()
