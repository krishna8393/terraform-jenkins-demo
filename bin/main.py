import json
import boto3
import logging
import os

LOGGER = logging.getLogger()
LOGGER.setLevel(os.getenv('LOGLEVEL', logging.INFO))

def lambda_handler(event, context):

    session = boto3.Session()
    LOGGER.info(f'Event: {event}')
    SERVICE_CODE = event['SERVICE_CODE']
    QUOTAS_CODE = event['QUOTAS_CODE']
    DESIRED_LIMIT = event['DESIRED_LIMIT']
    REGION_LIST = event['REGION']
    
    # client = boto3.client('service-quotas')
    try:
        for region in REGION_LIST:
            client = session.client(
                'service-quotas',
                region_name=region
            )
            default_val = client.get_aws_default_service_quota(
                ServiceCode=SERVICE_CODE,
                QuotaCode=QUOTAS_CODE
                )
            default_value = default_val['Quota']['Value']
            
            response = client.get_service_quota(
                ServiceCode = SERVICE_CODE,
                QuotaCode = QUOTAS_CODE
                )
            current_value = response['Quota']['Value']
            
            if(current_value >= default_value and DESIRED_LIMIT > current_value):
                response = client.request_service_quota_increase(
                    ServiceCode=SERVICE_CODE,
                    QuotaCode=QUOTAS_CODE,
                    DesiredValue=int(DESIRED_LIMIT),
                    )
                if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                    LOGGER.info(f'Successfully requested service limit increase for AWS account '+region)
                else:
                    LOGGER.error(f'Failed to successfully request a service limit increase for AWS account')
            elif(DESIRED_LIMIT == current_value):
                print('EIP Desired Value limit and Current value is equal in region:'+region+', Kindly provide higher Desire value to increase quota')
            elif(DESIRED_LIMIT < current_value):
                print('Privoided EIP limit is lesser than current value in region:'+region+', Kindly provide higher Desired value to increase quota.')
    except Exception as e:
        LOGGER.error(f'Error requesting service limit increase: {e}')
