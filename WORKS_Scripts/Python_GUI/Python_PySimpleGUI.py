import PySimpleGUI as sg

# 添加颜色
sg.theme('DarkAmber')

# layout 窗口所有的东西
layout = [ [sg.Text('Some text on Row 1')],   # 文本显示
           [sg.Text('Enter something on Row 2'), # 文本显示
               sg.InputText()],# 文本输入窗口},
               [sg.Button('Ok'), sg.Button('Cancel')]]

# 创建住窗口，传入layout
window = sg.Window('Window Title', layout)

# 事件循环
while True:
    envent, values = window.read()  # 获取文本框输入内容
    if envent == sg.WIN_CLOSED or envent == 'Cancel':
        #判断是否点击Cancel按钮
        break
    print('You entered', values[0]) # 打印输出内容

# 关闭窗口
window.close()
