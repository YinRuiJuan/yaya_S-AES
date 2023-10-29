from tkinter import *
from tkinter.messagebox import *
import S_AES_16bits
# 设置主界面的容器大小和位置
root = Tk()
root.title('S-AES')
root.geometry("1000x500+100+150")
root.configure(bg="gray")
# 声明组件变量
key=StringVar()
input = StringVar()
output = StringVar()
text_1=StringVar()
text_1.set("结果:")
# 组件的使用
def btn_encropt():
    a=input.get()
    b=key.get()
    c= S_AES_16bits.encropt(a, b)
    text_1.set("加密结果:")
    output.set(c)
def btn_decropt():
    a=input.get()
    b=key.get()
    c= S_AES_16bits.decropt(a, b)
    text_1.set("解密结果:")
    output.set(c)
def btn_ascii_encropt():
    a = input.get()
    b = key.get()
    output1 = S_AES_16bits.convert_to_8bit(a)
    C=S_AES_16bits.fenzu(output1)
    ans=""
    for i in range(len(C)):
        ans+=S_AES_16bits.encropt(C[i],b)
    D=S_AES_16bits.fenzu(ans)
    result=S_AES_16bits.bit_to_convert(D)
    text_1.set("ASCII加密结果:")
    output.set(result)
def btn_ascii_decropt():
    a = input.get()
    b = key.get()
    output1 = S_AES_16bits.convert_to_8bit(a)
    C=S_AES_16bits.fenzu(output1)
    ans=""
    for i in range(len(C)):
        ans+=S_AES_16bits.decropt(C[i],b)
    D=S_AES_16bits.fenzu(ans)
    result=S_AES_16bits.bit_to_convert(D)
    text_1.set("ASCII解密结果:")
    output.set(result)
def btn_two_encropt():
    a = input.get()
    b = key.get()
    c = S_AES_16bits.two_encropt(a, b)
    text_1.set("二重加密结果:")
    output.set(c)
def btn_two_decropt():
    a = input.get()
    b = key.get()
    c = S_AES_16bits.two_decropt(a, b)
    text_1.set("二重解密结果:")
    output.set(c)
def btn_three_encropt():
    a = input.get()
    b = key.get()
    c = S_AES_16bits.three_encropt(a, b)
    text_1.set("三重加密结果:")
    output.set(c)
def btn_three_decropt():
    a = input.get()
    b = key.get()
    c = S_AES_16bits.three_decropt(a, b)
    text_1.set("三重解密结果:")
    output.set(c)

# 组件的使用
Label(root, text='密钥:', font=('幼圆', 20),background="gray").place(x=50, y=30)
Entry(width=50, font=('幼圆', 20), textvariable=key).place(x=250, y=30)
Label(root, text='输入:', font=('幼圆', 20),background="gray").place(x=50, y=110)
Entry(width=50, font=('幼圆', 20), textvariable=input).place(x=250, y=110)
Label(root, textvariable=text_1, font=('幼圆', 20),background="gray").place(x=50, y=180)
Entry(width=50, font=('幼圆', 20), textvariable=output).place(x=250, y=180)

Button(text='二进制加密',
       background='darkgray',  # 背景色
       foreground='black', # 前景色
       width=10,
       font=('幼圆', 20),  # 字体  大小
       command=btn_encropt).place(x=130, y=250)
Button(text='二进制解密',
       background='darkgray',  # 背景色
       foreground='black', # 前景色
       width=10,
       font=('幼圆', 20),  # 字体  大小
       command=btn_decropt).place(x=330, y=250)
Button(text='ASCII加密',
       background='darkgray',  # 背景色
       foreground='black', # 前景色
       width=10,
       font=('幼圆', 20),  # 字体  大小
       command=btn_ascii_encropt).place(x=530, y=250)
Button(text='ASCII解密',
       background='darkgray',  # 背景色
       foreground='black', # 前景色
       width=10,
       font=('幼圆', 20),  # 字体  大小
       command=btn_ascii_decropt).place(x=730, y=250)
Button(text='双重加密',
       background='darkgray',  # 背景色
       foreground='black', # 前景色
       width=10,
       font=('幼圆', 20),  # 字体  大小
       command=btn_two_encropt).place(x=130, y=350)
Button(text='双重解密',
       background='darkgray',  # 背景色
       foreground='black', # 前景色
       width=10,
       font=('幼圆', 20),  # 字体  大小
       command=btn_two_decropt).place(x=330, y=350)
Button(text='三重加密',
       background='darkgray',  # 背景色
       foreground='black', # 前景色
       width=10,
       font=('幼圆', 20),  # 字体  大小
       command=btn_three_encropt).place(x=530, y=350)
Button(text='三重解密',
       background='darkgray',  # 背景色
       foreground='black', # 前景色
       width=10,
       font=('幼圆', 20),  # 字体  大小
       command=btn_three_decropt).place(x=730, y=350)
Button(text='退出',
       background='darkgray',  # 背景色
       foreground='black',  # 前景色
       width=10,
       font=('幼圆', 15),  # 字体  大小
       command=lambda: root.quit()).place(x=450, y=450)


# 显示图形界面
root.mainloop()