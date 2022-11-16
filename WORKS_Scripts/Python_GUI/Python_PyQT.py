import sys
from PyQt5.QtWidgets import QApplication, QWidget

def show_w():
    '显示窗口'
    app=QApplication(sys.argv)

    w=QWidget()

    w.resize(500, 500)
    w.move(500, 100)
    w.setWindowTitle('simple')
    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    show_w()
