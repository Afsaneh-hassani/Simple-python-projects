import datetime
birthdate=input()
birthdate=birthdate.split('/')
nowdate=datetime.datetime.now()
nowdate=nowdate.strftime('%Y/%m/%d')
nowdate=nowdate.split('/')
daybirth=int(birthdate[2])
monthbirth=int(birthdate[1])
yearbirth=int(birthdate[0])
daynow=int(nowdate[2])
monthnow=int(nowdate[1])
yearnow=int(nowdate[0])

if monthbirth>12:
    print('WRONG')
elif daybirth>31:
    print('WRONG')
else:
    if daynow<daybirth:
        monthnow=monthnow-1
    if monthnow<monthbirth:
        yearnow=yearnow-1

    print(yearnow-yearbirth)
    
    
