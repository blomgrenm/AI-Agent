from functions.get_files_info import get_files_info

print(get_files_info("calculator","."))
print(get_files_info("calculator","pkg"))
get_files_info("calculator","/bin")
get_files_info("calculator","../")