import os

# mkdir - make directory
# rmdir - remove directory
directory = "/home/ulan/edu/justcode/python14/9_2"
new_dir = os.path.join(directory, "test1")

print(new_dir)
# os.mkdir(new_dir)
# os.rmdir(new_dir)
os.remove(new_dir + "/to_delete.py")


