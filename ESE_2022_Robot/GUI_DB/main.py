from threading import Thread
import time
import sys
from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import database
reload(sys)
sys.setdefaultencoding('utf-8')

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
        self.th = Thread1()
        self.th2 = Thread2()
    
    
    #button actions    
    def button(self):
        self.start_1.clicked.connect(self.goto6)
        self.finsave_6.clicked.connect(self.goto2)
        self.seerecord_1.clicked.connect(self.goto3)
        self.calibration_1.clicked.connect(self.goto4)

        self.gotohome_2.clicked.connect(self.gotohome)
        self.gotohome_3.clicked.connect(self.gotohome)
        self.gotohome_4.clicked.connect(self.gotohome)
        self.goto3_5.clicked.connect(self.goto3)
        #self.startfinish_2.clicked.connect(self.start_finish)
        self.startfinish_2.clicked.connect(self.workoutestimate)
        
        self.giverecord_3.clicked.connect(self.giverecord)
        self.givefeedback_3.clicked.connect(self.givefeedback)
        self.info_3.clicked.connect(self.giveinfo)
        self.pushButton.clicked.connect(self.liveupdate)
        
        self.addroutine_6.clicked.connect(self.addroutine)
        self.deleteroutine_6.clicked.connect(self.deleteroutine)
        self.nowroutine_6.activated[str].connect(self.changeroutinepage)
        self.saveroutinedb_6.clicked.connect(self.saveroutine)
        
    #silsigan pose-check
    def goto2(self):
        self.stackedWidget.setCurrentWidget(self.page_2)
        self.nowroutine_2.setText(self.nowroutine_6.currentText())   
    
    # record
    def goto3(self):
        mydb = database.db()
        
        current_day = QDate.currentDate()
        self.stackedWidget.setCurrentWidget(self.page_3)
        for i in range(1,8,1):
            nowday = "day"+str(i)+"_3"
            getattr(self, nowday).setText(current_day.addDays(i-7).toString('MM.dd'))

        # weekrecord
        for i in range(7):
            nowday = current_day.addDays(-i).toString('yyyy-MM-dd')
            row = mydb.returnDayworkoutRows(nowday)
            count = len(row)

            for x in range(count):
                name, time = row[x] 
                workrecord = "day"+str(7-i)+str(x+1)+"_3"
                getattr(self, workrecord).setText(name+time)
        
        
        
        
        
        
        
        
        
        
        # for x in range(count):
        #     day, name, time = row[x]
        #     for i in range(7):
        #         if day == current_day.addDays(-i).toString('yyyy-MM-dd'):
        #             for z in range(6):
        #                 workrecord = "day"+str(7-i)+str(z+1)+"_3"
        #                 if getattr(self, workrecord).text()!=None:
        #                     continue
        #                 getattr(self, workrecord).setText(name+time)
            
            # if day == current_day.toString('YY-MM-dd'):
            #     print("good")
            #     for i in range(1, 6):
            #         day7 = "day7" +str(i)+ "_3"
            #         getattr(self, day7).setText(name, time)
        # self.day7_3.setText(current_day.toString('MM.dd'))
        # self.day6_3.setText(current_day.addDays(-1).toString('MM.dd'))
        # self.day5_3.setText(current_day.addDays(-2).toString('MM.dd'))
        # self.day4_3.setText(current_day.addDays(-3).toString('MM.dd'))
        # self.day3_3.setText(current_day.addDays(-4).toString('MM.dd'))
        # self.day2_3.setText(current_day.addDays(-5).toString('MM.dd'))
        # self.day1_3.setText(current_day.addDays(-6).toString('MM.dd'))
        
    #calibration
    def goto4(self):
        self.stackedWidget.setCurrentWidget(self.page_4) 
        mydb = database.db()
        mydb.printwork()
        
    def goto6(self):
        self.stackedWidget.setCurrentWidget(self.page_6)    

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
        #woondongsizak
        if a%2 == 0:       
            print(self.cb1_2.currentText())
            print(self.cb2_2.currentText())  
            print(self.cb3_2.currentText())     
            #self.nowstate_2.setText(self.cb1_2.currentText())  
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
            #self.nowstate_2.setText("")  
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
    
    # def addroutine(self):
    #     if self.nowroutine_6.currentText() == "routine 1" :
    #         for i in range(5):
    #             #if self.nowroutine_6.currentText() == str("routine " + i):
    #             if self.routine_1.item(i,0) == None:
    #                 break
    #         self.routine_1.setItem(i, 0, QTableWidgetItem(self.cb1_6.currentText()))
    #         self.routine_1.setItem(i, 1, QTableWidgetItem(self.cb2_6.currentText()))
    #         self.routine_1.setItem(i, 2, QTableWidgetItem(self.cb3_6.currentText()))
    #         self.routine_1.setItem(i, 3, QTableWidgetItem(self.cb4_6.currentText()))
    def changeroutinepage(self):
        for i in range(1,7,1):
            if self.nowroutine_6.currentText() == "routine " +str(i) :
                currentroutinepage = "routinepage_"+str(i)    
                self.stackedWidget_2.setCurrentWidget(getattr(self, currentroutinepage))
        
        
    def addroutine(self):
        for i in range(1,7,1):
            if self.nowroutine_6.currentText() == "routine " +str(i) :
                currentroutine = "routine_"+str(i)
                for j in range(5):
                    if getattr(self, currentroutine).item(j,0) == None:
                        break
        getattr(self, currentroutine).setItem(j, 0, QTableWidgetItem(self.cb1_6.currentText()))
        getattr(self, currentroutine).setItem(j, 1, QTableWidgetItem(self.cb2_6.currentText()))
        getattr(self, currentroutine).setItem(j, 2, QTableWidgetItem(self.cb3_6.currentText()))
        getattr(self, currentroutine).setItem(j, 3, QTableWidgetItem(self.cb4_6.currentText()))        
          
    def deleteroutine(self):
        for i in range(1,7,1):
            if self.nowroutine_6.currentText() == "routine "+str(i):
                currentroutine = "routine_"+str(i)
                for j in range(4,-1,-1):
                    if getattr(self, currentroutine).item(j,0) != None:
                        break
        getattr(self, currentroutine).setItem(j, 0, None)
        getattr(self, currentroutine).setItem(j, 1, None)
        getattr(self, currentroutine).setItem(j, 2, None)
        getattr(self, currentroutine).setItem(j, 3, None)
         
    #   
    def liveupdate(self):
        self.th.start()
        self.th.change_value2.connect(self.label_83.setText)
        self.th.change_value1.connect(self.label_87.setText)

    def saveroutine(self):
        mydb = database.db()
        #mydb.insertWorkoutData()
        print(self.routine_1.item(0, 0).text())
        
    def workoutestimate(self):
        global a
        a = a+1
        self.th2.start() 
        self.th2.exername.connect(self.label_7.setText)
        self.th2.exerset.connect(self.leftset_2.setText)
        self.th2.exercount.connect(self.lefttry_2.setText)
        self.th2.resttime.connect(self.resttime_2.setText)
        #
        #woondongsizak
        # if a%2 == 0:
        #     self.th2.estimateworkout(b,c,d,e)
        #     self.th2.exername.connect(self.label_7.setText)
        #     self.th2.exerset.connect(self.leftset_2.setText)
        #     self.th2.exercount.connect(self.lefttry_2.setText)
        #     self.th2.resttime.connect(self.resttime_2.setText)
               
            
        
