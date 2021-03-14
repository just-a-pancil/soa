import platform, os
from pathlib import PureWindowsPath, Path, PurePath

if platform.system() == "Linux":
    token = 'OC-9R1XArhmhvzTUfP7NXvoFzSacc90CHLge_H_GNCk'
    path = Path(__file__).resolve()
    print(path)
    qrs_path = PurePath(path.cwd(),'media','qrs')
    print(qrs_path)
    code_path = Path(qrs_path, token).with_suffix('.png')
    print(code_path)
    print(code_path.exists())
    print(path.with_suffix('.txt'))
    print(Path(__file__).resolve().with_name('modules'))
    print(PureWindowsPath(code_path))
elif platform.system() == "Windows":

    filename = Path("source_data/text_files/raw_data.txt")

    # Convert path to Windows format
    path_on_windows = PureWindowsPath(filename)

    print(path_on_windows)
    # prints "source_data\text_files\raw_data.txt"
