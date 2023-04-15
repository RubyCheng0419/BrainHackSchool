
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
        # change key length
        key = generatekey(letter, key)
        lst = []
        lst2= []
        # separate each character of the word
        for char in letter:
            lst.append(char)  
        for char in key:
            lst2.append(char)
        ans = encrypt_letter(letter, key)
        return ans
    else:
        # change key length
        key = generatekey(letter, key)
        lst = []
        lst2= []
        # separate each character of the word
        for char in letter:
            lst.append(char)  
        for char in key:
            lst2.append(char)
        ans = decrypt_letter(letter, key)
        return ans
    

if __name__ == "__main__":
    letter = input("your message: ")
    key = input("your key: ")
    encrypt=input()
    ans = process_message(letter,key,encrypt)
    print (ans)   

    # x = input("Please enter your message: ")
    # y = input("Please enter your key: ")
    # Z = input("True or False: ")
    # x= process_message(a,b,c)
    # print(x)