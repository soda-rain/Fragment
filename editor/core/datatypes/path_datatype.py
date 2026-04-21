from .base_datatype import BaseDatatype
from pathlib import Path

class PathDatatype(BaseDatatype):
    def __init__(self):
        super().__init__()
        self.value: Path | None = None

    def update_value(self, path: Path | None):
        self.value = path
        self.value_changed.emit()

    def is_blank(self) -> bool:
        return self.value is None
    
    def path_exists(self) -> bool:
        if self.value is None:
            return False
        return self.value.exists()
    
    def to_json_data(self) -> list:
        return [
            'editor.datatype.path_datatype',
            self.value.as_posix() if isinstance(self.value, Path) else None
        ]
    
    def load_json_data(self, data: list):
        self.update_value(data[1])
