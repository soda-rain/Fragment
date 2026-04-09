from pathlib import Path

def create_fragment_project(path: Path, name: str):
    """Creates a blank fragment project at a given path."""
    (path / name).mkdir()
    (path / name / '.fragment').mkdir()
    (path / name / 'resources').mkdir()
    with open(path / name / 'project.fragment', 'w') as f:
        f.write('')
