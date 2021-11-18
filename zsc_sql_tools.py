import pymysql
db = pymysql.connect(host='localhost',
                     user='supercro',
                     password='supercro',
                     db='',
                     charset='utf8',
                     cursorclass=pymysql.cursors.DictCursor)

cursor = db.cursor()#create cursor

def get_command(word):
    sql = word

def do_command(word2):
    cursor.execute(word2)


def com():
    db.commit()

def get_result():

    data = cursor.fetchall()
    return data



def close():
    cursor.close()
    db.close()

if __name__ =='__main__':
    do_command("use mytools;")
    do_command("select * from waterlist;")
    data = get_result()
    for i in data:
        print(i)
