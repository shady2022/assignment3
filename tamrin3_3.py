a=[]

for i in range(len(a)):
    sh=int(input("please enter your number:"))
    if a[i]<a[i+1]:
        a.append(sh)
        print("thats right!")
        
    else:
       print("nooo..!!!")
       exit()
        