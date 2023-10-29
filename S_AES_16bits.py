s_0=[["1001","0100","1010","1011"],
     ["1101","0001","1000","0101"],
     ["0110","0010","0000","0011"],
     ["1100","1110","1111","0111"]]
s_1=[["1010","0101","1001","1011"],
     ["0001","0111","1000","1111"],
     ["0110","0000","0010","0011"],
     ["1100","0100","1101","1110"]]

def two_to_ten(binary):
    decimal=0
    binary_list = [int(x) for x in str(binary)[::-1]]
    for i in range(len(binary_list)):
        decimal += binary_list[i] * 2**i
    return decimal

def change_LandR(w):
    w_left=w[0:4]
    w_right=w[4:8]
    #print(w_left)
    #print(w_right)
    temp=w_left
    w_left=w_right
    w_right=temp
    ans=w_left+w_right
    return ans

def xor(a,b):
    c=""
    for i in range(len(a)):
        temp1=int(a[i])
        temp2=int(b[i])
        c+=str(temp1^temp2)
    return c
#print(xor("10001000","00100101"))

#s:s盒  w:8bit
def S_change(s,w):
    w_1=w[0:2]
    w_2=w[2:4]
    w_3=w[4:6]
    w_4=w[6:8]
    #print("w_1:",w_1,"w_2:",w_2,"w_3:",w_3,"w_4:",w_4)
    w1=two_to_ten(w_1)
    w2=two_to_ten(w_2)
    w3=two_to_ten(w_3)
    w4=two_to_ten(w_4)
    #print("w1:",w1,"w2:",w2,"w3:",w3,"w3:",w4)
    w_s=s[w1][w2]+s[w3][w4]
    #print("s[w1][w2]:",s[w1][w2],"s[w3][w4]:",s[w3][w4])
    return w_s

def g1(w1):
    R1="10000000"
    w1_1=change_LandR(w1)
    #print("w1交换：",w1_1)
    #把交换后的进入S盒交换
    w1_1_s=S_change(s_0,w1_1)
    #print("w1交换后经过S盒：",w1_1_s)
    #与轮常数进行异或
    w1_1_s_r=xor(w1_1_s,R1)
    #print("轮常数：",w1_1_s_r)
    return w1_1_s_r
def g2(w1):
    R2="00110000"
    w1_1=change_LandR(w1)
    #print("w1交换：",w1_1)
    #把交换后的进入S盒交换
    w1_1_s=S_change(s_0,w1_1)
    #print("w1交换后经过S盒：",w1_1_s)
    #与轮常数进行异或
    w1_1_s_r=xor(w1_1_s,R2)
    #print("轮常数：",w1_1_s_r)
    return w1_1_s_r


def lunCrpto(w):
     w0 = w[0:8]
     w1 = w[8:16]
     # print("w0:",w0)
     # print("w1:",w1)

     w1_g = g1(w1)
     w2 = xor(w0, w1_g)
     # print("w2:",w2)

     w3 = xor(w2, w1)
     # print("w3:",w3)

     w3_g = g2(w3)
     w4 = xor(w2, w3_g)
     # print("w4:",w4)

     w5 = xor(w4, w3)
     # print("w5:",w5)

     key0 = w0 + w1
     key1 = w2 + w3
     key2 = w4 + w5
     # print(key0,key1,key2)
     return key1, key2

def ban_change(s,ming):
    ming0=ming[0:4]
    ming1=ming[4:8]
    ming2=ming[8:12]
    ming3=ming[12:16]
    #print("ming0:",ming0,"ming1:",ming1,"ming2:",ming2,"ming3:",ming3)
    ming0_1=(S_change(s,ming0+ming1))[0:4]
    ming1_1=(S_change(s,ming0+ming1))[4:8]
    ming2_1=(S_change(s,ming2+ming3))[0:4]
    ming3_1=(S_change(s,ming2+ming3))[4:8]
    #print("ming0_1:",ming0_1,"ming1_1:",ming1_1,"ming2_1:",ming2_1,"ming3_1:",ming3_1)
    ming_new=ming0_1+ming1_1+ming2_1+ming3_1
    #print("new:",ming_new)
    return ming_new
def hang_change(ming):
    #提取出半字节
    ming0=ming[0:4]
    ming1=ming[4:8]
    ming2=ming[8:12]
    ming3=ming[12:16]
    #print(ming0,ming1,ming2,ming3)
    #交换
    temp=ming1
    ming1=ming3
    ming3=temp
    #组合
    ming_new=ming0+ming1+ming2+ming3
    return ming_new
