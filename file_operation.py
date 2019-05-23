# --*--coding:utf-8 --*--
"""
@author: XXX
@testcase description: XXX
@date: XXX
"""

import unittest
import time
import os
import datetime
import random
import string
import calendar


class File_Operation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        curpath = os.getcwd()
        folder_path = os.path.join(curpath, 'FileOperation')
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))

        if os.path.exists(folder_path):
            os.rmdir(folder_path)

    def test_mkdir(self):
        #获取当前文件的目录
        path = os.getcwd()
        print(path)

        #查看当前文件是否存在
        curdate = time.strftime('%Y%m%d', time.localtime(time.time()))
        dirname = os.path.join(path, curdate)
        print(dirname)

        #创建文件夹
        if not os.path.exists(dirname):
            os.mkdir(dirname)

        #新建日志文件
        curtime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        logfile = os.path.join(dirname, curtime+'.txt')
        print(logfile)


        #写入日志
        file = open(logfile, "w+")
        str1 = str(time.strftime("%Y-%m-%d: %H:%M:%S", time.localtime(time.time())))+\
               ": error:1024 test test hello world\n"
        str2 = str(datetime.datetime.now())+": Hello the world!"
        file.write(str1)
        file.write(str2)
        file.close()

        #读取日志文件
        file1 = open(logfile, 'r')
        print(file1.readlines())
        file1.close()

        #删除日志文件以及日志目录
        # print(os.walk(path, topdown=False))
        for root, dirs, files in os.walk(dirname, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))

        os.rmdir(dirname)


    def test_newfile(self):
        '''文件内容的新增、删除、查找、修改'''
        #文件内容的新增

        curpath = os.getcwd()
        folder_path = os.path.join(curpath, 'FileOperation')
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

        file_path = os.path.join(folder_path, 'test.txt')
        fo = open(file_path, 'w+')
        for i in range(0, 10):
            ran_str = ''.join(random.sample(string.ascii_letters + string.digits,20))
            fo.write(ran_str+'\n')

        fo.seek(0,0)  #回到文件的开头
        print(fo.readlines())
        fo.close()

    def test_findKey(self):
        curpath = os.getcwd()
        file_path = os.path.join(curpath, 'FileOperation','test.txt')
        save_file = os.path.join(curpath, 'FileOperation', 'save_key.txt')

        fo = open(file_path, 'r')
        save_fo = open(save_file, 'w+')

        cnt = 0
        for line in fo:
            if "a" in line:
                print(line)

                save_fo.write(line)
                cnt += 1
        print("cnt = ", cnt)

        save_fo.seek(0,0)
        print(save_fo.readlines())

        fo.close()
        save_fo.close()


    def test_calender(self):
        cal = calendar.month(2019, 5)
        print("以下输出2019年5月份的日历:")
        print(cal)

        print(calendar.isleap(2000))
        # print(calendar.firstweekday())
        print(calendar.calendar(2019,w=2,l=1,c=6))

    def test_random_digit_letter(self):
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 20))
        print(ran_str)
        print(string.ascii_letters)
        print(string.digits)

if __name__ == '__main__':
    unittest.main()






