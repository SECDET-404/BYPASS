import os, platform
os.system("rm -rf BYPASS")
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from bypass import Adnan
    Adnan()
elif bit == '32bit':
    from bypass import Adnan
    Adnan()
