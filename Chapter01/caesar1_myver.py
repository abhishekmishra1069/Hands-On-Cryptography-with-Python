import sys
alpha =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#alpha = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"


def encode_caesar(str_in):
   n = len(str_in)
   #print(f"Length of strins is {n}")
   str_out = ""

   for i in range(n):
      c = str_in[i]
      loc = alpha.find(c)
   #   print (i, c, loc) 
      newloc = loc + 3
      str_out += alpha[newloc]
   return   str_out

def decode_caesar(str_in):
   n = len(str_in)
   #print(f"Length of strins is {n}")
   str_out = ""

   for i in range(n):
      c = str_in[i]
      loc = alpha.find(c)
   #   print (i, c, loc) 
      newloc = loc - 3
      str_out += alpha[newloc]
   return   str_out

if __name__ == "__main__":
    # Prompt the user for input and handle potential empty input
    try:
        str_in = input("Enter a message to encode (e.g., HELLO): ")
        query = input("Press E for encode and D for decode: ")
    except (EOFError, KeyboardInterrupt):
        print("\nExiting.")
        sys.exit()

    if not str_in:
        print("No message entered. Exiting.")
        sys.exit()

    # Encode and print the result
    if query.upper() == 'D': 
         decoded = decode_caesar(str_in)
         print("Deobfuscated version:", decoded)
         sys.exit()
    elif query.upper() == 'E':
         encoded = encode_caesar(str_in)
         print("Obfuscated version:", encoded)



