
import zipfile
import pathlib

def make_archive(filepaths, destination):
    path = pathlib.Path(destination, "compressed.zip")
    with zipfile.ZipFile(path, "w") as file:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            print(filepath)
            file.write(filepath, arcname=filepath.name)
