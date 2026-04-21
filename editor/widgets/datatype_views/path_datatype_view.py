from editor.core.datatypes.path_datatype import PathDatatype
from .base_datatype_view import BaseDatatypeView
from assets.loader import ICONS_FOREGROUND
from PySide6 import QtWidgets
from pathlib import Path


class PathDatatypeView(BaseDatatypeView):
    def __init__(self, datatype: PathDatatype):
        super().__init__(datatype)
        self.datatype: PathDatatype

        self.relative_to: Path | None = None
        self.is_directory: bool = False

        self.main_layout = QtWidgets.QHBoxLayout(self)
        self.path_display_button = QtWidgets.QPushButton()
        self.path_display_button.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        self.main_layout.addWidget(self.path_display_button)
        self.update_path_display_text()

        self.change_path_button = QtWidgets.QPushButton()
        self.change_path_button.setIcon(ICONS_FOREGROUND['folder-open'])
        self.main_layout.addWidget(self.change_path_button)

    def update_path_display_text(self):
        path = self.datatype.value
        if path is None:
            self.path_display_button.setText('Empty')
            self.path_display_button.setEnabled(False)
        else:
            self.path_display_button.setText(path.name)
            self.path_display_button.setEnabled(True)

    def on_datatype_value_change(self):
        self.update_path_display_text()
