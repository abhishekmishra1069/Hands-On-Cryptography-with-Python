alpha =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

str_in = input("Enter message, like HELLO: ")
#shift = int(raw_input("Shift value, like 3: "))

n = len(str_in)

for shift in range(26):
   str_out = ""
   for i in range(n):
      c = str_in[i]
      loc = alpha.find(c)
      newloc = (loc - shift)%26
      str_out += alpha[newloc]
   print (shift, str_out)

#print "Obfuscated version:", str_out

