import os

file_path = "data.txt"
if os.path.exists(file_path):
    with open(file_path) as file:
        for line in file:
            continue

def get_size(path):
    return sum(os.path.getsize(os.path.join(root, file)) 
               for root, _, files in os.walk(path) for file in files)

def sum_small_dirs(root_path, limit=100000):
    sizes = {dirpath: get_size(dirpath) for dirpath, _, _ in os.walk(root_path)}
    return sum(size for size in sizes.values() if size <= limit)



root_directory = "/Users/yuliannapriadka/Desktop/backend(1)/lab_04/"
print(sum_small_dirs(root_directory))

