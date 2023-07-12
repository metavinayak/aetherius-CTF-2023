from sympy import *
from sympy.abc import x
import random

flag_string="***REDACTED***"
# Original flag_string consists of only lowercase english alphabets

l=len(flag_string)
# Given: l%3 == 0

def to_matrix(str):
    ar=[]
    for i in range(3):
        ar.append(ord(str[i])-ord('a'))
    return Matrix(Array(ar,(3,1)))

def to_text(mat):
    return "".join(str(chr(mat[i]+ord('a'))) for i in range(3))

i=0
flag_enc=''
helper_enc=''
while(i!=(l//3)):
    ar=[]
    for j in range(3*3):
        ar.append(random.randint(0,26))

    mat = Matrix(Array(ar,(3,3)))
    try:
        inv=mat.inv_mod(26) 
        # ensuring inverse exists so decryption is possible :)
    except:
        pass
    else:
        ar[i]=x
        with open("matrix.txt", "a") as file:
            file.write(str(ar)+'\n')

        original_part=to_matrix(flag_string[3*i:3*i+3])
        helper_part=to_matrix('ctf')
        
        enc=(mat*original_part)%26
        helpr=(mat*helper_part)%26

        flag_enc+=to_text(enc)
        helper_enc+=to_text(helpr)
    
        i+=1

def decrypt():
    '''
    1) parse given data from .txt files
    2) do some crypto stuff
    3) reconstruct the original flag string and submit
    '''

with open("enc_flag.txt", "w") as file:
    file.write(flag_enc+'\n')
    file.write(helper_enc+'\n')