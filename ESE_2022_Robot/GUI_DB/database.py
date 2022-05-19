# -*- coding:utf-8 -*-

import sqlite3
import random

class sqlite_lib:

    dbname =""
    db = None
    cursor = None

    def open(self, name):
        self.dbname = name
        self.db = sqlite3.connect(self.dbname)
        self.cur = self.db.cursor()

    def close(self):
        if self.db != None:
            self.db.close()

    def commit(self):
        self.db.commit()

    def sql_exec(self, sql):
        self.cur.execute(sql)
        self.commit()

        return self.cur

class db(sqlite_lib):

    # 센서 데이터 테이블 생성 함수(roll pitch yaw)
    def createSensorTable(self):
        
        self = sqlite_lib()
        self.open("database.db")

        sqlL = '''CREATE TABLE if not exists leftsensor(
        time DATETIME DEFAULT (DATETIME('now', 'localtime')),
        roll float not null,
        pitch float not null,
        yaw float not null)'''

        sqlR ='''CREATE TABLE if not exists rightsensor(
        time DATETIME DEFAULT (DATETIME('now', 'localtime')),
        roll float not null,
        pitch float not null,
        yaw float not null)'''

        self.sql_exec(sqlL)
        self.sql_exec(sqlR)
        self.close()

    # 센서 데이터 테이블에서 운동별 자세 측정을 위해 데이터 추출 함수
    def classifySensorData(self):
        self = sqlite_lib()
        self.open("database.db")

        num = int(raw_input('운동 종류 선택: ')
        )
        if num == 1:
            sql = '''SELECT * FROM sensor WHERE id="%s"'''%num
            self.sql_exec(sql)
            rows = self.cur.fetchall()

            for row in rows:
                print(row)

            self.close()

        elif num == 2:
            sql = '''SELECT * FROM sensor WHERE id="%s"'''%num

            self.sql_exec(sql)
            rows = self.cur.fetchall()

            for row in rows:
                print(row)

            self.close()

        elif num == 3:
            sql = '''SELECT * FROM sensor WHERE id="%s"'''%num

            self.sql_exec(sql)
            rows = self.cur.fetchall()

            for row in rows:
                print(row)

            self.close()

        elif num == 4:
            sql = '''SELECT * FROM sensor WHERE id="%s"'''%num

            self.sql_exec(sql)
            rows = self.cur.fetchall()

            for row in rows:
                print(row)

            self.close()

    # 센서 데이터 테이블에서 운동 종류에 따라 테이블 데이터 출력
    def getSensorData(self):
        self = sqlite_lib()
        self.open("database.db")

        num = int(raw_input("운동종류선택: "))

        while num != 0:
            for i in range(10):
                data = (num, random.random(), random.random(), random.random()
                    , random.random(), random.random(), random.random()
                    , random.random(), random.random(), random.random()
                    , random.random(), random.random(), random.random()
                    , random.random(), random.random(), random.random()
                    , random.random(), random.random(), random.random()
                    , random.random(), random.random(), random.random()
                    , random.random(), random.random(), random.random())

                sqlInsert = '''INSERT INTO sensor(
                    id, Lfsr1, Lfsr2, Lfsr3, Rfsr1, Rfsr2, Rfsr3,
                    LaccelX, LaccelY, LaccelZ, LgyroX, LgyroY, LgyroZ, LmagX, LmagY, LmagZ,
                    RaccelX, RaccelY, RaccelZ, RgyroX, RgyroY, RgyroZ, RmagX, RmagY, RmagZ
                    ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''

                self.cur.execute(sqlInsert, data)
                self.commit()
            num = int(raw_input("종료: 0 다른 운동종류선택: ?"))

        self.close()

    # 센서 데이터 저장 후 계산
    def saveSensorData(self):
        self = sqlite_lib()
        self.open("database.db")

    # 운동목표 데이터 베이스 생성 함수
    def createWorkoutData(self):
        self = sqlite_lib()
        self.open("database.db")
        
        # 운동 목표 데이터 베이스(id, 운동이름, 목표 세트, 목표 개수)
        sql1 = '''CREATE TABLE if not exists workout(
            id integer not null primary key autoincrement,
            name text not null,
            aim_set int not null,
            aim_num int not null)'''

        # 운동 루틴 데이터 베이스(id, 루틴 이름)
        sql2 = '''CREATE TABLE if not exists routine(
            id integer not null primary key autoincrement,
            name text not null)
            '''

        # 운동 루틴-종류 매핑 데이터 베이스(루틴id, 운동종류id)
        sql3 = '''CREATE TABLE if not exists mappingR2W(
            routineid integer not null,
            workoutid integer not null)
            '''

        # 장기 피드백 데이터 베이스(날짜, 운동 루틴)
        sql4 = '''CREATE TABLE if not exists daywork(
            time DATETIME DEFAULT (strftime('%Y-%m-%d', DATETIME('now', 'localtime'))),
            name text not null)'''


        # 단기 피드백 데이터 베이스(시간, )
        sql5 = '''CREATE TABLE if not exists livedata(
            time text not null,
            name text not null,
            leftFB float not null,
            rightFB float not null,
            leftLR float not null,
            rightLR float not null
            )'''

        self.sql_exec(sql1)
        self.sql_exec(sql2)
        self.sql_exec(sql3)
        self.sql_exec(sql4)
        self.sql_exec(sql5)
        self.close()

    # 운동 정보 입력 함수
    def insertWorkoutData(self):
        self = sqlite_lib()
        self.open("database.db")

        key = int(raw_input('운동 종류 입력 [0], 운동 루틴 이름 [1], 운동 루틴 결정 [2]'))

        if key == 0:
            name = raw_input('운동이름: ')
            aim_set = int(raw_input('목표세트: '))
            aim_num = int(raw_input('목표개수: '))

            sqlInsert = '''INSERT INTO workout(name, aim_set, aim_num) VALUES(
                '{}', '{}', '{}')'''.format(name, aim_set, aim_num)

            self.sql_exec(sqlInsert)
            self.close()

        elif key == 1:
            name = raw_input('루틴이름: ')

            sqlInsert = '''INSERT INTO routine(name) VALUES('{}')'''.format(name)
            self.sql_exec(sqlInsert)
            self.close()

        elif key == 2:
            routineID = int(raw_input('루틴번호: '))
            workoutID = int(raw_input('운동번호: (입력 중단은 0)'))
            while workoutID:
                workoutID = int(raw_input('운동번호: (입력 중단은 0)'))
                sqlInsert = '''INSERT INTO mappingR2W(routineid, workoutid) VALUES('{}', '{}')'''.format(routineID, workoutID)
                self.sql_exec(sqlInsert)
            self.close()

    

    # 루틴에 따른 운동정보 출력 함수
    def printWorkoutInfo(self):
        self = sqlite_lib()
        self.open("database.db")

        sql = '''SELECT routine.name, workout.name, workout.aim_set, workout.aim_num
            FROM mappingR2W
            INNER JOIN routine ON mappingR2W.routineid = routine.id
            INNER JOIN workout ON mappingR2W.workoutid = workout.id
            '''

        self.sql_exec(sql)
        rows = self.cur.fetchall()

        for row in rows:
            print(row)

        self.close()

    # 운동정보 출력 함수
    def printwork(self):
        self = sqlite_lib()
        self.open("database.db")

        sql = '''SELECT * FROM workout'''

        self.sql_exec(sql)
        rows = self.cur.fetchall()

        for row in rows:
            print(row[1], row[2], row[3])
        self.close()

    # 테이블 삭제 함수
    def deleteDB(self):
        self = sqlite_lib()
        self.open("workout.db")
        
        key = int(raw_input('0-[삭제취소] 1-[운동루틴 삭제] 2-[운동종류 삭제] 3-[단기피드백 삭제] 4-[장기피드백 삭제] 5-[초기화]'))

        if key == 0:
            print("Return to menu")
        elif key == 1:
            option = int(raw_input('삭제할 루틴 번호: '))
            sql1 = '''DELETE FROM mappingR2W WHERE routineid = ('{}')'''.format(option)
            sql2 = '''DELETE FROM routine WHERE id = ('{}')'''.format(option)
            self.sql_exec(sql1)
            self.sql_exec(sql2)
            self.close()
        elif key == 2:
            option = int(raw_input('삭제할 루틴 번호: '))
            sql = '''DELETE FROM workout WHERE id = ('{}')'''.format(option)
            self.sql_exec(sql)
            self.close()
        elif key == 3:
            option = raw_input('삭제할 단기피드백 번호: ')
            sql = '''DELETE FROM livedata WHERE name = ('{}')'''.format(option)
            self.sql_exec(sql)
            self.close()
        elif key == 4:
            option = raw_input('삭제할 장기피드백 번호: ')
            sql = '''DELETE FROM daywork WHERE name = ('{}')'''.format(option)
            self.sql_exec(sql)
            self.close()
        elif key == 5:
            option = raw_input('정말 초기화를 진행하려면 0입력 취소는 아무숫자 입력: ')
            if option == 0:
                sql1 = '''DELETE FROM mappingR2w'''
                sql2 = '''DELETE FROM routine'''
                sql3 = '''DELETE FROM workout'''
                sql4 = '''DELETE FROM livedata'''
                sql5 = '''DELETE FROM daywork'''
                self.sql_exec(sql1)
                self.sql_exec(sql2)
                self.sql_exec(sql3)
                self.sql_exec(sql4)
                self.sql_exec(sql5)
                self.close()
            else:
                self.close()


if __name__ == '__main__':
    dbsql = db()
    while True:
        num = int(raw_input('메뉴: 테이블 생성 [0], 데이터 삽입 [1], 데이터 출력 [2], 데이터 삭제 [3]'))
        if num == 0:
            dbsql.createSensorTable()
            dbsql.createWorkoutData()
        elif num == 1:
            dbsql.insertWorkoutData()
        elif num == 2:
            dbsql.printwork()
            dbsql.printWorkoutInfo()
    

