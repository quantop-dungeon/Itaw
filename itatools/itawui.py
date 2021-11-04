# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'itaw.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Itaw(object):
    def setupUi(self, Itaw):
        Itaw.setObjectName("Itaw")
        Itaw.resize(1500, 850)
        Itaw.setStyleSheet("QWidget {\n"
"    font: 8pt \"OpenSans\";\n"
"    background-color: white;\n"
"}\n"
"QComboBox {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(0, 0, 0);\n"
"}\n"
"QToolButton {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: white;\n"
"}\n"
"QToolButton:hover {\n"
"    background-color: rgb(204, 232, 255);\n"
"}\n"
"QToolButton:checked {\n"
"    background-color: rgb(204, 232, 255);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(240, 240, 240);\n"
"}\n"
"QToolTip {\n"
"    font: 10pt \"Calibri Light\";\n"
"}\n"
"QMenu::item {\n"
"    /* sets background of menu item. set this to something non-transparent\n"
"        if you want menu color and menu item color to be different */\n"
"    background-color: transparent;\n"
"}\n"
"QMenu::item:selected { /* when user selects item using mouse or keyboard */\n"
"    background-color: rgb(204, 232, 255);\n"
"    color: black;\n"
"}\n"
"QPushButton { \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    min-width: 8em;\n"
"    padding: 3px; \n"
"}")
        self.centralwidget = QtWidgets.QWidget(Itaw)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.openDirButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openDirButton.sizePolicy().hasHeightForWidth())
        self.openDirButton.setSizePolicy(sizePolicy)
        self.openDirButton.setMinimumSize(QtCore.QSize(112, 0))
        self.openDirButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.openDirButton.setObjectName("openDirButton")
        self.gridLayout.addWidget(self.openDirButton, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mplVBox = QtWidgets.QVBoxLayout()
        self.mplVBox.setObjectName("mplVBox")
        self.horizontalLayout.addLayout(self.mplVBox)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.argsLabel = QtWidgets.QLabel(self.centralwidget)
        self.argsLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.argsLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.argsLabel.setObjectName("argsLabel")
        self.gridLayout_2.addWidget(self.argsLabel, 1, 0, 1, 1)
        self.traceListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.traceListWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.traceListWidget.setDragEnabled(False)
        self.traceListWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.traceListWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.traceListWidget.setObjectName("traceListWidget")
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("trace_not_disp_icon.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("trace_disp_icon.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        item.setIcon(icon)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.traceListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setIcon(icon)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.traceListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setIcon(icon)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.traceListWidget.addItem(item)
        self.gridLayout_2.addWidget(self.traceListWidget, 2, 1, 1, 1)
        self.readTraceButton = QtWidgets.QPushButton(self.centralwidget)
        self.readTraceButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.readTraceButton.setObjectName("readTraceButton")
        self.gridLayout_2.addWidget(self.readTraceButton, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 3, 1, 1, 1)
        self.argsLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.argsLineEdit.setMinimumSize(QtCore.QSize(140, 0))
        self.argsLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.argsLineEdit.setText("")
        self.argsLineEdit.setPlaceholderText("")
        self.argsLineEdit.setObjectName("argsLineEdit")
        self.gridLayout_2.addWidget(self.argsLineEdit, 1, 1, 1, 1)
        self.saveTraceButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveTraceButton.setObjectName("saveTraceButton")
        self.gridLayout_2.addWidget(self.saveTraceButton, 4, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout.setStretch(0, 3)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 6)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 1, 4, 1, 1)
        self.dirLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.dirLineEdit.setObjectName("dirLineEdit")
        self.gridLayout.addWidget(self.dirLineEdit, 2, 4, 1, 1)
        Itaw.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Itaw)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1500, 19))
        self.menubar.setObjectName("menubar")
        self.actionsMenu = QtWidgets.QMenu(self.menubar)
        self.actionsMenu.setObjectName("actionsMenu")
        Itaw.setMenuBar(self.menubar)
        self.tightLayoutAction = QtWidgets.QAction(Itaw)
        self.tightLayoutAction.setObjectName("tightLayoutAction")
        self.actionitem2 = QtWidgets.QAction(Itaw)
        self.actionitem2.setObjectName("actionitem2")
        self.resetColorOrderAction = QtWidgets.QAction(Itaw)
        self.resetColorOrderAction.setObjectName("resetColorOrderAction")
        self.actionsMenu.addAction(self.tightLayoutAction)
        self.actionsMenu.addAction(self.resetColorOrderAction)
        self.menubar.addAction(self.actionsMenu.menuAction())
        self.argsLabel.setBuddy(self.argsLineEdit)
        self.label.setBuddy(self.dirLineEdit)

        self.retranslateUi(Itaw)
        QtCore.QMetaObject.connectSlotsByName(Itaw)

    def retranslateUi(self, Itaw):
        _translate = QtCore.QCoreApplication.translate
        Itaw.setWindowTitle(_translate("Itaw", "Itaw"))
        self.openDirButton.setText(_translate("Itaw", "Open"))
        self.argsLabel.setText(_translate("Itaw", "Args:"))
        self.traceListWidget.setToolTip(_translate("Itaw", "<html><head/><body><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:19px; background-color:#ffffff;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:14px; color:#000000;\">Ctrl+s - save selected trace</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:19px; background-color:#ffffff;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:14px; color:#000000;\">Ctrl+x - toggle visibility</span></pre></body></html>"))
        __sortingEnabled = self.traceListWidget.isSortingEnabled()
        self.traceListWidget.setSortingEnabled(False)
        item = self.traceListWidget.item(0)
        item.setText(_translate("Itaw", "1. transmission td scan 2"))
        item = self.traceListWidget.item(1)
        item.setText(_translate("Itaw", "2. transmission td locked res"))
        item = self.traceListWidget.item(2)
        item.setText(_translate("Itaw", "3. new trace"))
        self.traceListWidget.setSortingEnabled(__sortingEnabled)
        self.readTraceButton.setText(_translate("Itaw", "Read"))
        self.argsLineEdit.setToolTip(_translate("Itaw", "<html><head/><body><p>e.g. &quot;ch=1, mem=True&quot;</p></body></html>"))
        self.saveTraceButton.setText(_translate("Itaw", "Save"))
        self.label.setText(_translate("Itaw", "Directory:"))
        self.actionsMenu.setTitle(_translate("Itaw", "Actions"))
        self.tightLayoutAction.setText(_translate("Itaw", "Tight layout"))
        self.actionitem2.setText(_translate("Itaw", "item2"))
        self.resetColorOrderAction.setText(_translate("Itaw", "Reset color order"))
