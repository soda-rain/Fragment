from pathlib import Path

def create_fragment_config(path: Path):
    """Creates a .fragment config folder at path"""
    (path / '.fragment').mkdir()
    (path / '.fragment' / 'library').mkdir()
    with open(path / '.fragment' / 'library' / 'recent_projects.json', 'w') as file:
        file.write('[]')
