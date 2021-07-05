# demo/test codes
from core import ProjectInitiator
if __name__ == "__main__":
    first_level = {"folders": ['root'], "files": None}
    second_level = {"folders": ['root/src', 'root/tests'], "files": None }
    third_level = {"folders": ['root/src/module', 'root/tests/unit_test', 'root/tests/func_test'], "files": ['root/src/file1.txt', 'root/src/file2', 'root/src/file3.py']}
    fourth_level = {"folders": None, "files": ['root/tests/unit_test/test_file1.py']}
    project_struct = [first_level, second_level, third_level, fourth_level]
    p = ProjectInitiator(project_struct)
    p.initialize_project()

# # demo/test codes for struct_info is List[str]
# if __name__ == "__main__":
#     file_paths = ['d/root', 'd/root/src/module', 'd/root/tests/unit_test', 'd/root/tests/func_test', 'd/root/src', 'd/root/tests', 'f/root/src/file1.txt', 'f/root/src/file2', 'd/root/src/file3.py', 'f/root/tests/unit_test/test_file1.py']
#     p = ProjectInitiator(file_paths)
#     p.initialize_project()