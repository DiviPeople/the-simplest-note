from PyQt5 import QtCore, QtWidgets


class UiNote:
    def __init__(self):
        self.note = None
        self.central_widget = None
        self.vertical_layout = None
        self.plain_text_edit = None
        self.push_button = None
        self.menu_bar = None
        self.menu_file = None
        self.menu_settings = None
        self.menu_help = None
        self.action_settings = None

    def setupUi(self, note):
        self.note = note
        self.note.setObjectName("Note")
        self.note.resize(612, 720)
        self.central_widget = QtWidgets.QWidget(self.note)
        self.central_widget.setObjectName("centralwidget")
        self.vertical_layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.vertical_layout.setObjectName("verticalLayout")
        self.plain_text_edit = QtWidgets.QPlainTextEdit(self.central_widget)
        self.plain_text_edit.setObjectName("plainTextEdit")
        self.vertical_layout.addWidget(self.plain_text_edit)
        self.push_button = QtWidgets.QPushButton(self.plain_text_edit)
        self.push_button.setObjectName("pushButton")
        self.vertical_layout.addWidget(self.push_button)
        self.note.setCentralWidget(self.central_widget)
        self.menu_bar = QtWidgets.QMenuBar(self.note)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 612, 21))
        self.menu_bar.setObjectName("menuBar")
        self.menu_file = QtWidgets.QMenu(self.menu_bar)
        self.menu_file.setObjectName("menuFile")
        self.menu_settings = QtWidgets.QMenu(self.menu_bar)
        self.menu_settings.setObjectName("menuSettings")
        self.menu_help = QtWidgets.QMenu(self.menu_bar)
        self.menu_help.setObjectName("menuHelp")
        self.note.setMenuBar(self.menu_bar)
        self.action_settings = QtWidgets.QAction(self.note)
        self.action_settings.setObjectName("actionSettings")
        self.menu_bar.addAction(self.menu_file.menuAction())
        self.menu_bar.addAction(self.menu_settings.menuAction())
        self.menu_bar.addAction(self.menu_help.menuAction())

        self.push_button.clicked.connect(self.on_button_save_click)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.note)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.note.setWindowTitle(_translate("Note", "Simplest Note"))
        self.push_button.setText(_translate("Note", "Save"))
        self.menu_file.setTitle(_translate("Note", "File"))
        self.menu_settings.setTitle(_translate("Note", "Settings"))
        self.menu_help.setTitle(_translate("Note", "Help"))
        self.action_settings.setText(_translate("Note", "Settings"))

    def on_button_save_click(self):
        file_name = QtWidgets.QFileDialog.getSaveFileName(self.note, caption='Save note', filter='.txt')
        print(f'{file_name[0]}{file_name[1]}')
