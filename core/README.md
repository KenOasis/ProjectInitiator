#the data type use to describe the project structure is the List which contain Dictionary type which has the folder/file name at that level

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


## Data structure for each level of directory
first_level = {"folders": ['root'], "files": None}
second_level = {"folders": ['root/src', 'root/tests'], "files":None }
third_level = {"folders": ['root/src/module', 'root/tests/unit_test', 'root/tests/func_test'], "files": ['root/src/file1.txt', 'root/src/file2', 'root/src/file3.py']}
fourth_level = {"folders": None, "files": ['root/tests/unit_test/test_file1.py']}

## All 4 dictionaries should save in a List, which 1st_level at index 0, as follows:
project_struct = [first_level, second_level, third_level, fourth_level]
