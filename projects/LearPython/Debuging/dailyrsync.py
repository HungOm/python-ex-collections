#!/usr/bin/env python3
import os
from multiprocessing import Pool
import subprocess

src = "./data/prod/"
dest = "./data/prod_backup/"

def paths(folder):
    path_ls = []
    for (root,dirs,files )in os.walk(folder):
        print(root)
        path = root[len(folder):]
        if dirs != []:
            for d in dirs:
                path_ls.append((path,d))
        for file in files:
            path_ls.append((path,file))
    return path_ls

def backup(path):
    source = os.path.join(src, path[0], path[1])
    destination = os.path.join(dest, path[0])
    subprocess.call(['rsync', '-arq', src, dest])
if __name__ == "__main__":
    pathList =paths(src)
    p = Pool(len(pathList))
    p.map(backup, pathList)