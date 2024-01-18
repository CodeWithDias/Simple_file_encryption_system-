import os

# Basic Python program designed for securing sensitive data through encryption
# Created by M.D.W.D Bandaranayaka 
# code_with_dias ----> https://www.youtube.com/channel/UCsPlOm3lx7eisnd-6G0-yzA

# Encrypting the data
def sub_encrypt(data, key=7):
    encrypted_data = bytearray()
    for byte in data:
        encrypted_byte = (byte + key) % 256
        encrypted_data.append(encrypted_byte)
    return bytes(encrypted_data)

# Decrypting the data
def sub_decrypt(encrypted_data, key=7):
    return sub_encrypt(encrypted_data, -key)


# Read the file and rewrite the encrypted data
def main_encrypt(file_paths):
    for file_path in file_paths:
        with open(file_path, "rb") as the_file:
            content = the_file.read()
        encrypted = sub_encrypt(content)
        with open(file_path, "wb") as the_file:
            the_file.write(encrypted)

# Read the file and rewrite the decrypted data
def main_decrypt(file_paths):
    for file_path in file_paths:
        with open(file_path, "rb") as the_file:
            content = the_file.read()
            print(file_path)
        decrypted = sub_decrypt(content)
        with open(file_path, "wb") as the_file:
            the_file.write(decrypted)
            print(file_path)

# Return a list of all the files in the root directory and it's sub directories
def list_files_and_folders(directory_path):
    file_path_list = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_path_list.append(file_path)

    return file_path_list

# When modifying the root_directory_path, especially on a Windows system, 
# ensure that your path is formatted correctly, such as: "C:\\root\\directory\\path"
root_directory_path = "C:\\Path\\TO\\Root\\Directory"

all_files = list_files_and_folders(root_directory_path)
print("""
Warning: Utilizing this program may pose a risk to your data.
Ensure that the root_directory_path is set correctly.
When modifying the root_directory_path, particularly on a Windows system, make sure that your path is formatted correctly, for example: "C:\\Root\\Directory\\Path".
""")
try:
    num = int(input("Enter what you want to do(1 --> encrypt/ 2 --> decrypt) - "))
    if num == 2:
        main_decrypt(all_files)
    if num == 1:
        main_encrypt(all_files)
except ValueError:
    exit("---------Invalid command-------")
