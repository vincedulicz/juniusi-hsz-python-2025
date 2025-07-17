import os, shutil
import time


def teszt():
    try:
        if not os.path.exists("example.txt"):
            with open("example.txt", "w") as f:
                f.write("Hello world")
    except FileNotFoundError as e:
        print(e)

    for file in os.listdir("."):
        print(file)

    print(os.getcwd())

# teszt()

# os.mkdir("new folder")

os.chdir("..")
print(f'hol vagyunk: {os.getcwd()}')

txt_files = [f for f in os.listdir(".") if f.endswith(".txt")]
print(f'txt files {txt_files}')

file_size = os.path.getsize("example.txt")
print(file_size)

# powershell

if os.name == "nt":
    os.system("dir")
else: # posix -> linux/macOS
    os.system("ls")
base_path = os.getcwd()
file_path = os.path.join(base_path, "folder", "file.txt")

print(f'Full path: {file_path}')

with open("tempfile.tmp", "w") as temp_file:
    temp_file.write("tmp data")
print("tmp file created")

os.remove("tempfile.tmp")

os.environ["NEW_VAR"] = "pyauto"
print("new var: ", os.getenv("NEW_VAR"))


for root, dirs, files in os.walk("."):
    print("Dir: ", root)
    for file in files:
        print("File: ", file)



path = "new folder"
if os.path.isfile(path):
    print(f"ez egy file {path}")
elif os.path.isdir(path):
    print(f'ez egy mappa {path}')
else:
    print(f'{path} nem létezik')


mod_time = os.path.getmtime("example.txt")
print(mod_time)
print(time.ctime(mod_time))

try:
    os.remove("non.file")
except FileNotFoundError as e:
    print(f'error {e}')


os.makedirs("parent/child/grandchild", exist_ok=True)
os.removedirs("parent/child/grandchild")

print("current user:", os.getlogin())

temp_dir = os.getenv("TEMP", "/tmp")
print(temp_dir)

# with open("permissions.txt", "w") as f:
#     f.write("permission exampllleee")

# print(os.chmod("permissions.txt", 0o444)) # read

file_size = os.stat("example.txt").st_size
print(file_size)

# hash -> dict {k: v)
for key, value in os.environ.items():
    print(f'K: {key} - V: {value}')


start_time = time.time()
time.sleep(2)
end_time = time.time()
print(f'program runtime: {end_time-start_time} sec')

