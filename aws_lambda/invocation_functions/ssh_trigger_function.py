# Function to trigger worker lambda function to execute a shell script for each ec2 host
import boto3


def trigger_handler(event, context):
    # Get IP Addresses of EC2 instance
    client = boto3.client('ec2')
    instDict = client.describe_instances(
                    Filters=[{'Name': 'tag:Environment', 'Values':['Dev']}])
    print("hello")
    hostList = []
    for r in instDict['Reservations']:
        for inst in r['Instances']:
            hostList.append(inst['PublicIpAddress'])

    print(hostList)
    # invoke worker function for each IP Address

    client = boto3.client('lambda')
    for host in hostList:
        print("invoking worker_function on host ".format(host))
        invokeResponse = client.invoke(
                FunctionName='ssh_worker_function',
                InvocationType='Event',
                LogType='Tail',
                Payload='{"IP":"'+host+'"}'
                )
        print(invokeResponse)

    return {'message': "Trigger function completed"}
