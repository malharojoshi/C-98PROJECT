def swapFiles():
    fileName1=input("Enter The File Name 1: ")
    fileName2=input("Enter The File Name 2: ")
    with open(fileName1,'r') as a:
        data_a = a.read()
        a.close()
    with open(fileName2,'r') as b:
        data_b = b.read()
        b.close()
    with open(fileName1,'w') as a:
        a.write(data_b)
        a.close()
    with open(fileName2,'w') as b:
        b.write(data_a)
        b.close()
swapFiles()