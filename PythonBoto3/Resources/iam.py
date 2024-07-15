from typing import Any
from .Common import *
from .Common.policy import *

class Iam :
    def __init__(self) -> None:
        self.iam = boto3.client('iam')

        self.id = boto3.client('sts').get_caller_identity()['Account']

        print("iam client created ; id = ", self.id)

    def create_user(self,userName:str) :
        """create an iam user"""
        try : 
            response = self.iam.create_user(
                UserName = userName
            )
            pprint(response)
        except Exception as e :
            print(e)
    
    def list_users(self) :
        """list of users"""
        self.paginator  = self.iam.get_paginator("list_users")
        for response in self.paginator.paginate() :
            print(response)
    
    def get_list_users(self) :
        """get a list of users """
        users = []
        self.paginator  = self.iam.get_paginator("list_users")
        for response in self.paginator.paginate() :
            users.append(response)

        return users

    def update_user(self,name:str,new:str):
        """update user name """
        try : 
            self.iam.update_user(
                UserName=name ,
                NewUserName=new
            )
        except Exception as e : 
            print(e)
    

    def delete_user(self,name:str) :
        """delete an user"""
        try : 
            self.iam.delete_user(
                UserName = name
            )
        except Exception as e :
            print(e)

    def create_policy(self ,policyName:str ,policy:dict):
        """Create IAM Policy"""
        response = self.iam.create_policy(
            PolicyName = policyName,
            PolicyDocument = dumps(policy)
        )
        pprint(response)
    
    def get_policy(self,arn:str) :
        """Get IAM Policy"""
        try : 
            reponse = self.iam.get_policy(
                PolicyArn = arn
            )
            return reponse
        except Exception as e : 
            print(e)
    

    def create_role(self,name:str,policy:dict) :
        """Create a IAM RoelE"""
        try : 
            self.iam.create_role(
                RoleName = name, 
                AssumeRolePolicyDocument=dumps(policy)
            )
        except Exception as e :
            print(e)



    def attach_role_policy(self,arn:str,name:str) :
        """Attach a managed role policy"""
        try : 
            self.iam.attach_role_policy(
                PolicyArn=arn,
                RoleName=name
            )
        except Exception as e :
            print(e)
    

    def detach_role_policy(self,arn:str,name:str): 
        """Detach a managed role policy"""
        try : 
            self.iam.detach_role_policy(
                PolicyArn=arn,
                RoleName=name
            )
        except Exception as e :
            print(e)

    
    def create_access_key(self,user:str) :
        """Create access keys for a user"""
        try : 
            response = self.iam.create_access_key(
                UserName = user)
            return response
        except Exception as e :
            print(e)
    
    def list_users_access_key(self,user:str='') :
        """List a user's access keys"""
        if user:
            users = []
            paginator = self.iam.get_paginator('list_access_keys')
            for response in paginator.paginate(UserName=user) :
                users.append(response)
            return users
        else :
            users = []
            paginator = self.iam.get_paginator('list_access_keys')
            for response in paginator.paginate() :
                users.append(response)
            return users
    
    def get_access_key(self,KeyId:str):
        """Get the access key last used """
        try : 
            response = self.iam.get_access_key_last_used(
                AccessKeyId=KeyId)
            return response
        except Exception as e : print(e)


    def update_access_key_status(self,keyId:str,name:str,active:bool) : 
        """Update access key status """
        
        if active==True:status = "Active" 
        elif active == False :status="Inactive"
        else : status = None
        try : 
            self.iam.update_access_key(
                AccessKeyId=keyId,
                Status=status,
                UserName=name )
        except Exception as e : print(e)


    def delete_access_key(self,KeyId:str,user:str) :
        """Delete an access key"""

        self.iam.delete_access_key(
            AccessKeyId = KeyId,
            UserName = user)
        
    
    def list_server_certificates(self,) :
        """List your server certificates"""

        certificates = []
        paginator = self.iam.get_paginator('list_server_certificates')
        for response in paginator.paginate():
            print(response['ServerCertificateMetadataList'])
    

    def get_server_certificate(self,certificateName:str) :
        """Get a server certificate 
        certificateName=[MyWebsiteCert  , 
        MyAppCert  , WildcardCert , DevEnvironmentCert, BackupCert  ]
        """

        try : 
            response = self.iam.get_server_certificate(ServerCertificateName=certificateName)
            print(response)
        except Exception as e : print(e)


    def update_server_certificate(self,oldCertificate:str,newCertificate:str) :
        """ Update a server certificate """

        try : 
            self.iam.update_server_certificate(
                ServerCertificateName=oldCertificate,
                NewServerCertificateName=newCertificate)
        except Exception as e : print(e)

    
    def delete_server_certificate(self,certificateName:str) :
        """Delete a server certificate """

        try : 
            self.iam.delete_server_certificate(
                ServerCertificateName=certificateName)
        except Exception as e : print(e)

    
    def create_acount_alias(self,alias:str) :
        """Create an account alias """

        self.iam.create_account_alias(
            AccountAlias=alias
        )

    
    def list_account_alias(self) :
        """List an account alias"""

        paginator = self.iam.get_paginator('list_account_aliases')
        for response in paginator.paginate():
            print(response['AccountAliases'])
    

    def delete_account_alias(self,alias) :
        """Delete an account alias"""

        self.iam.delete_account_alias(
            AccountAlias=alias )
    
    def create_group(self,group_name,path=None) :
        if path :         
            response = self.s3.create_group(
                Path=path,GroupName=group_name)
        else :
            response = self.s3.create_group(
                GroupName=group_name)
        return response 
    
    def create_predefined_role(self,policy:str,name:str=None) :
        """Policy: AWSLambdaBasicExecutionPolicy , 
        InvokeOtherLambdaPolicy,
        """

        if name==None: name=policy 
        try : 
            self.iam.create_role(
                RoleName = name, 
                AssumeRolePolicyDocument=dumps( RolePolicy[policy] )
            )
        except Exception as e :
            print(e)

    def put_role_policy(self,Rolename,Policyname,Policydocument):
        self.iam.put_role_policy(
            RoleName=Rolename,
            PolicyName=Policyname,
            PolicyDocument=dumps(Policydocument)
        )


        
    
    
    