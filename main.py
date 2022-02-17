import boto3
client = boto3.client('iam')
def lambda_handler(event, context):
    response = client.create_role(
        Path='string',
        RoleName='string',
        AssumeRolePolicyDocument='string',
        Description='string',
        MaxSessionDuration=123,
        PermissionsBoundary='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
