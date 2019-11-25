import os
from userInfo import jobTittle

for job in jobTittle:
    try:
        os.system('python apply.py "' + job + '"')
    except Exception as e:
        raise
