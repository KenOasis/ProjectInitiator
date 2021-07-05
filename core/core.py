import os
from typing import List, Dict
from helper import touch, mkdirs
from errors import WrongFileStructInfoError, WrongFilePathError, InitialProjectError
class ProjectInitiator:

    def __init__(self, struct_info: List, option:str =""):
        self.__struct_info = struct_info
        self.__option = option

        try:
            if type(self.__struct_info) is not list:
                raise WrongFileStructInfoError
            elif type(self.__struct_info[0]) is dict:
                pass
            elif type(self.__struct_info[0]) is str:
                self.__struct_info_str_to_dict() 
            else:
                raise WrongFileStructInfoError
        except WrongFileStructInfoError:
            print("WrongFileStructInfoError: The struct_info must be List[dict] or List[str]")
        except WrongFilePathError:
            print("WrongFilePathError: The format of the file path is wrong. Checked Format.md")

    @property
    def struct_info(self):
        return self.__struct_info

    @struct_info.setter
    def struct_info(self, struct_info: Dict):
        self.__struct_info = struct_info

    def initialize_project(self):
        cwd = os.getcwd()
        is_not_as_list = type(self.__struct_info) is not list
        path_is_not_dict = type(self.__struct_info[0]) is not dict
        if is_not_as_list and path_is_not_dict:
            print("Failed to initialed the project")
        else:
            for dir_level in self.__struct_info:
                directories = dir_level["directories"]
                files = dir_level["files"]
                if directories != None:
                    for folder in directories:
                        dir_path = cwd + "/" + folder
                        mkdirs(dir_path)
                if files != None:
                    for file in files:
                        file_path = cwd + "/" + file
                        touch(file_path)
            else:
                print("Successfully initialed the project")

    def __struct_info_str_to_dict(self):
        if type(self.__struct_info[0]) is not str:
            raise WrongFileStructInfoError
        else:
            file_struct_strs = self.__struct_info.copy()
            file_path_split = [x.split('/') for x in file_struct_strs]
            max_len = max(len(s) for s in file_path_split)
            dict_struct_info = [{"directories":None, "files":None} for count in range(0, max_len - 1)]
            for index in range(0, len(file_struct_strs)):
                file_level = len(file_path_split[index]) - 1
                # file_type is 'd' or 'f'
                file_type = file_path_split[index][0]
                if file_type == 'd':
                    # when file_type is directory
                    if dict_struct_info[file_level - 1]["directories"] == None:
                        dict_struct_info[file_level - 1]["directories"] = list()
                    dict_struct_info[file_level - 1]["directories"].append(file_struct_strs[index][2:])
                elif file_type == "f":
                    # when file_type is file
                    if dict_struct_info[file_level - 1]["files"] == None:
                        dict_struct_info[file_level - 1]["files"] = list()
                    dict_struct_info[file_level - 1]["files"].append(file_struct_strs[index][2:])
                else:
                    raise WrongFilePathError
            self.__struct_info = dict_struct_info
                    
# # demo/test codes for struct_info is standard type (List[dict])
# if __name__ == "__main__":
#     first_level = {"directories": ['root'], "files": None}
#     second_level = {"directories": ['root/src', 'root/tests'], "files": None }
#     third_level = {"directories": ['root/src/module', 'root/tests/unit_test', 'root/tests/func_test'], "files": ['root/src/file1.txt', 'root/src/file2', 'root/src/file3.py']}
#     fourth_level = {"directories": None, "files": ['root/tests/unit_test/test_file1.py']}
#     project_struct = [first_level, second_level, third_level, fourth_level]
#     p = ProjectInitiator(project_struct)
#     p.initialize_project()

# demo/test codes for struct_info is List[str]
if __name__ == "__main__":
    file_paths = ['d/root', 'd/root/src/module', 'd/root/tests/unit_test', 'd/root/tests/func_test', 'd/root/src', 'd/root/tests', 'f/root/src/file1.txt', 'f/root/src/file2', 'd/root/src/file3.py', 'f/root/tests/unit_test/test_file1.py']
    p = ProjectInitiator(file_paths)
    p.initialize_project()