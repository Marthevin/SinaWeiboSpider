# -*- coding: utf-8 -*-

from pymysql import Connection
import time

HOST = 'localhost'
USER = 'root'
PASSWORD = 'admin'
DATABASE = 'sinaweibo'
PORT = 3306
CHARSET = 'utf8mb4'
connection = Connection(host=HOST, user=USER, password=PASSWORD, database=DATABASE, port=PORT, charset=CHARSET)
cursor = connection.cursor()

sql = 'select * from rural_water_quality'
cursor.execute(sql)
# TODO fetch all when deploy
result = cursor.fetchall()
print len(result)

neat_list = []


def contains(src_list, target):
    for ele in src_list:
        if ele[2] == target[2]:
            return True
    return False

for record in result:
    if len(neat_list) == 0:
        neat_list.append(record)
    else:
        print "neat record list length is: " + str(len(neat_list))
        if not contains(neat_list, record):
            neat_list.append(record)
        time.sleep(0.005)

print "clear duplicated record complete! new clean table contains " + str(len(neat_list)) + " rows..."
time.sleep(1)

i = 1
for record in neat_list:
    # TODO replace test to new table
    # further clean record to remove :
    from_user = record[1]
    post_content = record[2]
    post_date = record[3]
    new_content = post_content.lstrip(":")
    new_record = (from_user, new_content, post_date)
    sql = 'insert into neat_rural_water_quality(from_user, post_content, post_date) VALUES(%s, %s, %s)'
    cursor.execute(sql, new_record)
    connection.commit()
    print str(i) + " record inserted! "
    i += 1
    time.sleep(0.003)

# TODO close Connection
connection.close()