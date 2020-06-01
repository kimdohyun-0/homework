print("1.데이터 추가\n2.데이터 검색\n3.데이터 삭제\n4.데이터 정렬\n0.종료")
list1 = []
mylist2 = []
def insert():
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
def search():
    global mylist2
    string = ""
    num = 0
    num = input("학번입력:")
    string = input("이름입력:")
    for j in range(0, 5):
        for k in range(0, 6):
            if mylist2[j][k] == num:
                print(mylist2[j])

def delete():
    global mylist2
    string = ""
    num = 0
    num = input("학번입력:")
    string = input("이름입력:")
    for j in range(0, 5):
        for k in range(0, 6):
            if mylist2[j][k] == num:
                for i in range(0, 6):
                    mylist2[j][i] = 0;

def sort():
    global mylist2
    global list3
    list3 = []
    list3 = sorted(mylist2)
    print(list3)
while (True):
    a = int(input("메뉴를 선택하세요:"))
    if a == 0:
        break
    if a == 1:
        insert();
    if a == 2:
        search();
    if a == 3:
        delete();
    if a==4:
        sort();
