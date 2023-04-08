# ELLA MARIE A. MALLARI
# BSCPE 1-4

# PROBLEM 2 - DECRYPTION

# input encrypted text
print("\033[0;32m=" * 80)
encrypted_text = input("\033[0;32mTYPE ENCRYPTED TEXT: ")
decrypted_text = ""
# check every symbol to substitute
for i in range(len(encrypted_text)):
    # if *, make it a
    if encrypted_text [i] == "*":
        decrypted_text += "a"
    # if &, make it e
    elif encrypted_text [i] == "&":
        decrypted_text += "e"
      # if &, make it e
    elif encrypted_text [i] == "#":
        decrypted_text += "i"
      # if &, make it e
    elif encrypted_text [i] == "+":
        decrypted_text += "o"
      # if &, make it e
    elif encrypted_text [i] == "!":
        decrypted_text += "u"
    else:
        decrypted_text += encrypted_text[i]
# print decrypted text 
print("\033[0;31m=" * 80)
print("\033[0;31mDECRYPTED TEXT: " + decrypted_text)

# i follow the steps on the first problem and apply some learnings in our discussion like code for colors :>