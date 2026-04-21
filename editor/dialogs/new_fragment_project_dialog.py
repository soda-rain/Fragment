from .selection_dialog import SelectionDialog
from editor.core.datatypes.string_datatype import StringDatatype
from editor.widgets.datatype_views.string_datatype_view import StringDatatypeView
from editor.core.datatypes.path_datatype import PathDatatype
from editor.widgets.datatype_views.path_datatype_view import PathDatatypeView
from PySide6 import QtWidgets
import re

# Reserved names on Windows that cannot be used as directory names
_RESERVED_NAMES = re.compile(
    r'^(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])$',
    re.IGNORECASE
)

def validate_dirname(name: str) -> bool:
    if not name or len(name) > 255:
        return False
    if _RESERVED_NAMES.match(name):
        return False

    pattern = r'^(?![.\s])[\w\s\-]{1,255}(?<![.\s])$'
    return bool(re.match(pattern, name))



class NewFragmentProjectDialog(SelectionDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self.main_content_layout = QtWidgets.QFormLayout(self.central_widget)

        self.project_name = StringDatatype()
        self.project_base_folder = PathDatatype()

        self.project_name_view = StringDatatypeView(self.project_name)
        self.project_base_folder_view = PathDatatypeView(self.project_base_folder)
        self.project_base_folder_view.is_directory = True

        self.project_name.value_changed.connect(lambda: self.set_can_continue(self.is_valid_project()))
        self.project_base_folder.value_changed.connect(lambda: self.set_can_continue(self.is_valid_project()))

        self.main_content_layout.addRow('Project Name', self.project_name_view)
        self.main_content_layout.addRow('Project Base Folder', self.project_base_folder_view)

        self.set_can_continue(self.is_valid_project())

    def is_valid_project(self) -> bool:
        if self.project_name.is_blank():
            return False
        if not validate_dirname(self.project_name.value):
            return False
        
        if not self.project_base_folder.path_exists():
            return False

        return True
