#!/usr/bin/python3 env
# encoding=utf-8
import secrets
import string
import random
from tkinter import *
from tkinter import messagebox

'''
    String模块中的常量：
    string.digits：数字0~9
    string.ascii_letters：所有字母（大小写）
    string.lowercase：所有小写字母
    string.printable：可打印字符的字符串
    string.punctuation：所有标点,即特殊字符
    string.uppercase：所有大写字母
'''


# 生成
def init_pass(pass_length=24, special_character_length=2):
    # generate for a many character password
    password = ''.join(secrets.choice(string.ascii_letters + string.digits)
                       for i in range(pass_length-special_character_length))
    password += ''.join(secrets.choice(string.punctuation)
                        for i in range(special_character_length))
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    info_output.config(state='normal')
    info_output.delete("1.0", 'end')
    info_output.insert('end', '{}'.format(len(password)))
    info_output.config(state='disabled')

    miyue_output.config(state='normal')
    miyue_output.delete("1.0", 'end')
    miyue_output.insert('end', '{}'.format(password))
    miyue_output.config(state='disabled')

    messagebox.showinfo(
        '系统提示：', "生成完毕")


# 复制
def copy():
    miyue = miyue_output.get('0.0', 'end-1c')
    root.clipboard_clear()
    root.clipboard_append(miyue)
    root.update()
    messagebox.showinfo('系统提示：', '{}\n复制成功'.format(miyue))


if __name__ == "__main__":
    root = Tk()
    root.title("python生成随机设定位数的密码")
    root.resizable(width=False, height=False)
    # line 1
    Label(root, text="密钥整体长度：").grid(
        row=1, column=1)
    Button(root, text="生成", command=lambda: init_pass(
        vari.get(), vari_special.get())).grid(row=1, column=5, rowspan=3, padx=10)
    # line 2
    length_list = [
        '8',
        '12',
        '24',
        '32'
    ]
    vari = IntVar()
    vari.set(24)
    for each in length_list:
        Radiobutton(root, variable=vari, text=each, value=each).grid(
            row=2, column=length_list.index(each)+1)
    # line 3
    Label(root, text="特殊字符个数：").grid(
        row=3, column=1)
    # line 4
    special_character_list = [
        '2',
        '3',
        '4'
    ]
    vari_special = IntVar()
    vari_special.set(2)
    for each in special_character_list:
        Radiobutton(root, variable=vari_special, text=each, value=each).grid(
            row=4, column=special_character_list.index(each)+1)
    Button(root, text="复制", command=lambda: copy()).grid(
        row=4, column=5, rowspan=3, padx=10)
    # line 5
    Label(root, text="随机密码的长度是长度：").grid(
        row=5, column=1)
    info_output = Text(root, width=60, height=1)
    info_output.grid(
        row=5, column=2, columnspan=3)
    # line 6
    Label(root, text="密码是：").grid(
        row=6, column=1)
    miyue_output = Text(root, width=60, height=1)
    miyue_output.grid(
        row=6, column=2, columnspan=3)
    root.mainloop()
