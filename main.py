import boto3
client = boto3.client('iam')
def lambda_handler():
    response = client.create_user(
    Path='/',
    UserName='terraform',
    Tags=[
        {
            'from': 'terraform'
        },
    ]
)
if __name__ == "__main__":
    lambda_handler()
