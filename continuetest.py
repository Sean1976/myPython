for i in range(10):
    print("i in for is:",i)
    if i%2!=0:
        print("i%2 is:",i%2)
        continue
    i+=2
    print(i)