from PySide6 import QtWidgets


class BaseDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setModal(True)

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.central_widget = QtWidgets.QWidget()
        self.main_layout.addWidget(self.central_widget)

