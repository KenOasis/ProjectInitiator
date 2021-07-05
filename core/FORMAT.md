#This file defines the data structures which defines the project structure info and it is the first argument of the constructor of class core.ProjectInitiator
#example: (prefix: d as directory, f as file)
    --d:root
        --d:src
            --d:module
            --f:file1.txt
            --f:file2
            --f:file3.py
        --d:tests:
            --d:unit_test
            --test_file1.py
        --d:func_test

# First available type is the standard as List[Dictionary] type
## Data structure for each level (from top to bottom as 1 ~ n as Dictionary)
    first_level = {"directories": ['root'], "files": None}
    second_level = {"directories": ['root/src', 'root/tests'], "files":None }
    third_level = {"directories": ['root/src/module', 'root/tests/unit_test', 'root/tests/func_test'], "files": ['root/src/file1.txt', 'root/src/file2', 'root/src/file3.py']}
    fourth_level = {"directories": None, "files": ['root/tests/unit_test/test_file1.py']}
## All 4 dictionaries should save in a List, which 1st_level at index 0, as follows:
    project_struct = [first_level, second_level, third_level, fourth_level]


## Second available type is it store as List[str] type
    project_structure = ['d/root', 'd/root/src/module', 'd/root/tests/unit_test', 'd/root/tests/func_test', 'd/root/src', 'd/root/tests', 'f/root/src/file1.txt', 'f/root/src/file2', 'd/root/src/file3.py', 'f/root/tests/unit_test/test_file1.py']
## The order of the file path is not matter, the file path format is:
    "(d or f)/path/to/the/file"
    d: directory
    f: file
    !!!Important: pls do not have extra '/' at the beginning or the end of the path