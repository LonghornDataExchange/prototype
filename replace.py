import os


# Finds find_lines in code and replaces the lines with replace_lines
def find_and_replace(code,find_lines,replace_lines):
    num_lines = len(code)
    num_find = len(find_lines)
    num_replace = len(replace_lines)

    i = 0
    while i < len(code) - num_find:
        if code[i] == find_lines[0]:

            match = True
            for j in range(num_find):
                print(i+j)
                if code[i+j] != find_lines[j]:
                    match = False

            if match:
                for k in range(num_find):
                    code.pop(i) # removes the line we want to delete

                for k in range(len(replace_lines)):
                    code.insert(i,replace_lines[ num_replace-1-k])

        i += 1

    return code


# Handles files and configurations
# Calls find_and_replace()
def replace_code(fandr_file_path, code_file_path):
    # Get find and replace lines
    fandr_file = open(fandr_file_path,'r')

    replace = False
    find_lines = []
    replace_lines = []
    for line in fandr_file:
        if line.strip() == 'Find':
            continue # Ignore

        if line.strip() == 'Replace':
            replace = True
            continue

        if not replace:
            find_lines.append(line)
        else:
            replace_lines.append(line)

    fandr_file.close()

    # Open and read in the file
    in_out_file = open(code_file_path,'r')

    in_code = []
    for line in in_out_file:
        in_code.append(line)

    # Replace the lines
    out_code = find_and_replace(in_code,find_lines,replace_lines)

    in_out_file.close()
    in_out_file = open(code_file_path,'w')

    in_out_file.writelines(out_code)

    in_out_file.close()


# Find specific type of file out of a list of paths
# Returns a copy of the paths
def select_file_type(paths,suffix):
    out_paths = []
    for path in paths:
        if path.find(suffix)>-1:
            out_paths.append(path)

    return out_paths.copy()

# Out of a list of files, returns only the folders
def get_folders(files):

    return_files = []
    for file in files:
        if file.find(".") < 0:
            return_files.append(file)

    return return_files.copy()


def rec_get_paths(current_path, all_paths):
    files = os.listdir(current_path)
    folders = get_folders(files)

    for file in files:
        all_paths.append(current_path + '/' +file)

    if len(folders) == 0:
        return
    else:
        for folder in folders:
            rec_get_paths(current_path + '/' + folder, all_paths)

        return


def get_all_paths(start_path):
    all_paths = []
    rec_get_paths(start_path,all_paths)
    return all_paths


def main():

    replacement_document = './findandreplace.txt'
    suffix = '.html'

    # Find all paths
    all_paths = get_all_paths('.')

    # Select just the paths we want to modify by suffix
    select_paths = select_file_type(all_paths,suffix)

    # Replace each selected path
    for each_path in select_paths:
        replace_code(replacement_document,each_path)



main()
