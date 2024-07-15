import boto3
import subprocess as sb

class Session :
    def __init__(self , id:str,key:str,region:str=None) :
        self.key_id = id 
        self.access_key = key 
        self.region = region
    
    def Sign_In(self) :
        if self.region : 
            self.session = boto3.Session(
                aws_access_key_id=self.key_id,
                aws_secret_access_key=self.access_key,
                region_name=self.region
                )
        else : 
            self.session = boto3.Session(
                aws_access_key_id=self.key_id,
                aws_secret_access_key=self.access_key
                )
    
