# This script generates html file with links of all the file existing in the 
# present working directory.
# Author: Anshu Raj
# Email: imanshuraj@gmail.com


import os
start = """<!DOCTYPE html><html><head><style>body {text-align: centre;}</style><title>Download</title></head><body> """
last = """</body></html>"""

fo = open("index.html", "w")
list = os.listdir(os.getcwd())
fo.write(start)
for i in list:
    fo.write('<a href="' + i + '"> ' + i + "</a><p>")
fo.write(last)
fo.close()
