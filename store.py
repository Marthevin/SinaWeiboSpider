# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import glob
import os
from pymysql import Connection
import re
import sys
import time


# mysql connection String
HOST = 'localhost'
USER = 'root'
PASSWORD = 'admin'
DATABASE = 'sinaweibo'
PORT = 3306
CHARSET = 'utf8mb4'
connection = Connection(host=HOST, user=USER, password=PASSWORD, database=DATABASE, port=PORT, charset=CHARSET)
cursor = connection.cursor()


os.chdir(r"E:\project\data_rural_water_quality")


def get_file_list():
    cwd = os.getcwd()
    file_list = filter(os.path.isfile, glob.glob(cwd + r'\*.html'))
    file_list.sort(key=lambda x: os.path.getmtime(x))
    return file_list

file_list = get_file_list()
# print len(file_list)

nick_name_list = []
micro_content_list = []
post_time_list = []

# 匹配日期的正则表达式
pattern = re.compile(r'^\d{4}-\d{2}-\d{2}')

for file_ele in file_list:
    print "read " + file_ele
    file_read = open(file_ele)
    bsoup = BeautifulSoup(file_read.read(), "lxml")
    nick_name_list = bsoup.find_all('a', {'class': 'nk'})
    micro_content_list = bsoup.find_all('span', {'class': 'ctt'})
    post_time_list = bsoup.find_all('span', {'class': 'ct'})
    file_read.close()
    if len(nick_name_list) != len(micro_content_list) or len(nick_name_list) != len(post_time_list) or len(
            micro_content_list) != len(post_time_list):
        print "Data returned MalFormatted..." + file_ele
        sys.exit(0)
    post_time_date = None
    record_list = []
    # store content into database
    for i in range(len(nick_name_list)):
        nick_name = nick_name_list[i].text.lstrip(u"：")
        micro_content = micro_content_list[i].text
        post_time = post_time_list[i].text
        if pattern.match(post_time):
            post_time_date = pattern.match(post_time).group(0)
        # insert if Date Format is legal
        if post_time_date:
            record = (nick_name, micro_content, post_time_date)
            record_list.append(record)
            sql = "insert into rural_water_quality(from_user, post_content, post_date) VALUES (%s, %s, %s)"
            print "Record inserted Success!"
            cursor.execute(sql, record)
            connection.commit()
    time.sleep(0.08)

# TODO close mysql connection
connection.close()

