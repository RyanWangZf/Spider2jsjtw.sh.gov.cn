#-*- coding:utf-8 -*-
#Author: Ryan Wang
#Date: 2018/04/04
#Python 3.6.2 AMD64
#All Rights Reserved, No Commercial Use.
#A Crawler for http://jsjtw.sh.gov.cn.

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from lxml import etree
import os
import pandas as pd
import shutil

class Tender():
    #运行爬虫的函数
    def RunSpider(self):
        print('程序正在启动中,请稍等......')
        print('不要操作弹出的Chrome浏览器视图,最小化等待即可!')
        #检查是否设置日期
        if not os.path.exists(".//date_list.csv"):
            print("未设置起始或终止日期!")
            time.sleep(5)
            exit()
        #检查是否存在Pages文件夹
        if not os.path.exists('.//Pages'):
            os.makedirs('.//Pages')
        #检查chromedriver.exe是否存在
        if not os.path.exists('.//ChromeDriver/chromedriver.exe'):
            print('找不到ChromeDriver!程序无法运行!')
            time.sleep(5)
            exit()
        #读取URL
        try:
            f = open('.//url_list.txt')
            url = f.read()
            f.close()
        except:
            print("未发现URL文件,将采用默认URL进行爬取")
            url = "http://jsjtw.sh.gov.cn/gb/node2/n4/n14/n840/n918/u1ai175338.html"
        #读取日期
        df = pd.read_csv('date_list.csv')
        startdate = df.columns.values[0].replace('/','-')
        enddate = df.values[0][0].replace('/','-')
        
    
        chrome_options=Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("Block-image_v1.1.crx")

        #打开driver
        driver_path = ".//ChromeDriver//chromedriver.exe"
        driver=webdriver.Chrome(chrome_options=chrome_options)
        driver.get(url)
        time.sleep(3)
        #找到起始和终止日期的所有报道,提交日期表单
        driver.switch_to_frame(driver.find_element_by_name("mainframe"))
        driver.find_element_by_id("txtZbrqBegin").send_keys(startdate)
        driver.find_element_by_id("txtZbrqEnd").send_keys(enddate)
        driver.find_element_by_id("btnSearch").click()

        title = [];date=[];cat=[];

        html = driver.page_source
        root = etree.HTML(html)
        driver.set_page_load_timeout(10)
        #首页页面数
        init_pages = len(root.xpath('//tr[@class="pagestyle"]/td/table/tbody/tr/td'))
        if init_pages <= 10:
            for i in range(1,init_pages):
                print("正在爬取第%s页"%str(i))
                html = driver.page_source
                f = open('.\\Pages\\%s.txt'%str(i),'w')
                f.write(html)
                f.close()
                time.sleep(1)
                try:
                    driver.find_elements_by_xpath('//tr[@class="pagestyle"]/td/table/tbody/tr/td')[i].click()        
                except TimeoutException as e:
                    driver.execute_script('window.stop()')
        #首页页面多于10，有后续页面
        else:
            for i in range(1,11):
                print("正在爬取第%s页"%str(i))
                html = driver.page_source
                f = open('.\\Pages\\%s.txt'%str(i),'w')
                f.write(html)
                f.close()
                time.sleep(1)
                driver.find_elements_by_xpath('//tr[@class="pagestyle"]/td/table/tbody/tr/td')[i].click()
            page_rank = 11
            tag = 1
            while tag != 0:
                for i in range(2,12):
                    print("正在爬取第%s页"%str(page_rank))
                    html = driver.page_source
                    root = etree.HTML(html)
                    f = open('.\\Pages\\%s.txt'%str(page_rank),'w')
                    f.write(html)
                    f.close()
                    time.sleep(1)
                    page_rank += 1
                    try:
                        driver.find_elements_by_xpath('//tr[@class="pagestyle"]/td/table/tbody/tr/td')[i].click()
                    except:
                        tag = 0;break

        #开始处理html页面
        #依次处理爬取好的html文件并存入csv表格中
        title = [];date=[];cat=[];
        page_rank =  len(os.listdir(os.path.dirname(".//Pages//")))
        for i in range(1,page_rank+1):
            print('正在处理第%s页的页面数据...'%str(i))
            f = open('.\\Pages\\%s.txt'%str(i),'r')
            r = f.read()
            f.close()
            root = etree.HTML(r)
            #获得标题
            title.extend(root.xpath('//td[@align="left"]/a/text()'))
            #获得中标日期
            date_list = root.xpath('//td[@align="center" and @class="td"][2]/text()')
            date_list = [d.strip() for d in date_list]
            date.extend(date_list)
            #获得中标类型
            cat_list=root.xpath('//td[@align="center" and @class="td"][3]/text()')
            cat_list = [c.strip() for c in cat_list]
            cat.extend(cat_list)
    
        df = pd.DataFrame({"项目名称":title,"中标日期":date,"招标类型":cat})
        #去重
        df = df.drop_duplicates(['项目名称'])
        df.to_csv('projects.csv',index=False,encoding='utf_8_sig')
        #删除Pages文件夹
        shutil.rmtree('Pages')
        print('爬虫执行完毕,如出现错误请尝试再次启动,谢谢使用!')
