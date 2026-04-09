from .base_dialog import BaseDialog
from PySide6 import QtWidgets


class SelectionDialog(BaseDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self.button_group = QtWidgets.QWidget()
        self.main_layout.addWidget(self.button_group)
        self.button_group_layout = QtWidgets.QHBoxLayout(self.button_group)

        self.accept_button = QtWidgets.QPushButton()
        self.accept_button.setText('Accept')
        self.accept_button.setEnabled(False)
        self.accept_button.setDefault(True)
        self.accept_button.setSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.accept_button.clicked.connect(self.accept)
        self.button_group_layout.addWidget(self.accept_button)

        self.cancel_button = QtWidgets.QPushButton()
        self.cancel_button.setText('Cancel')
        self.cancel_button.setSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.cancel_button.clicked.connect(self.reject)
        self.button_group_layout.addWidget(self.cancel_button)

    def set_can_continue(self, can_continue: bool):
        if can_continue:
            self.accept_button.setEnabled(True)
        else:
            self.accept_button.setEnabled(False)
