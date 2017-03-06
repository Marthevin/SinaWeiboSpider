# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import random
import time
import os
import atexit
import sys
import glob
import datetime


def random_sleep(factor):
    random_int = random.randint(3, 7)
    time.sleep(random_int*factor)

os.chdir(r'E:\project\data_rural_water_quality1')


# 这里获取系统传过来的参数 如果没有获取到则使用的值
start_time = u'20090816'
end_time = u'20150222'

if len(sys.argv) > 1:
    # 带入参数成功
    end_time = sys.argv[1]
    # 日期上线小于某个日期 退出程序
    if int(end_time) < 20100101:
        sys.exit(0)
    print "带入参数成功！ 新的日期上线为" + end_time


profile = webdriver.FirefoxProfile(r'D:\Develop\Config')
firefox = webdriver.Firefox(profile)
firefox.get('http://weibo.cn/search/mblog?advanced=mblog&f=s')
keyword_input = firefox.find_element_by_name('keyword')
origin_input = firefox.find_element_by_name('hasori')
start_time_input = firefox.find_element_by_name('starttime')
end_time_input = firefox.find_element_by_name('endtime')
search_btn = firefox.find_element_by_name('smblog')

keyword_input.clear()
keyword_input.send_keys(u'农村水质')
random_sleep(0.3)
origin_input.click()
random_sleep(0.3)
start_time_input.send_keys(start_time)
end_time_input.clear()
random_sleep(0.3)
end_time_input.send_keys(end_time)
search_btn.click()

try:
    WebDriverWait(firefox, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, u'下页'))
    )
except Exception, e:
    # 这里重试两次
    print e.message
    firefox.execute_script("history.go(-1)")
    random_sleep(0.4)
    search_btn = firefox.find_element_by_name('smblog')
    search_btn.click()
    try:
        WebDriverWait(firefox, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, u'下页'))
        )
    except Exception, e:
        print e.message
        firefox.execute_script("history.go(-1)")
        random_sleep(0.4)
        search_btn = firefox.find_element_by_name('smblog')
        search_btn.click()

random_sleep(0.3)
page_number = 101
i = 1
try:

    while i <= page_number:
        next_page_button = firefox.find_element_by_link_text(u'下页')
        next_page_button.click()
        WebDriverWait(firefox, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, u'下页'))
        )
        fp = open(start_time + '-' + end_time + '_page' + str(i) + ".html", 'w+')
        fp.writelines(firefox.page_source.encode('utf-8'))
        fp.close()
        random_sleep(0.6)
        i += 1

