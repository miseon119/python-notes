import os
import shutil
from datetime import datetime

# create directory
def create_dir(dir_name):
    try:
        os.makedirs(dir_name, exist_ok=True)
    except OSError as error:
        print("Directory '%s' can not be created")    

# delete directory
def delete_empty_dir(empty_dir):
    try:
        shutil.rmtree(empty_dir)
    except Exception:
        print("remove empty dir error")

# sort directorires by time        
def get_oldest_dir(dir_path):
    dir_path = dir_path + "/*"
    dirs =sorted(glob.glob(dir_path), key=os.path.getctime)
        
        
# check disk available space
def get_available_space_percent():
    total, used, free = shutil.disk_usage("/")
    free_percent = free/total
    # print("Total: %d GiB" % (total // (2**30)))
    # print("Used: %d GiB" % (used // (2**30)))
    # print("Free: %d GiB" % (free // (2**30)))
    return free_percent

  
# get current time
def get_current_time():
    now = datetime.now()
    # year = now.strftime("%Y")
    # month = now.strftime("%m")
    # day = now.strftime("%d")
    # time = now.strftime(('%H-%M-%S-%f')[:-3])
    time = datetime.now().strftime('%H-%M-%S-%f%z')
    # time = datetime.utcnow().strftime('%H-%M-%S-%f')[:-3]
    return time

# Check if File Exists
os.path.isfile('./final_data.csv')

# Check if Directory Exists
os.path.isdir('./final_data_folder')

# Checking If a Certain File or Directory Exists
os.path.exists('./final_data_2020.csv')          # it's ok in directory case
