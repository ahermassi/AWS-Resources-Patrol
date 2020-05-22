import configparser
import logging
import boto3
from utils.init import init
from services.ec2 import ec2
from services.rds import rds
from services.redshift import redshift
from utils.send_email import send_email


def handler():
    config = configparser.ConfigParser()
    config.read('config/config')
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

    aws_region = config['AWS']['AWS_REGION']
    session = boto3.Session(region_name=aws_region)
    sts = session.client('sts')
    ses = session.client('ses')

    sender = 'Instance Watcher <' + config['AWS']['SENDER'] + '>'
    recipients = config['AWS']['RECIPIENTS'].split()
    subject = '[AWS] AWS Resources Patrol - '
    charset = 'UTF-8'
    mail_enabled = config['AWS']['MAIL_ENABLED']

    account_id = sts.get_caller_identity().get('Account')
    account_alias = boto3.client('iam').list_account_aliases()['AccountAliases'][0]
    regions = [region['RegionName'] for region in session.client('ec2').describe_regions()['Regions']]

    # init(sender, ses)

    ec2_running = []
    rds_running = []
    redshift_running = []

    for region in ['us-east-1']:
        print('Checking running instances in: {}'.format(region))
        ec2_running = ec2(region, ec2_running)
        rds_running = rds(region, rds_running)
        redshift_running = redshift(region, redshift_running)

    # send_email(account_id, account_alias, mail_enabled, ses, sender, recipients, subject, charset, ec2_running,
    #            rds_running)

    print('Number of running EC2 instances: {} '.format(len(ec2_running)))
    print('Number of running RDS instances: {} '.format(len(rds_running)))
    print('Number of running Redshift instances: {} '.format(len(redshift_running)))


if __name__ == '__main__':
    handler()

