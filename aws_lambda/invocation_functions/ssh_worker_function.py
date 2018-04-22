import boto3
import paramiko


def worker_handler(event, context):
    s3_client = boto3.client('s3', 'ap-south-1')
    s3_client.download_file('prax-bucket',
                            'keys/EC2SouthKP.pem',
                            '/tmp/EC2SouthKP.pem')

    key = paramiko.RSAKey.from_private_key_file('/tmp/EC2SouthKP.pem')
    print("key = {0} ".format(key))
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    host = event['IP']
    print("Connecting to host: {0}".format(host))
    client.connect(hostname=host, username="ec2-user", pkey=key)
    print("Connected to {0}".format(host))

    commands = [
            """aws s3 cp s3://prax-bucket/scripts/HelloWorld.sh 
                               /home/ec2-user/HelloWorld.sh""",
            "chmod 700 /home/ec2-user/HelloWorld.sh",
            "/home/ec2-user/HelloWorld.sh"
            ]

    for command in commands:
        print("Executing {}".format(command))
        stdin, stdout, stderr = client.execute(command)

        print(stdout.read())
        print(stderr.read())

    return 
    {
            'message': """Script execution completed. 
                         See Cloudwatch logs for complete output"""
            } 



