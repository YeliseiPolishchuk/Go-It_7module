import sys
from pathlib import Path
from sorting_func_yp import read_folder, rename_file


def sort_this(p: Path):
    # folder_path = Path(sys.argv[1])
    # folder_path = Path('to_sort')

    # Создаю папку для отсортированных файлов
    sorted_folder_path = Path('./sorted')
    sorted_folder_path.mkdir(exist_ok=True, parents=True)

    read_folder(p)
    rename_file(sorted_folder_path)