except Exception, e:
    print "No Result"+e.message
    # 这里重试三次
    random_sleep(0.3)
    firefox.execute_script("history.go(-1)")
    i -= 1
    try:

        while i <= page_number:
            next_page_button = firefox.find_element_by_link_text(u'下页')
            random_sleep(0.4)
            next_page_button.click()
            WebDriverWait(firefox, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, u'下页'))
            )
            fp = open(start_time + '-' + end_time + '_page' + str(i) + ".html", 'w+')
            fp.writelines(firefox.page_source.encode('utf-8'))
            fp.close()
            random_sleep(0.6)
            i += 1
    except Exception, e:
        print "No Result" + e.message
        random_sleep(0.3)
        firefox.execute_script("history.go(-1)")
        i -= 1
        try:

            while i <= page_number:
                next_page_button = firefox.find_element_by_link_text(u'下页')
                random_sleep(0.4)
                next_page_button.click()
                WebDriverWait(firefox, 10).until(
                    EC.presence_of_element_located((By.LINK_TEXT, u'下页'))
                )
                fp = open(start_time + '-' + end_time + '_page' + str(i) + ".html", 'w+')
                fp.writelines(firefox.page_source.encode('utf-8'))
                fp.close()
                random_sleep(0.6)
                i += 1
        except Exception, e:
            print "No Result" + e.message
            random_sleep(0.3)
            firefox.execute_script("history.go(-1)")
            i -= 1
            try:
                while i <= page_number:
                    next_page_button = firefox.find_element_by_link_text(u'下页')
                    random_sleep(0.4)
                    next_page_button.click()
                    WebDriverWait(firefox, 10).until(
                        EC.presence_of_element_located((By.LINK_TEXT, u'下页'))
                    )
                    fp = open(start_time + '-' + end_time + '_page' + str(i) + ".html", 'w+')
                    fp.writelines(firefox.page_source.encode('utf-8'))
                    fp.close()
                    random_sleep(0.6)
                    i += 1
            except Exception, e:
                print "No Result" + e.message
                random_sleep(0.3)
                firefox.execute_script("history.go(-1)")
                i -= 1
                try:
                    while i <= page_number:
                        next_page_button = firefox.find_element_by_link_text(u'下页')
                        random_sleep(0.4)
                        next_page_button.click()
                        WebDriverWait(firefox, 10).until(
                            EC.presence_of_element_located((By.LINK_TEXT, u'下页'))
                        )
                        fp = open(start_time + '-' + end_time + '_page' + str(i) + ".html", 'w+')
                        fp.writelines(firefox.page_source.encode('utf-8'))
                        fp.close()
                        random_sleep(0.6)
                        i += 1
                except Exception, e:

                    print "No Result" + e.message
                    random_sleep(0.3)
                    firefox.execute_script("history.go(-1)")
                    i -= 1
                    try:
                        while i <= page_number:
                            next_page_button = firefox.find_element_by_link_text(u'下页')
                            random_sleep(0.4)
                            next_page_button.click()
                            WebDriverWait(firefox, 10).until(
                                EC.presence_of_element_located((By.LINK_TEXT, u'下页'))
                            )
                            fp = open(start_time + '-' + end_time + '_page' + str(i) + ".html", 'w+')
                            fp.writelines(firefox.page_source.encode('utf-8'))
                            fp.close()
                            random_sleep(0.6)
                            i += 1
                    except Exception, e:

                        print "No Result" + e.message
                        random_sleep(0.3)
                        firefox.execute_script("history.go(-1)")
                        i -= 1
                        try:
                            while i <= page_number:
                                next_page_button = firefox.find_element_by_link_text(u'下页')
                                random_sleep(0.4)
                                next_page_button.click()
                                WebDriverWait(firefox, 10).until(
                                    EC.presence_of_element_located((By.LINK_TEXT, u'下页'))
                                )
                                fp = open(start_time + '-' + end_time + '_page' + str(i) + ".html", 'w+')
                                fp.writelines(firefox.page_source.encode('utf-8'))
                                fp.close()
                                random_sleep(0.6)
                                i += 1
                        except Exception, e:

                            print "No Result" + e.message
                            random_sleep(0.3)
                            firefox.execute_script("history.go(-1)")
                            i -= 1
                            try:
                                while i <= page_number:
                                    next_page_button = firefox.find_element_by_link_text(u'下页')
                                    random_sleep(0.4)
                                    next_page_button.click()
                                    WebDriverWait(firefox, 10).until(
                                        EC.presence_of_element_located((By.LINK_TEXT, u'下页'))
                                    )
                                    fp = open(start_time + '-' + end_time + '_page' + str(i) + ".html", 'w+')
                                    fp.writelines(firefox.page_source.encode('utf-8'))
                                    fp.close()
                                    random_sleep(0.6)
                                    i += 1
                            except Exception, e:

                                print "No Result" + e.message
                                random_sleep(0.3)
                                firefox.execute_script("history.go(-1)")
                                i -= 1
                                try:
                                    while i <= page_number:
                                        next_page_button = firefox.find_element_by_link_text(u'下页')
                                        random_sleep(0.4)
                                        next_page_button.click()
                                        WebDriverWait(firefox, 10).until(
                                            EC.presence_of_element_located((By.LINK_TEXT, u'下页'))
                                        )
                                        fp = open(start_time + '-' + end_time + '_page' + str(i) + ".html", 'w+')
                                        fp.writelines(firefox.page_source.encode('utf-8'))
                                        fp.close()
                                        random_sleep(0.6)
                                        i += 1
                                except Exception, e:

                                    print "No Result" + e.message
                                    random_sleep(0.3)
                                    firefox.execute_script("history.go(-1)")
                                    i -= 1
    # 写入最后一页数据
print "写入最后一页数据"
try:
    WebDriverWait(firefox, 10).until(
        EC.presence_of_element_located(
            (By.LINK_TEXT, u'上页'))
    )
    fp = open(start_time + '-' + end_time + '_page' + str(page_number+2) + ".html", 'w+')
    fp.writelines(firefox.page_source.encode('utf-8'))
    fp.close()
except Exception, e:
    print e.message
    print "No Result"
# print BeautifulSoup(firefox.page_source, "lxml").prettify()


def get_new_uppers():
    cwd = os.getcwd()
    file_list = filter(os.path.isfile, glob.glob(cwd + r'\*.html'))
    file_list.sort(key=lambda x : os.path.getmtime(x))  # 升序 创建时间从早到晚排列 因此取最后一个文件
    print len(file_list)
    file_read = open(file_list[-1])
    bsoup = BeautifulSoup(file_read.read(), "lxml")
    time_tag = bsoup.select('.ct')
    if len(time_tag) > 0:
        time_str = time_tag[-1].text
        new_date_upper = time_str.split(" ")[0].split("-")
        new_date = datetime.datetime(int(new_date_upper[0]), int(new_date_upper[1]), int(new_date_upper[2])) - datetime.timedelta(1)
        return str(new_date).split(" ")[0].replace("-", "")


def exit_handle_method():
    firefox.quit()
    new_upper = get_new_uppers()
    if len(new_upper) == 8:
        os.system("python E:\project\Github\spider\SinaSpider\Sina_spider1\\test\weibo2013.py "+new_upper)

atexit.register(exit_handle_method)