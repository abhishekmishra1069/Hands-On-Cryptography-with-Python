import sys
alpha =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#alpha = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"

str_in = input("Enter message, like HELLO: ")
shift = int(input("Shift value, like 3: "))

n = len(str_in)
str_out = ""

for i in range(n):
   c = str_in[i]
   loc = alpha.find(c)
   newloc = loc + shift
   if newloc >= 26:
      newloc -= 26
   str_out += alpha[newloc]

print ("Obfuscated version:", str_out)

