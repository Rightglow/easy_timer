import sys

from PyQt5.QtWidgets import QApplication,QDialog
import generated.basic_widget as basic_widget

if __name__ == '__main__':

   app = QApplication(sys.argv)
   MainWindow = QDialog()
   easy_timer = basic_widget.Ui_EasyTimer()
   easy_timer.setupUi(MainWindow)
   MainWindow.show()
   sys.exit(app.exec_())