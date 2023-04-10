
# make len(keys) equals len(message)
def generatekey(letter, key):
    key = list(key)
    if len(letter) == len(key):
        return(key)
    else:
        for i in range(len(letter) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

# def encrypt_letter
def encrypt_letter(lst, lst2):
    list = []
    for i in range(len(lst)):
        encrypted_index = chr((ord(lst[i]) + ord(lst2[i])) % 1114112)
        list.append(encrypted_index)
    return (''.join(str(e) for e in list))

# def decrypt_letter
def decrypt_letter(lst, lst2):
    list1 = []
    for i in range(len(lst)):
        decrypt_index = chr((ord(lst[i]) - ord(lst2[i])) % 1114112)
        list1.append(decrypt_index)
    return (''.join(str(e) for e in list1))

# def process_message
def process_message(letter, key, encrypt):
    if encrypt == "True":
        print(encrypt_letter(letter, key))
    else:
        print(decrypt_letter(letter, key))



letter = input("your message: ")
key = input("your key: ")
encrypt=input()

lst = []
lst2= []

# change key length
key = generatekey(letter, key)

# separate each character of the word
for char in letter:
    lst.append(char)  

for char in key:
    lst2.append(char)

process_message(letter,key,encrypt)




# if __name__ == "_main_":
#     x = input("Please type in your message:")
#     y = input("Please enter your key:")
#     ans=decrypt_letter(x, y)
#     print(ans)