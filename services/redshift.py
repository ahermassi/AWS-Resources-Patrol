import boto3


def redshift(region, redshift_running):
    redshift_client = boto3.client('redshift', region_name=region)
    redshift_clusters = redshift_client.describe_clusters()

    for cluster in redshift_clusters['Clusters']:
        identifier = cluster['ClusterIdentifier']
        status = cluster['ClusterStatus']
        type = cluster['NodeType']
        nodes = cluster['NumberOfNodes']
        creation_time = cluster['ClusterCreateTime'].strftime('%Y-%m-%d %H:%M:%S')

        if status in ['available', 'storage-full', 'resizing']:
            cluster_info = {
                'identifier': identifier,
                'status': status,
                'type': type,
                'nodes': nodes,
                'region': region,
                'creation_time': creation_time
            }
            redshift_running.append(cluster_info)
            print('Redshift = ' + str(cluster_info))
    
    return redshift_running
