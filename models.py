import pymysql
from app import db

# def get_conn():
#     host = '192.168.1.174'
#     port = 3306
#     db = 'swan'
#     user = 'root'
#     password = 'xxxx'
#     conn = pymysql.connect(host=host,port=port,user=user,password=password,db=db)
#     return conn

class User(db.Model):
    user_id = db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String)

    def __init__(self,user_id,user_name):
        self.user_id=user_id
        self.user_name=user_name
    #
    # def save(self):
    #     conn = get_conn()
    #     cursor = conn.cursor()
    #     sql = "insert into user (user_id,user_name)VALUES (%s,%s)"
    #     cursor.execute(sql,(self.user_id,self.user_name))
    #     conn.commit()
    #     cursor.close()
    #     conn.close()
    # pass
    #
    # @staticmethod
    # def query_all():
    #     # conn = get_conn()
    #     # cursor = conn.cursor()
    #     sql = "select * from USER "
    #     # cursor.execute(sql)
    #     # rows = cursor.fetchall()
    #     users = []
    #     for r in rows:
    #         user = User(r[0],r[1])
    #         users.append(user)
    #     conn.commit()
    #     cursor.close()
    #     conn.close()
    #     return users
    def __str__(self):
        return "id:{}-name:{}".format(self.user_name,self.user_id)