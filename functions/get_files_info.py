import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'

    contents = os.listdir(full_path)

    contents_desc = []
    try:
        for content in contents:
            contents_desc.append(f'{content} file_size={os.path.getsize(f'{full_path}/{content}')} bytes, is_dir={os.path.isdir(f'{full_path}/{content}')}')
        return '- ' + '\n- '.join(contents_desc)
    except Exception as e:
        return f'Error: {e}'

