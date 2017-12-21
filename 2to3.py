import os.path
import re

here = os.path.dirname(os.path.abspath(__file__))
# here = os.getcwd()

files = [file for file in os.listdir(here) if not file.startswith('.') and os.path.isfile(file)]
print(os.listdir(here))
print(files)

m = "print\ ([\"]?.*)"
rs = re.compile(m)

for file in files:
    print(file)
    f = open(file,'r+',encoding='utf-8')
    content = f.read()
    f.seek(0)
    content = rs.sub(r'print(\1)',content)
    f.write(content)
    f.close()

