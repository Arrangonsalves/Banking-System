x=int(input("Press\n1.Insert a/c details\n2.update a/c details\n3.Balance inquiry\n4.Cash withdraw\n5.Cash deposit\n6.Delete account\n"))
d={'barry_18_1234554321':['barry',18,1234554321,50000]}
def ins():
    global d
    a=input('Enter your name ')
    b=input('Enter your age ')
    c=input('Enter your mobile no. ')
    if(len(c)<10 or len(c)>10):
      print('Please enter 10 digit no.')
      c=input('Enter 10 digit mobile no.')
    u=a+'_'+b+'_'+c
    e=int(input('Deposit a minimum of 500 rupees or more '))
    if(e<500):
        print('Deposit a minimum of 500 rupees')
    else:
        d[u]=[a,b,c,e]
        print(d)
        print('Your user ID is ',u)    
def upd():
    global d
    a=input('Enter your user ID ')
    if a in d.keys():
        print('Your account details are')
        print(d[a])
        y=int(input('Press\n1 to change name\n2 to update age\n3 to update mobile no.\n'))
        if(y==1):
           p=input('Enter new username ')
           d[a][0]=p
           print('your name is updated as ',p)
        elif(y==2):
           p=input('Enter your new age ')
           d[a][1]=p
           print('Your age is updated as',p)
        elif(y==3):
           p=input('Enter new mobile number ')
           d[a][2]=p
    else:
        print('No user found ')
        w=input('Do you want to enter again(y/n)')
        if(w=='y' or w=='Y'):
            upd()
        else:
            pass
def bal():
    global d
    a=input('Enter your user ID ')
    if a in d.keys():
        print('Your account details are')
        print(d[a])
        print('your balance is',d[a][3])
    else:
        print('No username found')
def dep():
    global d
    a=input('Enter your user ID ')
    if a in d.keys():
        print('Your balance is ',d[a][3])
        x=int(input('Enter the amount you want to deposit '))
        y=d[a][3]+x
        print('Your updated balance is ',y)
    else:
        print('No username found')
def wit():
    global d
    a=input('Enter your user ID ')
    if a in d.keys():
        print('Your balance is ',d[a][3])
        x=int(input('Enter amount you want to withdraw '))
        y=d[a][3]-x
        print('Your updated balance is ',y)
def dele():
    global d
    a=input('Enter your user ID ')
    if a in d.keys():
        p=('Are you sure you want to delete this account(y/n)')
        if(p=='y'or'Y'):
            del(d[a])
            print('Your account is deleted successfully')
        else:
            pass    
if(x==1):
    ins()
elif(x==2):
    upd()
elif(x==3):
    bal()
elif(x==4):
    dep()
elif(x==5):
    wit()
elif(x==6):
    dele()
