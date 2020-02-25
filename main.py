from gui import Gui
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QFile, QTextStream
import breeze_resources

if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    w = Gui(app)
    w.resize(800, 600)
    w.show()

    sys.exit(app.exec_())