#print(hang_change("0110000001001100"))

def lie_change(ming):
     a1 = int(ming[0]) ^ int(ming[6])
     a2 = int(ming[1]) ^ int(ming[4]) ^ int(ming[7])
     a3 = int(ming[2]) ^ int(ming[4]) ^ int(ming[5])
     a4 = int(ming[3]) ^ int(ming[5])
     s00 = str(a1) + str(a2) + str(a3) + str(a4)
     # print("s00:",s00)

     b1 = int(ming[2]) ^ int(ming[4])
     b2 = int(ming[0]) ^ int(ming[3]) ^ int(ming[5])
     b3 = int(ming[0]) ^ int(ming[1]) ^ int(ming[6])
     b4 = int(ming[1]) ^ int(ming[7])
     s10 = str(b1) + str(b2) + str(b3) + str(b4)
     # print("s10:",s10)

     c1 = int(ming[8]) ^ int(ming[14])
     c2 = int(ming[9]) ^ int(ming[12]) ^ int(ming[15])
     c3 = int(ming[10]) ^ int(ming[12]) ^ int(ming[13])
     c4 = int(ming[11]) ^ int(ming[13])
     s01 = str(c1) + str(c2) + str(c3) + str(c4)
     # print("s01:",s01)

     d1 = int(ming[10]) ^ int(ming[12])
     d2 = int(ming[8]) ^ int(ming[11]) ^ int(ming[13])
     d3 = int(ming[8]) ^ int(ming[9]) ^ int(ming[14])
     d4 = int(ming[9]) ^ int(ming[15])
     s11 = str(d1) + str(d2) + str(d3) + str(d4)
     # print("s11:",s11)

     ming_new = s00 + s10 + s01 + s11

     return ming_new


def ni_lie_change(mi):  # 列混淆中的矩阵乘法
     mi_0 = mi[0:4]
     mi_1 = mi[4:8]
     mi_2 = mi[8:12]
     mi_3 = mi[12:16]
     s00 = xor(MultiProcess(9, mi_0), MultiProcess(2, mi_1))
     s01 = xor(MultiProcess(9, mi_2), MultiProcess(2, mi_3))
     s10 = xor(MultiProcess(2, mi_0), MultiProcess(9, mi_1))
     s11 = xor(MultiProcess(2, mi_2), MultiProcess(9, mi_3))
     # print(s00,s01,s10,s11)
     mi_new = s00 + s10 + s01 + s11
     return mi_new


def MultiProcess(a, b):  # 列混淆中的乘法运算的具体过程
     if a == 1:
          return b
     elif a == 2:
          if b[0] == '0':
               b = b[1:] + '0'
          else:
               b = b[1:] + '0'
               b = xor(b, '0011')
          return b
     elif a == 9:
          tmp_b = b
          return xor(tmp_b, MultiProcess(2, MultiProcess(2, MultiProcess(2, b))))


def encropt(Ming, KEY):
     # 生成轮密钥
     key1, key2 = lunCrpto(KEY)
     # print(key1,key2)
     # 第0轮
     # 轮密钥加
     Ming_0 = xor(Ming, KEY)
     # print("经过第0轮的明文",Ming_0)

     # 第1轮
     # 半字节代替
     Ming_1 = ban_change(s_0, Ming_0)
     # print("yi",Ming_1)
     # 行位移
     Ming_2 = hang_change(Ming_1)
     # print("er",Ming_2)
     # 列混淆
     Ming_3 = lie_change(Ming_2)
     # print("san",Ming_3)
     # 轮密钥加
     Ming_4 = xor(Ming_3, key1)
     # print("si",Ming_4)

     # 第2轮
     # 半字节代替
     Ming_5 = ban_change(s_0, Ming_4)
     # print("wu",Ming_5)
     # 行位移
     Ming_6 = hang_change(Ming_5)
     # print("liu",Ming_6)
     # 轮密钥加
     Ming_7 = xor(Ming_6, key2)

     Mi = Ming_7
     return Mi


