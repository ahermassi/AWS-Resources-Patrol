import os
import configparser
import boto3
from utils.layer import layer
from utils.verify_sender import verify_sender


def init():
    config = configparser.ConfigParser()
    config.read('config/config')

    sender = 'AWS Resources Patrol <' + config['AWS']['SENDER'] + '>'
    session = boto3.Session(region_name=config['AWS']['AWS_REGION'])
    ses = session.client('ses')

    verify_sender(sender, ses)
    layer()
    os.system('make package')
    os.system('make deploy')
