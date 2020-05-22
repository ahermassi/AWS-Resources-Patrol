import boto3


def rds(region, rds_running):
    rds_client = boto3.client('rds', region_name=region)
    rds_instances = rds_client.describe_db_instances()

    for instance in rds_instances['DBInstances']:
        identifier = instance['DBInstanceIdentifier']
        engine = instance['Engine']
        status = instance['DBInstanceStatus']
        type = instance['DBInstanceClass']
        storage = instance['AllocatedStorage']
        creation_time = instance['InstanceCreateTime'].strftime("%Y-%m-%d %H:%M:%S")
        publicly_accessible = instance['PubliclyAccessible']

        if status in ['available', 'backing-up', 'failed']:
            instance_info = {
                'identifier': identifier,
                'engine': engine,
                'status': status,
                'type': type,
                'storage': storage,
                'publicly_accessible': publicly_accessible,
                'region': region,
                'creation_time': creation_time
            }
            rds_running.append(instance_info)
            print('RDS = ' + str(instance_info))

    return rds_running
