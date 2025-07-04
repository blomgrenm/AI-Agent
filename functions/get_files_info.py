import os



def get_files_info(working_directory, directory=None):
    directory_path = os.path.abspath(os.path.join(working_directory,directory))
    working_directory_path = os.path.abspath(working_directory)
    # if not os.path.abspath(directory).startswith(os.path.abspath(working_directory)):
    if not directory_path.startswith(working_directory_path):
        # print(os.path.abspath(directory))
        # print(os.path.abspath(working_directory))
        return (f'Error: cannot list "{directory}" as it is outside the permitted working directory')
    if not os.path.isdir(directory):
        # print("Test2")
        return (f'Error: "{directory}" is not a directory')
    
    return_list = []
    
    for i in os.listdir(directory):

        try:
            size = os.path.getsize(i)
        except Exception as e:
            return f"Error: {str(e)}"
        try:
            is_dir = os.path.isdir(i)
        except Exception as e:
            return f"Error: {str(e)}"
        
        # print(f"{i}: file_size={size}, is_dir={is_dir}")
        return_list.append(i+": file_size="+str(size)+", is_dir="+str(is_dir))

    return_string = "\n".join(return_list)

get_files_info("calculator","pkg")
    