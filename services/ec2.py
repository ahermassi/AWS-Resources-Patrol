import boto3


def ec2(region, ec2_running):
    ec2_client = boto3.client('ec2', region_name=region)
    reservations = ec2_client.describe_instances()['Reservations']

    for reservation in reservations:
        for instance in reservation['Instances']:
            state = instance['State']['Name']
            type = instance['InstanceType']
            id = instance['InstanceId']
            launch_time = instance['LaunchTime'].strftime("%Y-%m-%d %H:%M:%S")
            tags = instance['Tags'] if 'Tags' in instance else []
            name = "unnamed"
            for tag in tags:
                if tag['Key'] == 'Name':
                    name = tag['Value']
            if state == 'running':
                instance_info = {
                    'name': name,
                    'state': state,
                    'type': type,
                    'id': id,
                    'region': region,
                    'launch_time': launch_time
                }
                ec2_running.append(instance_info)
                print('EC2 = ' + str(instance_info))
    return ec2_running
