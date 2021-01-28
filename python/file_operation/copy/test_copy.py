import os
import shutil

# src = './test_1.json'
src = './test_1.json'
if os.path.isfile(src):
    print("exit!")

    new_dir_path = './new-dir'
    os.mkdir(new_dir_path)

    n = 10
    for i in range(1, n + 1):
        copy = new_dir_path + '/test_' + str(i) + '.json'
        shutil.copyfile(src, copy)
