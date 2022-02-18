import boto3
client = boto3.client('iam')
def lambda_handler():
    response = client.get_user(
    UserName='EKS_Creator')
    print('response', response)
 
if __name__ == "__main__":
    lambda_handler()
