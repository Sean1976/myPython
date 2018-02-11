def printme(str):
    print(str);
    return;
def changeme(mylist):
    mylist.append([1,2,3,4])
    print("函数的内取值：",mylist)
    return
def printkey(name,age=35):
    print("name:",name)
    print("age:",age)
    return
def printLesson(name,*lessons):
    print("name:",name)
    for lesson in lessons:
        print(lesson)
    return

printme("调用我的自定义函数")
mylist=[10,20,30]
changeme(mylist)
print("函数的外取值:",mylist)
printkey(age=40,name="Sean")
printkey(name="Sean")
printLesson("Sean",("Chinese","Math","English"))