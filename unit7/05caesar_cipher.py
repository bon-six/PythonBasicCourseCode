

def get_mode():
    print('Give me a task. (e to encrypt, d to decrypt, b for brute-force)')
    while True:
        answer=input().lower()

        if answer[0] in ['e', 'd', 'b']:
            return answer[0]
        print('(e to encrypt, d to decrypt, b for brute-force)')

def get_key():
    print('Let me know your secret key to be used (1 ~ 25)')
    while True:  
        answer = input()

        if not answer.isdecimal():
            print('key must be decimal digit numbers between 1 ~ 25')
            continue

        key = int(answer)

        if key < 1 or key > 25 :
            print('key must be decimal digit numbers between 1 ~ 25')
            continue

        break
    return key

def get_message():
    print('Give me your message')
    answer = input()
    return answer

def process_message(message,key):
    output = ''
    for letter in message:
        num = ord(letter)
        if 65<=num<=90:
            num+=key
            if num>90: num-=26
            if num<65: num+=26
            output+=chr(num)
        elif 97<=num<=122:
            num+=key
            if num>122: num-=26
            if num<97: num+=26
            output+=chr(num)
        else:
            output+=letter
    return output

print('Welcome. I am Caesar Cipher program. I can help you do Caesar Cipher to your message.')
while True:
    mode = get_mode()

    if mode == 'd' or mode == 'e':
        key = get_key()

    message = get_message()

    if mode == 'b':
        print('Please check all message with different key done.')
        for key in range(1,26):
            processed_message = process_message(message,key)
            print(key, ' ', processed_message)
    elif mode == 'd':
        key = -key
        print('Please check the decrypted message.')
        processed_message = process_message(message,key)
        print(processed_message)
        key = -key
    elif mode == 'e':
        print('Please check the encrypted message.')
        processed_message = process_message(message,key)
        print(processed_message)
    else:
        pass

    print('Do you have more task to do?(y or n)')
    answer =input()
    if len(answer)>0 and answer[0] == 'y':
        continue
    else:
        break
    
    
