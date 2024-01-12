import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox

from crt import Crt, CrtException, EasyFS
from mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.actionE_xit.triggered.connect(self.file_exit)
        self.actionOpen_crt.triggered.connect(self.file_open)
        self.model = EasyFS(self)

    def file_exit(self) -> None:
        self.close()

    def file_open(self) -> None:
        file = QFileDialog.getOpenFileName(self, "Open CRT file", filter="Cart files (*.crt);;All files (*.*)")
        if file[0] == '':
            return
        with open(file[0], 'rb') as f:
            try:
                crt = Crt.from_bytes(f.read())
                raw = crt.get_raw().lstrip(b'\xff')
                self.model.from_bytes(raw)
            except CrtException as ex:
                QMessageBox.critical(self, "Open CRT file", str(ex))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
