"""
@Author: Rikesh Chhetri
@Date: 2021-09-01 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-09-01 10:03:30
@Title : Program Aim cretaing EC2 instance using boto3 library.
"""

# Lets create EC2 instances using Python BOTO3
import boto3
from loghandler import logger

def create_ec2_instance():
    """
    MaxCount=1, # Keep the max count to 1, unless you have a requirement to increase it
    InstanceType="t2.micro", # Change it as per your need, But use the Free tier one
    KeyName="ec2-key" # Change it to the name of the key you have.
    :return: Creates the EC2 instance.
    """
    try:
        print ("Creating EC2 instance")
        ec2_resource = boto3.client("ec2")
        ec2_resource.run_instances(
            ImageId="ami-0c1a7f89451184c8b",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName="rikesh_mumbai_ec2"
        )
    except Exception as e:
        print(e)


def describe_ec2_instance():
    """
    Description:
        This method is used for getting instance id.
       
    """
    try:
        print ("Describing EC2 instance")
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
        return str(resource_ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
    except Exception as e:
        print(e)


def reboot_ec2_instance():
    """
    Description:
        This method is used for rebooting instance
       
    """
    try:
        print ("Reboot EC2 instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.reboot_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)


def stop_ec2_instance():
    """
    Description:
        This method is used for stopping instance
       
    """
    try:
        print ("Stop EC2 instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.stop_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)


def start_ec2_instance():
    """
    Description:
        This method is used for statring  instance
       
    """
    try:
        print ("Start EC2 instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.start_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)


def terminate_ec2_instance():
    """
    Description:
        This method is used for deleting instance
       
    """
    try:
        print ("Terminate EC2 instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.terminate_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)


# create_ec2_instance()
# describe_ec2_instance()
# reboot_ec2_instance()
# stop_ec2_instance()
# start_ec2_instance()
# terminate_ec2_instance()