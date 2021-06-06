import shutil, os
source = "/src/"
destination = "/dst/newfolder/"
if not os.path.exists(destination):
    os.makedirs(destination) 
for f in os.listdir(source):
    if f.endswith(".txt"):
        shutil.move(source + f, destination)
