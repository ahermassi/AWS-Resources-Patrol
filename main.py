import configparser
import boto3
from utils.verify_sender import verify_sender
from utils.layer import layer

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config/config')

    aws_region = config['AWS']['AWS_REGION']
    session = boto3.Session(region_name=aws_region)
    ec2 = session.client('ec2')
    sts = session.client('sts')
    ses = session.client('ses')

    sender = "Instance Watcher <" + config['AWS']['SENDER'] + ">"
    recipients = config['AWS']['RECIPIENTS'].split()
    subject = '[AWS] AWS Resources Patrol - '
    charset = "UTF-8"
    mail_enabled = config['AWS']['MAIL_ENABLED']

    account_id = sts.get_caller_identity().get('Account')
    account_alias = boto3.client('iam').list_account_aliases()['AccountAliases'][0]
    regions = [region['RegionName'] for region in ec2.describe_regions()['Regions']]

    # verify_sender(sender, ses)
    layer()

    ec2_running = []

    # for region in regions:
    #     # logging.info("Checking running instances in: %s", region)
    #     ec2_running = ec2(region, ec2_running)
