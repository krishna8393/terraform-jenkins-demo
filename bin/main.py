# import boto3
# client = boto3.client('iam')
# def lambda_handler():
#     response = client.get_role(
#     RoleName='jenkins_slave')
#     print('response', response)
 
# if __name__ == "__main__":
#     lambda_handler()
#!/usr/bin/env python

import boto3
import json
import time
import sys

client = boto3.client('ec2')
# snapshot = ec2.Snapshot('id')
def lambda_handler(instance_ids):
    print('instance_ids', instance_ids)
    for instance in instance_ids:
        snapshot = client.create_snapshots(
        Description ='take snapshot for all the provided instances',
        InstanceSpecification={
            'InstanceId': instance,
            'ExcludeBootVolume': False
        }
        )
        # snapshot_id=snapshot['Snapshots'][0]['SnapshotId']
        snapshotids = get_snapshot_ids(snapshot['Snapshots'])
        for snapshot_id in snapshotids:
            print('snapshot_id', snapshot_id)
            status= check_status(snapshot_id)
            print('status', status)
            while status != "completed":
                print(status)
                time.sleep(5)
                status= check_status(snapshot_id)
    print('status', status)

def check_status(snapshot_id):
    snapshot_status = client.describe_snapshots(
    SnapshotIds=[snapshot_id])
    status=snapshot_status['Snapshots'][0]['State']
    return status

def get_snapshot_ids(snapshots):
    snapshotids = []
    for snapshot in snapshots:
        snapshotids.append(snapshot['SnapshotId'])
    return snapshotids


if __name__ == "__main__":
    print('programname', sys.argv[0])
    # n = len(sys.argv[1])
    instance_ids = sys.argv[1].split(',')
    print('instance_ids', instance_ids)
    lambda_handler(instance_ids)
