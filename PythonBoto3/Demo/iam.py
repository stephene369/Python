import boto3 
from Session.session import Session
from Resources.iam import Iam
import subprocess as sb

session = Session(
    id="AKIAVNEMEULAQ2SOU4UP",
    key="HGJEKeHEAToHVvBLRkI2lfnplBaJ2Wo9Fy2wblEA",
    region=None
)
session.Sign_In()

### Create IAM CLIENT :


iam = Iam()

"""
iam.list_users()
users = iam.get_list_users()
iam.update_user("Elma","Stacy")


trust_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "ec2.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
iam.create_role(
    name="MyEc2Role",
    policy=trust_policy
)


policy_name = 'MyExamplePolicy'
policy_document = {
    "Version": "2012-10-17",
    "Statement": [{
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::example-bucket"}]}
iam.create_policy(
    "MyExamplePolicy3",
    policy_document)


iam.get_policy(
    arn='arn:aws:iam::aws:policy/AWSLambdaExecute'
)['Policy']
iam.get_policy(
    arn='arn:aws:iam::371808576193:policy/MyExamplePolicy3'
)['Policy']


iam.attach_role_policy(
    arn="arn:aws:iam::371808576193:policy/MyExamplePolicy3" ,
    name="MyEc2Role")

iam.create_access_key("Elma2")
iam.list_users_access_key()
iam.list_users_access_key(user="Elma2")
iam.update_access_key_status(keyId="AKIAVNEMEULAX5OBHMXI",name="Elma2",active=False)

"""
