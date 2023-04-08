# ELLA MARIE A. MALLARI 
# BSCPE 1-4

# PROBLEM 3 - THE VIGENÉRE CIPHER

# first we need to define so that we can generate the key
def generateKeyword(textMessage, key):
    key = list(key)
    if len(textMessage) == len(key):
        return key
    else:
        for i in range(len(textMessage) - len(key)):
            key.append(key[i % len(key)])
        return("".join(key))
# we will define the cipher text to generate it and will add modulo 26 to complete the alphabet
def cipherText(textMessage, key):
    cipher_text = []
    for i in range(len(textMessage)):
        x = (ord(textMessage[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x)) 
    return("" .join(cipher_text))

if __name__ == "__main__":
# ask the user to type any message, keyword in all capital letters with no spaces
    print("=" * 80) # i added this so that i can separate it and be noticeable
    print("Kindly type any message in capital letters and no spaces: ")
    textMessage = input() 
    print("=" * 80) # i added this so that i can separate it and be noticeable
    print("Kindly type your chosen keyword also in capital letters: ")
    keyword = input() 
# i want to change colors to make it noticeable
    cyan = '\033[36m' # added this code to add color
    reset = '\033[0m'
    key = generateKeyword(textMessage, keyword) 
    cipher_text = cipherText(textMessage, key)
    print("=" * 80) # i added this so that i can separate it and be noticeable
    print(cyan + "CIPHERTEXT: " + reset + cipher_text)

# reference from geekforgeeks
# i alse added some codes for colors and characters :> 
