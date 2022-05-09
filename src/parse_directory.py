import os


def get_all_files_path(init_path):
    files = []
    for file in os.listdir(init_path):
        path = os.path.join(init_path, file)
        if os.path.isdir(path):
            files += get_all_files_path(path)
        else:
            files.append(path)
    return files


def get_files_from_path_list(paths):
    files = []
    for path in paths:
        files += get_all_files_path(path)

    return files
