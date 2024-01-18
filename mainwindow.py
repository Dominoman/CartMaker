# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QTableView, QToolBar, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionE_xit = QAction(MainWindow)
        self.actionE_xit.setObjectName(u"actionE_xit")
        icon = QIcon()
        icon.addFile(u":/Buttons/exit", QSize(), QIcon.Normal, QIcon.Off)
        self.actionE_xit.setIcon(icon)
        self.actionOpen_crt = QAction(MainWindow)
        self.actionOpen_crt.setObjectName(u"actionOpen_crt")
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/open", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen_crt.setIcon(icon1)
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.actionExport.setEnabled(False)
        icon2 = QIcon()
        icon2.addFile(u":/Buttons/export", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExport.setIcon(icon2)
        self.actionDelete_apps = QAction(MainWindow)
        self.actionDelete_apps.setObjectName(u"actionDelete_apps")
        self.actionDelete_apps.setEnabled(False)
        icon3 = QIcon()
        icon3.addFile(u":/Buttons/delete", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDelete_apps.setIcon(icon3)
        self.actionAdd_apps = QAction(MainWindow)
        self.actionAdd_apps.setObjectName(u"actionAdd_apps")
        icon4 = QIcon()
        icon4.addFile(u":/Buttons/add", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAdd_apps.setIcon(icon4)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menu_File.addAction(self.actionOpen_crt)
        self.menu_File.addAction(self.actionAdd_apps)
        self.menu_File.addAction(self.actionDelete_apps)
        self.menu_File.addAction(self.actionExport)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionE_xit)
        self.toolBar.addAction(self.actionOpen_crt)
        self.toolBar.addAction(self.actionExport)
        self.toolBar.addAction(self.actionAdd_apps)
        self.toolBar.addAction(self.actionDelete_apps)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionE_xit.setText(QCoreApplication.translate("MainWindow", u"E&xit", None))
        self.actionOpen_crt.setText(QCoreApplication.translate("MainWindow", u"Open crt...", None))
#if QT_CONFIG(shortcut)
        self.actionOpen_crt.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export...", None))
        self.actionDelete_apps.setText(QCoreApplication.translate("MainWindow", u"Delete apps...", None))
        self.actionAdd_apps.setText(QCoreApplication.translate("MainWindow", u"Add apps...", None))
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

