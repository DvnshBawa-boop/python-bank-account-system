user=input('ENTER YOUR NAME ')
print(f'Hi! {user}')
dob=input('Enter your in the format DDMMYYYY ')
day=int(dob[0:2])
month=int(dob[2:4])
yrs=int(dob[4:8])
yrag= 2026-yrs
if yrag<=18:
    print(f'You are underage to continue you are {yrag}')
    exit()
else:
    passw= str(yrs)+str(day)
    work=input('Enter your reason of visit ')
    print(f'Your generated password is {passw}') 
    attempt=0
while attempt<3:
    pwd=int(input('Enter Numeric pin to continue '))
    if pwd==int(passw):
        print(f'WELCOME {user}, you can {work}')
        break 
    else:
        attempt+=1
        print('INCORRECT CREDENTIALS')
        if attempt==0:
            print('1/3')
        if attempt==1:
            print('1/3')
        if attempt==2:
            print('2/3')
        if attempt==3:
            print('ALL 3 attempts over!!!')
            exit()
bal=int(input('Enter balance'))
pur=input('Enter (a)for deposit, (b)for withdrawal, (c)to check balance ')
if pur=='a':
    dep = int(input("Enter amount to deposit "))
    print(f'{user} deposited INR ',dep)
    bal+=dep
    pass
if pur=='b':
    wit=int(input('Enter amount to withdraw '))
    bal=bal-wit
    if bal<0:
        print('Insufficient Balance')
    else:
        print(f'{user} withdrawed INR{wit}')
        pass
if pur=='c':
    print(f'{user} balance is {bal}')
    pass
print(f'{user} account balance is INR{bal}')