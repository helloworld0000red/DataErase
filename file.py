import os
import shutil
import random
def overwrite_with_random_data(file_path):
    try:
        with open(file_path, "rb+") as f:
            file_size = os.path.getsize(file_path)
            random_data = bytearray(random.getrandbits(8) for _ in range(file_size))
            f.write(random_data)
        print(f"Overwritten file: {file_path}")
    except Exception as e:
        print(f"Failed to overwrite {file_path}: {e}")
def secure_delete_contents(directory):
    if not os.path.exists(directory):
        print("Directory does not exist.")
        return
    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            overwrite_with_random_data(file_path)
            try:
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
            except Exception as e:
                print(f"Failed to delete {file_path}: {e}")
        for name in dirs:
            dir_path = os.path.join(root, name)
            try:
                os.rmdir(dir_path)
                print(f"Deleted directory: {dir_path}")
            except Exception as e:
                print(f"Failed to delete {dir_path}: {e}")
if __name__ == "__main__":
    directory = input("Enter the path of the directory whose contents you want to erase: ")
    secure_delete_contents(directory)