def decropt(Mi, KEY):
     key1, key2 = lunCrpto(KEY)
     # print(key1,key2)
     # 第0轮
     # 轮密钥加
     Mi_0 = xor(Mi, key2)
     # print("经过第0轮的密文",Mi_0)

     # 第1轮
     # 逆行位移
     Mi_1 = hang_change(Mi_0)
     # print("yi",Mi_1)
     # 逆半字节代替
     Mi_2 = ban_change(s_1, Mi_1)
     # print("er",Mi_2)
     # 轮密钥加
     Mi_3 = xor(Mi_2, key1)
     # print("san",Mi_3)
     # 逆列混淆
     Mi_4 = ni_lie_change(Mi_3)
     # print("si",Mi_4)

     # 第二轮
     # 逆行位移
     Mi_5 = hang_change(Mi_4)
     # print("wu",Mi_5)
     # 逆半字节代替
     Mi_6 = ban_change(s_1, Mi_5)
     # print("liu",Mi_6)
     # 轮密钥加
     Mi_7 = xor(Mi_6, KEY)

     Ming = Mi_7
     return Ming

def convert_to_8bit(string):
    result = ""
    for char in string:
        # 将字符转换为8位ASCII编码，并使用zfill方法填充到8位
        ascii_code = bin(ord(char))[2:].zfill(8)
        result += ascii_code
    #print(len(string)%2)
    if len(string)%2!=0:
        print("字符数量不能两两分组")
        result="00000000"+result
    return result
def fenzu(string):
    num_of_group=len(string)/16
    #print(num_of_group)
    group=[0 for i in range(int(num_of_group))]

    for i in range(int(num_of_group)):
        group[i]=string[i*16:(i+1)*16]
        print(group[i])
    return group
def bit_to_convert(fenzu):
    result = ""
    for i in fenzu:
        # 将字符转换为8位ASCII编码，并使用zfill方法填充到8位
        i_1=i[0:8]
        i_2=i[8:16]
        ascii_code_1 = chr(two_to_ten(i_1))
        ascii_code_2 = chr(two_to_ten(i_2))
        ascii_code=ascii_code_1+ascii_code_2
        result += ascii_code
    return result
def two_encropt(mingwen,key):
    key1=key[0:16]
    key2=key[16:32]
    first=encropt(mingwen,key1)
    #print("第一个加：",first)
    second=encropt(first,key2)
    #print("第二个加：",second)
    return second
def two_decropt(miwen,key):
    key1=key[0:16]
    key2=key[16:32]
    first=decropt(miwen,key2)
    #print("第一个解：",first)
    second=decropt(first,key1)
    #print("第二个解：",second)
    return second

def three_encropt(mingwen,key):
    key1=key[0:16]
    key2=key[16:32]
    key3=key[32:48]
    first=encropt(mingwen,key1)
    #print("第一个加：",first)
    second=decropt(first,key2)
    #print("第二个加：",second)
    third=encropt(second,key3)
    return third
def three_decropt(miwen,key):
    key1=key[0:16]
    key2=key[16:32]
    key3=key[32:48]
    first=decropt(miwen,key3)
    #print("第一个解：",first)
    second=encropt(first,key2)
    #print("第二个解：",second)
    third=decropt(second,key1)
    return third
#使用密钥1010 0111 0011 1011加密二进制明文0110 1111 0110 1011，
#得出二进制密文0000 0111 0011 1000。
#0000 0111 0011 1000
#密文： 0000 0111 0011 1000
#明文： 0110 1111 0110 1011

def center_attack(mingwen, miwen):
    maybe_key = []
    num = len(mingwen)
    center_value1 = []
    center_value2 = []
    for i in range(2**16):
        key = bin(i)[2:].zfill(16)
        str1=""
        str2=""
        for j in range(num):
            temp=encropt(mingwen[j],key)
            str1+=temp
        center_value1.append(str1)
        for k in range(num):
            temp=decropt(miwen[k],key)
            str2+=temp
        center_value2.append(str2)
    for k in range(2 ** 16):
        for h in range(2 ** 16):
            if center_value1[k] == center_value2[h]:
                #print("same:", center_value1[k], center_value2[h])
                maybe_key.append((k, h))
    for m in maybe_key:
        key1=bin(m[0])[2:].zfill(16)
        key2 = bin(m[1])[2:].zfill(16)
        key_real=str(key1)+str(key2)
    print(key_real)
    return key_real

"""
keyword="11110000111100001111000011110000"
mingwen=["0110111101101011","1000101110000010","1101100000101000"]
miwen=["1000101110000010","1101100000101000","0110111101111011"]
center_attack(mingwen, miwen)"""