import boto3
from time import sleep

def kick_detect_drift(region):
    print(region)
    cfn = boto3.client('cloudformation',region_name=region)
    stacks = [x['StackName'] for x in cfn.list_stacks(StackStatusFilter=['CREATE_COMPLETE','UPDATE_COMPLETE','UPDATE_ROLLBACK_COMPLETE'])['StackSummaries']]
    detection_ids=[cfn.detect_stack_drift(StackName=x) for x in stacks]
    return [x['StackDriftDetectionId'] for x in detection_ids]

def check_drift(region):
    print(region)
    cfn = boto3.client('cloudformation',region_name=region)
    stacks = [x['StackName'] for x in cfn.list_stacks(StackStatusFilter=['CREATE_COMPLETE','UPDATE_COMPLETE','UPDATE_ROLLBACK_COMPLETE'])['StackSummaries'] if x['DriftInformation']['StackDriftStatus']=='DRIFTED']
    return stacks
    
if __name__ == '__main__':
    ec2 = boto3.client('ec2',region_name='us-east-1')
    regions = [x['RegionName'] for x in ec2.describe_regions()['Regions']]
    print ('------- kick_detect_drift --------')
    detection_ids = [kick_detect_drift(x) for x in regions]
    print ('------- waiting for 1 minutes --------')
    sleep (60)
    print ('------- check_drift --------')
    drifted_stack = [check_drift(x) for x in regions]

    print(drifted_stack)
