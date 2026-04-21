from editor.core.datatypes.string_datatype import StringDatatype
from .base_datatype_view import BaseDatatypeView
from PySide6 import QtWidgets


class StringDatatypeView(BaseDatatypeView):
    def __init__(self, datatype: StringDatatype):
        super().__init__(datatype)
        self.datatype: StringDatatype # For type checker
        self.main_layout = QtWidgets.QHBoxLayout(self)
        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.textChanged.connect(lambda: self.datatype.update_value(self.line_edit.text()))
        self.main_layout.addWidget(self.line_edit)

    def on_datatype_value_change(self):
        self.line_edit.blockSignals(True)
        self.line_edit.setText(self.datatype.value)
        self.line_edit.blockSignals(False)
