import boto3
client = boto3.client('iam')
def lambda_handler(event, context):
    response = client.create_user(
    Path='/',
    UserName='terraform',
    Tags=[
        {
            'from': 'terraform'
        },
    ]
)
