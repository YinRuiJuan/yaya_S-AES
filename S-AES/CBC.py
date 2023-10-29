import S_AES_16bits


def CBC_encropt(mingwen, key, IV):
    temp_Miwen = ["0" for i in range(len(mingwen))]
    for i in range(len(mingwen)):
        if i == 0:
            temp_Miwen [i] = (S_AES_16bits.encropt(S_AES_16bits.xor(mingwen[i], IV), key))
        else:
            temp_Miwen [i] = (S_AES_16bits.encropt(S_AES_16bits.xor(mingwen[i], temp_Miwen [i - 1]), key))
    return temp_Miwen
def CBC_decropt(miwen,key,IV):
    temp_decropt=[]
    temp_mingwen=[]
    ans=[]
    for i in miwen:
        temp_decropt.append(S_AES_16bits.decropt(i,key))
    for i in range(len(miwen)-1,-1,-1):
        if i !=0:
            temp_mingwen.append(S_AES_16bits.xor(temp_decropt[i],miwen[i-1]))
        if i==0:
            temp_mingwen.append(S_AES_16bits.xor(temp_decropt[i],IV))
    for i in reversed(temp_mingwen):
        ans.append(i)
    return ans


#
ming=["1000100010001000","0000111100001111","1010101010101010","0010001111010011"]
IV="0011001100110011"
key="0001000100010001"
print("CBC加密结果",CBC_encropt(ming,key,IV))
mi=['1101010000111100', '0100100101111101', '1111101000000111', '0010110011001001']
print("CBC解密结果",CBC_decropt(mi,key,IV))

print("*"*100)
print("在CBC模式下进行加密，对密文分组进行修改")
mi_change=["1101010000111100","0100100101111101","1111101000000110","0010110011001001"]
print("修改部分密文后的解密结果",CBC_decropt(mi_change,key,IV))