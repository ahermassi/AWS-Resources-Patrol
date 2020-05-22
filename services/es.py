import boto3


def es(region, elasticsearch_running):
    es_client = boto3.client('es', region_name=region)
    domain_names = es_client.list_domain_names()
    domain_names = [domain_name['DomainName'] for domain_name in domain_names['DomainNames']]

    for domain_name in domain_names:
        res = es_client.describe_elasticsearch_domain(DomainName=domain_name)['DomainStatus']
        name = res['DomainName']
        id = res['DomainId']
        created = res['Created']
        instance_type = res['ElasticsearchClusterConfig']['InstanceType']
        instance_count = res['ElasticsearchClusterConfig']['InstanceCount']
        endpoints = ', '.join([endpoint for key, endpoint in res['Endpoints'].items()])

        if created:
            domain_info = {
                'name': name,
                'id': id,
                'created': created,
                'instance_type': instance_type,
                'instance_count': instance_count,
                'endpoints': endpoints
            }
            elasticsearch_running.append(domain_info)
            print('Elasticsearch = ' + str(domain_info))

    return elasticsearch_running
