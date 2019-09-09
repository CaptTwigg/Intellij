import sys
from PyQt5.QtWidgets import QWidget, QApplication


class ${NAME}(QWidget):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = ${NAME}()
    widget.show()
    sys.exit(app.exec_())
