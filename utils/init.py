import os
from utils.layer import layer
from utils.verify_sender import verify_sender


def init(sender, ses):
    verify_sender(sender, ses)
    layer()
    os.system('make package')
    os.system('make deploy')
