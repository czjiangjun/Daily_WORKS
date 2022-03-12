import easygui as a
# msgbox(msg=' ', title=' ', ok_button=' ', image=None, root=None) # 消息弹窗
a.msgbox(msg='Today', title=' TEST ', ok_button=' Continue ', image=None, root=None)

# ccbox(msg=' ', title=' ', choices=('  ', '  '), image=None)  # 双项选择
a.ccbox(msg=' Today', title=' TEST ', choices=(' OK  ', ' Cancel '), image='/home/jun_jiang/Documents/Latex_art_beamer/Presentation_Beamer/Figures/seal_Jiang-2.jpg')  # 双项选择

# buttonbox(msg=' ', title=' ', choices=('Button1', 'Button2', 'Button3'), image=None, root=None) # 多项选择
a.buttonbox(msg=' Today', title=' TEST', choices=('Button1', 'Button2', 'Button3'), image=None)

# choicebox(msg=' ', title=' ', choices=()) # 可下拉菜单
ret = a.choicebox(msg=' Question:', title=' TEST', choices=['choice1','choice2', 'choice3'])
print(ret)
#multchoicebox() 提供多选
ret = a.multchoicebox(msg = 'Question:', title=' TEST', choices=['choice1','choice2', 'choice3', 'choice4'])
print(ret)

# enterbox(msg='  ', title=' ', default=' ', strip=True, image=None, root=None) 文本输入诓
ret = a.enterbox(msg=' Question ', title=' Dialog_box ', default=' TEST ', strip=True, image=None)
print(ret)

# integerbox(msg='', title=' ', default='', lowerbound=0, upperbound=99, image=None, root=None, **invalidKeywordArguments) # 只能输入界定范围内的整型数
ret = a.integerbox(msg=' Question ', title=' Dialog_box', default=666, lowerbound=0, upperbound=999, image=None)
print(ret)

Msg = '上网不涉密，涉密不上网'
Title = '校园网充值中心'
Fields = ['姓名', '学号', '充值面额']
# multenterbox(msg=' ', title=' ', fields=(), values=()) 其中values是输入的默认值、feilds是需要填写的条目名称，均用列表填写； 返回值是所有填写的值构成的列表；
ret = a.multenterbox(msg = Msg, title = Title, fields= Fields, values= ['0', '0', '0'])
print(ret)

# passwordbox(msg=' ', title=' ', default=' ', image=None, root=None) # 密码输入框(不显示)
ret = a.passwordbox(msg=' 输入密码 ', title=' 密码登录 ', default=' ', image=None, root=None)
print(ret)

User_and_Pass = ['用户名', '账号', '密码']
# multpasswordbox() # 与上面类似，不过其只有最后一个框是匿名的，即密码输入
ret = a.multpasswordbox(msg = Msg, title = Title, fields = User_and_Pass, values = ['', '', ''])
print(ret)

def main():
    exit()

if __name__=='__main__':
    main()
