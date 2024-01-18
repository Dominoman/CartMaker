import sys

from PySide6.QtCore import QItemSelection
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox

from crt import Crt, CrtException, EasyFS, EasyFile
from mainwindow import Ui_MainWindow
from widgets import MemoryWidget


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.actionE_xit.triggered.connect(self.file_exit)
        self.actionOpen_crt.triggered.connect(self.file_open)
        self.actionExport.triggered.connect(self.file_export)
        self.actionAdd_apps.triggered.connect(self.file_add)
        self.actionDelete_apps.triggered.connect(self.file_delete)
        self.model = EasyFS(self)
        self.tableView.setModel(self.model)
        selection_model = self.tableView.selectionModel()
        selection_model.selectionChanged.connect(self.sel_changed)

        self.widget = MemoryWidget(self.centralwidget)
        self.widget.setModel(self.model)
        self.verticalLayout.addWidget(self.widget)

    def sel_changed(self, selected: QItemSelection, deselected: QItemSelection) -> None:
        self.actionExport.setEnabled(selected.count() > 0)
        self.actionDelete_apps.setEnabled(selected.count() > 0)

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

    def file_export(self) -> None:
        path = QFileDialog.getExistingDirectory(self, "Export dir")
        if path != "":
            indexes = self.tableView.selectionModel().selectedRows()
            for index in indexes:
                file = self.model.files[index.row()]
                file.export(path)
            QMessageBox.information(self, "Export", f"Exported {len(indexes)} file(s).")

    def file_add(self) -> None:
        path = QFileDialog.getOpenFileNames(self, "Add files", filter="PRG files (*.prg);;All files (*.*)")
        if len(path[0]) != 0:
            for file in path[0]:
                ef = EasyFile.load_file(file)
                self.model.add_file(ef)

    def file_delete(self) -> None:
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
