import os



def get_files_info(working_directory, directory=None):
    directory_path = os.path.abspath(os.path.join(working_directory,directory or '.'))
    working_directory_path = os.path.abspath(working_directory)
    # if not os.path.abspath(directory).startswith(os.path.abspath(working_directory)):
    if not directory_path.startswith(working_directory_path):
        return (f'Error: cannot list "{directory}" as it is outside the permitted working directory')
    if not os.path.isdir(directory_path):
        # print("Test2")
        return (f'Error: "{directory}" is not a directory')
    
    return_list = []
    
    for i in os.listdir(directory_path):

        item_path = os.path.join(directory_path, i)
        try:
            size = os.path.getsize(item_path)
        except Exception as e:
            return f"Error: {str(e)}"
        try:
            is_dir = os.path.isdir(item_path)
        except Exception as e:
            return f"Error: {str(e)}"
        
        # print(f"{i}: file_size={size}, is_dir={is_dir}")
        return_list.append("- "+i+": file_size="+str(size)+", is_dir="+str(is_dir))

    return_string = "\n".join(return_list)

    return return_string

# get_files_info("calculator","pkg")
    