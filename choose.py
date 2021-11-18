import zsc_sql_tools as tool
import random


#import pandas

#prepare
class Person():
    def __init__(self, number, name, name2):
        self.number = number
        self.name = name
        self.name2 = name2
        self.percent_random = 0.25
        self.percent_data = 0.25
        self.percent_final = 0.25
zyb = Person(1, 'zyb', '1')
zsc = Person(2, 'zsc', '2')
aqy = Person(3, 'aqy', '3')
cm = Person(4, 'cm', '4')
list_person = [zyb, zsc, aqy, cm]

# start

#q = int(input("start:"))
#w = int(input("over:"))
#num_human = int(input("umber_of_person:"))
input("ready to start")
time_n = int(input("Time:"))


def f():
    list_a = []
    for i in range(1, 1024):
        a = random.randint(1, 4)
        list_a.append(a)


    for j in list_a:
        y = random.randint(0, 1)
        if y and list_a.__len__() != 1:
            list_a.remove(j)
    return list_a

list_random = f()
for m in list_person:
    m.percent_random = list_random.count(m.number) / list_random.__len__()

#random over

#data_sql start
'''
数据类型
mytools
waterlist
number int auto_increment primary key
id1 int
id2 int
id3 int
id4 int
time int
'''

'''
def get_command(word):
    sql = word
def do_command(word2):
    cursor.execute(word2)
def get_result():
    data = cursor.fetchall()
    return data
def close():
    cursor.close()
    db.close()
'''

tool.do_command('use mytools;')
tool.do_command('select * from waterlist;')

data_here = tool.get_result()
list_data = []
for dic_x in data_here[2:]:
    list_data.append(dic_x.get('id1'))
    list_data.append(dic_x.get('id2'))
    list_data.append(dic_x.get('id3'))
    list_data.append(dic_x.get('id4'))

for e in list_data:
    if e == 0:
        list_data.remove(e)

for m2 in list_person:
    m2.percent_data = 1 - list_data.count(m2.number) / list_data.__len__()

#start count
len_data_here = data_here.__len__()
data_percent = 0.5
random_percent = (1 - data_percent)/3

for m3 in list_person:
    m3.percent_final = m3.percent_data*data_percent + m3.percent_random*random_percent

list_record = []
list_t = [zyb.percent_final, zsc.percent_final, aqy.percent_final, cm.percent_final]
list_record = []
list_t.sort(reverse=True)
list_t.pop()
list_t.pop()
for man in list_person:
    if man.percent_final in list_t:
        list_record.append(man.number)

print(f"the numbers are: {list_record[0]}, {list_record[1]}")
print(f"{list_person[list_record[0]-1].name2} and {list_person[list_record[1]-1].name2}")
#print(list_record[0])
#print(list_record[1])

#insert into
list_insert = [0, 0, 0, 0]
list_insert[list_record[0]-1] = list_record[0]
list_insert[list_record[1]-1] = list_record[1]
insert_word = f"{len_data_here+1}, {list_insert[0]}, {list_insert[1]}, {list_insert[2]}, {list_insert[3]}, {time_n}"






#record


try:
    tool.do_command("insert into waterlist values (%s);" % insert_word)

    tool.db.commit()


except:
    tool.db.rollback()
    print("wrong")

tool.do_command("select * from waterlist;")
data = tool.get_result()
for i in data:
    print(i)
print(f"The next number should be: {len_data_here+1}")




tool.close()
#tool.do_command("exit")


'''
print(dic_x)
print(data_here)
print(list_data)
'''
