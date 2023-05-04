message = input("Please enter the message that you want to convey : ")
shifting = int(input("Please enter the number of alphabets that you want to be shifted : "))

operation = input("Please enter the operation that you want to perform (encrypt/decrypt) : ")

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

message_list = list(message) 
new_word = []
def encrypt():
    for i in range(0,len(message)):
        new_alphabet = alphabets[i+shifting]
        new_word.append(new_alphabet)
    new_string = " ".join(new_word)
    print("Your encrypted string is : " + new_string.replace(" ",""))
#encrypt()

length = len(message)

def decrypt():
    for i in reversed(range(length)):
        alphabet = alphabets[i]
        # print(alphabet)
        new_word.append(alphabet)
    new_string = " ".join(new_word)
    string_replace = new_string.replace(" ","")[::-1]
    print("Your decrypted string is : " + string_replace)
#decrypt()


if(operation == "encrypt"):
    encrypt()
else:
    if(operation == "decrypt"):
        decrypt()
    else:
        print("Please enter a valid operation.")

