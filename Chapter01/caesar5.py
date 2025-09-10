import sys
#alpha =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"



def encode(shift, str_in):
  n = len(str_in)
  str_out = ""

  for i in range(n):
    c = str_in[i]
    loc = alpha.find(c)
    newloc = (loc + shift)%52
    str_out += alpha[newloc]
    print("i=", i, "c=", c, "loc=", loc, "newloc=", newloc,   "char=", alpha[newloc]  )

  return str_out

def decode(shift, str_in):
  return encode(-shift, str_in)

if __name__ == "__main__": 
  str_in = input("Enter ciphertext: ")
  shift = int(input("Shift value, like 3: "))
  str_out = encode(shift, str_in)
  print ("Obfuscated version:", str_out)
  str_back = decode(shift, str_out)
  print ("De-obfuscated version:", str_back)

