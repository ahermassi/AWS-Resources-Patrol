import boto3
from datetime import datetime, timedelta


def costs():
    cost_client = boto3.client('ce', region_name='us-east-1')
    yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
    first_day_of_month = datetime.today().replace(day=1).strftime('%Y-%m-%d')
    cost_and_usage = cost_client.get_cost_and_usage(
        TimePeriod={
            'Start': first_day_of_month,
            'End': yesterday
        },
        Granularity='MONTHLY',
        Metrics=[
            'AmortizedCost',
        ]
    )
    result = cost_and_usage['ResultsByTime'][0]
    cost = result['Total']['AmortizedCost']['Amount']
    return round(float(cost), 2)

