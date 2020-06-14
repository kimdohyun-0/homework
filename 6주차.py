//성적처리부분.
print("1.데이터 추가\n2.데이터 검색\n3.데이터 삭제\n4.데이터 정렬\n0.종료")
list1 = []
mylist2 = []
class funtion:
    def insert(self):
        global list1
        for k in range(0, 5):
            list1.append(input("학과:"))
            list1.append(input("학번:"))
            list1.append(input("이름:"))
            list1.append(input("국어:"))
            list1.append(input("영어:"))
            list1.append(input("수학:"))
            list1.append(input("총점:"))
            list1.append(input("평균:"))
            list1.append(input("학점:"))
            mylist2.append(list1)
            list1 = []
    def search(self):
        global mylist2
        string = ""
        num = 0
        num = input("학번입력:")
        string = input("이름입력:")
        for j in range(0, 5):
            for k in range(0, 6):
                if mylist2[j][k] == num:
                    print(mylist2[j])

    def delete(self):
        global mylist2
        string = ""
        num = 0
        num = input("학번입력:")
        string = input("이름입력:")
        for j in range(0, 5):
            for k in range(0, 6):
                if mylist2[j][k] == num:
                    for i in range(0, 6):
                        mylist2[j][i] = 0

    def sort(self):
        global mylist2
        global list3
        list3 = []
        list3 = sorted(mylist2)
        print(list3)
while (True):
    a = int(input("메뉴를 선택하세요:"))
    b=funtion()
    if a == 0:
        break
    if a == 1:
        b.insert();
    if a == 2:
        b.search();
    if a == 3:
        b.delete();
    if a==4:
        b.sort();
//수업내용중 threading 문제 부분.
import threading
import time
class sum:
    num=1
    suma=0
    def __init__(self,a):
        self.num=a
    def sum(self):
        suma=0
        for i in range(1,self.num+1):
            suma+=i
        print("1+2+3+....+%d=%d" % (self.num,suma))
sum1=sum(1000)
sum2=sum(100000)
sum3=sum(10000000)
th1=threading.Thread(target=sum1.sum)
th2=threading.Thread(target=sum2.sum)
th3=threading.Thread(target=sum3.sum)
th1.start()
th2.start()
th3.start()
