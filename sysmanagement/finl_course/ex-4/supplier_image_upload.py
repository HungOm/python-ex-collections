# #!/usr/bin/env python3
import requests
import os

# # This example shows how a file can be uploaded using
# # The Python Requests module

# def get_files_from_dir(dir):
#     all_files =dict()
#     for root, directories, files in os.walk(dir):
        
#         for filename in files:
#             if os.path.splitext(os.path.join(root, filename))[1].lower() == ".jpeg":
#                 # print()
#                 # with open(os.path.join(root, filename),'rb') as data:
#                 all_files[filename] = open(os.path.join(root,filename),'rb')
                
    
#             # Join the two strings in order to form the full filepath.
#             # filepath = os.path.join(root, filename)
#             # file_paths.append(filepath)  # Add it to the list. 
#             # 

#     return all_files  # Self-explanatory.

# path = os.getcwd()+'/supplier-data/images'

# images =get_files_from_dir(path)
# print(images)





# #url = "http://localhost/upload/"
# # with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
# #r = requests.post(url, files=images)

# import requests
# import os

# The Python Requests module

def get_files_from_dir(dir,url):
    all_files =list()
    for root, directories, files in os.walk(dir):
        for filename in files:
            if os.path.splitext(os.path.join(root, filename))[1].lower() == ".jpeg":
                with open(os.path.join(root,filename),'rb') as data:
                  r = requests.post(url,files={'file': data})
                  all_files.append(r)
    return  all_files
    #return requests.post(url,files=all_files)  # Self-explanatory.

path = os.getcwd()+'/supplier-data/images'
url = "http://localhost/upload/"
images =get_files_from_dir(path,url)
print(images)





#url = "http://localhost/upload/"
#with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
#r = requests.post(url, files=images)
#print(r)