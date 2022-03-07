import easygui as a
# msgbox(msg=' ', title=' ', ok_button=' ', image=None, root=None) # 消息弹窗
a.msgbox(msg='Today', title=' TEST ', ok_button=' Continue ', image=None, root=None)

# ccbox(msg=' ', title=' ', choices=('  ', '  '), image=None)  # 双项选择
a.ccbox(msg=' Today', title=' TEST ', choices=(' OK  ', ' Cancel '), image=None)  # 双项选择

# buttonbox(msg=' ', title=' ', choices=('Button1', 'Button2', 'Button3'), image=None, root=None) # 多项选择
a.buttonbox(msg=' Today', title=' TEST', choices=('Button1', 'Button2', 'Button3'), image=None)

# choicebox(msg=' ', title=' ', choices=()) # 可下拉菜单
ret = a.choicebox(msg=' Question:', title=' TEST', choices=['choice1','choice2', 'choice3'])
print(ret)
#multchoicebox() 提供多选
ret = a.multchoicebox(msg = 'Question:', title=' TEST', choices=['choice1','choice2', 'choice3', 'choice4'])
print(ret)

# enterbox(msg='  ', title=' ', default=' ', strip=True, image=None, root=None) 文本输入诓
ret = a.enterbox(msg=' Question ', title=' Dialog_box ', default=' TEST ', strip=True, image=None) # 文本输入诓
print(ret)

def main():
    exit()

if __name__=='__main__':
    main()
