import boto3
import botocore
import paramiko
import time

ec2 = boto3.resource('ec2', region_name='us-east-1')
instance = ec2.create_instances(
    ImageId = 'ami-0c94855ba95c71c99',
    MinCount = 1,
    MaxCount = 1,
    InstanceType = 't2.micro',
    KeyName = 'Ansible',
    SecurityGroupIds=[
        'sg-0a946195e26dcdd80',
    ],
)
print (instance[0].id)
instance[0].wait_until_running()           
instance[0].reload()
print (instance[0].public_ip_address)
time.sleep(10)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.load_system_host_keys()
client.connect(hostname=instance[0].public_ip_address, username="ec2-user", key_filename='C:/Users/Sonu_2/Downloads/Ansible.pem')
stdin, stdout, stderr = client.exec_command('sudo yum update -y')
print (stdout.readlines())
time.sleep(3)
stdin, stdout, stderr = client.exec_command('sudo yum install git -y')
print (stdout.readlines())
time.sleep(3)
stdin, stdout, stderr = client.exec_command('git clone https://github.com/dantso/aws-python.git')
print (stdout.readlines())
time.sleep(3)
stdin, stdout, stderr = client.exec_command('sudo bash ~/aws-python/flaskApp/shell.sh &')
print (stdout.readlines())
time.sleep(3)
stdin, stdout, stderr = client.exec_command('python ~/aws-python/flaskApp/app.py &')
print (stdout.readlines())
time.sleep(3)
#client.close()

print ("Finished")
