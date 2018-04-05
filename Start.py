#-*- coding: utf-8 -*-
#Author: Zifeng Wang
#Date: 2018/04/04
#Python 3.6.2 AMD64
#All Rights Reserved, No Commercial Use.
#A Crawler for http://jsjtw.sh.gov.cn.

from PyQt5 import QtWidgets
from Ui_SpiderRunner import Ui_Form
from TenderSpider import Tender
import sys,time
import pandas as pd


class mydesignershow(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(mydesignershow,self).__init__()
        self.setupUi(self)
        self.RunButton.clicked.connect(self.Run)
    def Run(self):
        #开始运行应将日期框里的日期取出来传入TenderSpider中
        url = self.URLEdit.text()
        f = open('url_list.txt','w+',encoding='utf-8')
        f.write(url)
        f.close()
        s_date = self.Start_date.text()
        e_date = self.End_date.text()
        s_d = time.mktime(time.strptime(s_date,"%Y/%m/%d"))
        e_d = time.mktime(time.strptime(e_date,"%Y/%m/%d"))
        n_d = time.time()
        date_list = pd.Series([s_date,e_date])
        date_list.to_csv('date_list.csv',index=0) 
        if e_d - s_d < 0 or n_d - e_d<0:
            print("日期设置错误!请检查后重新设置!")
            print("程序即将退出......")
            time.sleep(5)
            exit()
        Tender.RunSpider(self)
        
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = mydesignershow()
    myshow.show()
    sys.exit(app.exec_())
