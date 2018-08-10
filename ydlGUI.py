from ui_design import Ui_Form
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui
import sys
import main


# main window class
class MyWindow(Ui_Form, QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.new = Ui_Form()
        self.setupUi(self)
        self.tableWidget.setHorizontalHeaderLabels(['Format Code', 'Extension',
                                                  'Resolution', 'Format Note',
                                                  'File Size'])  # set H label

        self.ExtractBtn.clicked.connect(self.showinfo)
        self.DownloadBtn.clicked.connect(self.download)

        self.show()

    # function that display output at the textBrowser
    # def normalOutputWritten(self, text):
    #     cursor = self.textBrowser.textCursor()
    #     cursor.movePosition(QtGui.QTextCursor.End)
    #     cursor.insertText(text)
    #     self.textBrowser.setTextCursor(cursor)
    #     self.textBrowser.ensureCursorVisible()

    def showinfo(self):
        main.RetrieveInfo(self)
        self.tableWidget.setRowCount(main.file_count)
        main.FillInfo(self)

    def download(self):
        main.ydl.params = {'format': self.SeleEdit.text()}
        try:
            main.ydl.process_video_result(main.video)
        except Exception as e:
            pass

# youtube-dl uses logger to redirect output
# class MyLogger():
#     def debug(self, msg, w):
#         w.normalOutputWritten(w, msg)
#
#     def warning(self, msg, w):
#         w.normalOutputWritten(w, msg)
#
#     def error(self, msg, w):
#         w.normalOutputWritten(w, msg)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()     # construct and show the window
    main.proxy = myshow.PxyEdit.text()   # initiate the proxy
    sys.exit(app.exec_())