class Thread1(QThread): 
    
    change_value1 = pyqtSignal(str)
    change_value2 = pyqtSignal(str)
   
    def __init__(self): 
        QThread.__init__(self) 
        #self.cond = QWaitCondition()
        #self.mutex = QMutex()
        
        
    def run(self): 
        self.change_value2.emit("1start.") 
        for i in range(20): 
            self.change_value1.emit(str(i)) 
            time.sleep(2) 
        self.change_value2.emit("arrive.")
        
class Thread2(QThread):
    
    exername = pyqtSignal(str)
    exerset = pyqtSignal(str)
    exercount = pyqtSignal(str)
    resttime = pyqtSignal(str)
    def __init__(self): 
       QThread.__init__(self)       

    def run(self):
        name = "benchpress"
        set = 5
        count = 10
        rest = 20
        self.exername.emit(name)
        for i in range(set):
            self.exerset.emit(str(set))
            for j in range(count):
                self.exercount.emit(str(count))
                count =count-1
                #print("?")
                time.sleep(1)
            set = set-1
            for k in range(rest):
                self.resttime.emit(str(rest-k))
                time.sleep(1)
        
               
    
            
        
        
        

if __name__ == '__main__':        
    app = QtGui.QApplication(sys.argv)
    mainWindow = UI()
    mainWindow.show()
    sys.exit(app.exec_())
