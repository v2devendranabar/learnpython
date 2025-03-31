import os

def update_server_config(file_path, key, value):

    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exists")
        return
    else:
        print(f"Updated {new_value} in {server_config} for {new_key} updated successfully!")
    
    with open(file_path,'r') as file:
        lines = file.readlines()

    with open(file_path,'w') as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)

server_config = input("Enter the configuration file path: ")
new_key = input("Enter the key to update: ")
new_value = input("Enter the new value: ")

if not server_config or not new_key or not new_value:
    print("Error: File path, key, or value cannot be empty!")
else:
    update_server_config(server_config, new_key, new_value)