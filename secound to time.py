h=0  
min=0
sec=int(input("enter the secound: "))
if sec<3600:
    h=00
    min=sec//60
    sec=(sec%60)
if sec>3599:
    h=sec//3600
    min=(sec%3600)//60
    sec=(sec%3600)%60
if h<10 and min<10 and sec<10:
    print("0",h ,":","0", min ,":" ,"0", sec)

elif h>9 and min>9 and sec>9: 
    print(h ,":", min ,":", sec)

elif h>9 and min<10 and sec<10: 
    print(h ,":","0", min ,":" ,"0",sec)
    
elif h<10 and min>9 and sec<10: 
    print("0",h ,":", min ,":" ,"0" ,sec)

elif h<10 and min<10 and sec>9: 
    print("0",h ,":","0", min ,":" , sec)

elif h>9 and min>9 and sec<10: 
    print(h ,":",min ,":" , sec) 

elif h<10 and min>9 and sec>9: 
    print("0",h ,":",min ,":" , sec)   

elif h>9 and min<10 and sec>9: 
    print(h ,":","0",min ,":" , sec) 
