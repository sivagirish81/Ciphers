
import numpy as np

def Encryptor(plain_text,keyw):
    l=len(plain_text)
    n=l**2
    t=len(keyw)
    k=0
    key=keyw.upper()
    new_text=plain_text.upper()
    b=[[] for i in range(l)]
    a=[[] for i in range(l)]
    for i in range(l):
        for j in range(l):
            a[i].append((ord(key[k])-65)%26)
            k=(k+1)%t
    print(a)
    for i in range(l):
        b[i].append((ord(new_text[i])-65)%26)
    print(b)   
    m=np.matmul(a,b)
    enc_string=""
    print(m)
    for i in range(l):
        enc_string+=chr(65+(m[i][0])%26)
    return enc_string

def Decryptor(Encrypted_string,keyw):
    
            
plain_text=input("Enter the Text to be encrypted:")
Key_word=input("Enter the Key to be used:")
Encrypted_string=Encryptor(plain_text,Key_word)
print("Encrypted String:",Encrypted_string)


            
            
    
                
    
