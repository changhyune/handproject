

import sys
from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtCore import *
import database

form_class = uic.loadUiType("userui.ui")[0]

a=1
set = 0
count = [] 

class UI(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        #super().__init__()
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        timer = QTimer(self)
        timer.timeout.connect(self.nowtime)
        timer.start(1000)
        
        self.button()
        self.nowtime()
        self.exercount()
    
    
    #button actions    
    def button(self):
        self.start_1.clicked.connect(self.goto2)
        self.seerecord_1.clicked.connect(self.goto3)
        self.calibration_1.clicked.connect(self.goto4)

        self.gotohome_2.clicked.connect(self.gotohome)
        self.gotohome_3.clicked.connect(self.gotohome)
        self.gotohome_4.clicked.connect(self.gotohome)
        self.goto3_5.clicked.connect(self.goto3)
        self.startfinish_2.clicked.connect(self.start_finish)
        
        self.giverecord_3.clicked.connect(self.giverecord)
        self.givefeedback_3.clicked.connect(self.givefeedback)
        self.info_3.clicked.connect(self.giveinfo)
        
    #silsigan pose-check
    def goto2(self):
        self.stackedWidget.setCurrentWidget(self.page_2)   
    
    # record
    def goto3(self):
        current_day = QDate.currentDate()
        self.stackedWidget.setCurrentWidget(self.page_3)
        self.day7_3.setText(current_day.toString('MM.dd'))
        self.day6_3.setText(current_day.addDays(-1).toString('MM.dd'))
        self.day5_3.setText(current_day.addDays(-2).toString('MM.dd'))
        self.day4_3.setText(current_day.addDays(-3).toString('MM.dd'))
        self.day3_3.setText(current_day.addDays(-4).toString('MM.dd'))
        self.day2_3.setText(current_day.addDays(-5).toString('MM.dd'))
        self.day1_3.setText(current_day.addDays(-6).toString('MM.dd'))
        
    #calibration
    def goto4(self):
        self.stackedWidget.setCurrentWidget(self.page_4) 
        mydb = database.db()
        mydb.printwork()

    # three button
    def gotohome(self):
        self.stackedWidget.setCurrentWidget(self.page)
        
    def nowtime(self):
        current_day = QDate.currentDate()
        current_time = QTime.currentTime()
        day = current_day.toString('yyyy.MM.dd')
        time = current_time.toString('hh:mm:ss')
        
        self.time_1.setText(day +" " +time) 
        self.time_2.setText(day +" "+ time) 
        self.time_3.setText(day +" " +time) 
        self.time_4.setText(day +" "+ time) 
        self.time_5.setText(day +" "+ time) 
        
    def start_finish(self):
        global a
        a = a+1
        if a%2 == 0:       
            print(self.cb1_2.currentText())
            print(self.cb2_2.currentText())  
            print(self.cb3_2.currentText())     
            self.nowstate_2.setText(self.cb1_2.currentText())  
            self.leftangle1_2.setText("check")
            self.leftangle2_2.setText("check")
            self.rightangle1_2.setText("check")
            self.rightangle2_2.setText("check")
            self.leftset_2.setText(self.cb2_2.currentText())
            self.lefttry_2.setText(self.cb3_2.currentText())
            
        else :
            print(self.cb1_2.currentText())
            print(self.cb2_2.currentText())  
            print(self.cb3_2.currentText())     
            self.nowstate_2.setText("")  
            self.leftangle1_2.setText("notcheck")
            self.leftangle2_2.setText("notcheck")
            self.rightangle1_2.setText("notcheck")
            self.rightangle2_2.setText("notcheck")
            self.leftset_2.setText("")
            self.lefttry_2.setText("")

    # undong tonggue
    def giverecord(self):
        self.stackedWidget.setCurrentWidget(self.page_5) 
        print(" giverecord.")
        
    # feedback
    def givefeedback(self):     
        print("feedback.")       
    
    # workout info
    def giveinfo(self):
        print("giveinfo")
        
    def exercount(self):
        global a
    
            
        
        
        

if __name__ == '__main__':        
    app = QtGui.QApplication(sys.argv)
    mainWindow = UI()
    mainWindow.show()
    sys.exit(app.exec_())
