
import json

file_dir = 'D:/Files/pythonWorkspace/python-advanced/basic/base/file/demo.json'


def read_json():
    with open(file_dir, "r", encoding="utf-8") as file:
        print(json.dumps(file.read()))


# read_json()