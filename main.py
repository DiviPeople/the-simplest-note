import sys

from PyQt5 import QtWidgets

from simplest_note.note_body import UiNote


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Note = QtWidgets.QMainWindow()
    ui = UiNote()
    ui.setupUi(Note)
    Note.show()
    sys.exit(app.exec_())
