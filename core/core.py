import os
from typing import List, Dict
from helper import touch, mkdirs
class ProjectInitiator:

    def __init__(self, struct_info: List[Dict], option:str =""):
        self.__struct_info = struct_info
        self.__option = option

    @property
    def struct_info(self):
        return self.__struct_info

    @struct_info.setter
    def struct_info(self, struct_info: Dict):
        self.__struct_info = struct_info

    def initialize_project(self):
        cwd = os.getcwd()
        for dir_level in self.__struct_info:
            folders = dir_level["folders"]
            files = dir_level["files"]
            if folders != None:
                for folder in folders:
                    dir_path = cwd + "/" + folder
                    mkdirs(dir_path)
            if files != None:
                for file in files:
                    file_path = cwd + "/" + file
                    touch(file_path)
        else:
            print("Successfully initialed the project")


# # demo/test codes
# if __name__ == "__main__":
#     first_level = {"folders": ['root'], "files": None}
#     second_level = {"folders": ['root/src', 'root/tests'], "files": None }
#     third_level = {"folders": ['root/src/module', 'root/tests/unit_test', 'root/tests/func_test'], "files": ['root/src/file1.txt', 'root/src/file2', 'root/src/file3.py']}
#     fourth_level = {"folders": None, "files": ['root/tests/unit_test/test_file1.py']}
#     project_struct = [first_level, second_level, third_level, fourth_level]
#     p = ProjectInitiator(project_struct)
#     p.initialize_project()