from .Common import * 
from boto3.s3.transfer import TransferConfig

class S3 :
    def __init__(self,region:str) -> None:
        self.s3 = boto3.client('s3',region_name=region)
        print("S3 new client create in : ", region)

    def create_bucket(self,bucket_name:str,region:str=None):
        """Create bucket in a region """
        try : 
            if region :
                s3 = boto3.client('s3',region_name=region)
                location = {'LocationConstraint': region}
                s3.create_bucket(Bucket=bucket_name,
                        CreateBucketConfiguration=location)
                
            else :
                self.s3.create_bucket(Bucket=bucket_name)
        except Exception as e : print(e)
    
    def list_buckets(self) :
        response = self.s3.list_buckets()
        buckets = []
        for bucket in response['Buckets'] :
            buckets.append( bucket['Name'] )
            
        return buckets

    def upload_file(self,file_name:str,bucket:str,object_name:str=None) :
        """
        Upload file in a spicific bucket 
        filename : path of file 
        bucket : the specific bucket 
        object name : the name of the object when upload in buckets
        """

        if object_name==None :
            object_name = Path(file_name).name
        try : 
            response = self.s3.upload_file(
                file_name,bucket,object_name
            )
        except Exception as e : print(e)

    def upload_file_obj(self,buffered,bucket:str,object_name:str) :
        """Upload file as a from bianaire object || BufferedReader
            ------------------------------------
            with open("FILE_NAME", "rb") as f:
                s3.upload_fileobj(f, "BUCKET_NAME", "OBJECT_NAME")
        """

        try : 
            self.s3.upload_fileobj(buffered,bucket,object_name)
        except Exception as e : print(e)


    def download_file(self,bucket:str,object_name:str,file_name:str,config=None):
        """Downloading files 
            -----------

        config = TransferConfig(max_concurrency=5)
                 
         """
        try : 
            if config : 
                self.s3.download_file(
                    bucket,object_name,file_name,
                    Config=config)
            else :
                self.s3.download_file(
                    bucket,object_name,file_name)
        except Exception as e : print(e)


    def download_fileobj(self,bucket:str,object_name:str,buffered) :
        """Download objet in Buffered 
        -----------
        with open('FILE_NAME', 'wb') as f:
            s3.download_fileobj('BUCKET_NAME', 'OBJECT_NAME', f)
        """

        try : 
            self.s3.download_fileobj(bucket,object_name,buffered)
        except Exception as e : print(e)

    def multipart_transfers(self,bucket:str,object_name:str,file_name:str,size:int) :
        """Multipart transfers
            ----------- 
            Multipart transfers occur when the file size exceeds the value of the multipart_threshold attribute.

            GB = 1024 ** 3
            config = TransferConfig(multipart_threshold=5*GB)
            s3.upload_file('FILE_NAME', 'BUCKET_NAME', 'OBJECT_NAME', Config=config)
            """
        try : 
            config = TransferConfig(multipart_threshold=size)
            self.s3.download_file( bucket, object_name, file_name,
                Config=config)
        except Exception as e : print(e)


    def generate_presigned_url(self,bucket,object_name,
                            kind:str="get_object",
                            expiration:int=1800.4) :
        """
        Presigned URLs
        -------
        A user who does not have AWS credentials or permission to 
        access an S3 object can be granted temporary access by 
        using a presigned URL.
        parameter = {'Bucket': bucket_name,'Key': object_name}

        kind : get_object , s3:GetObject , 
        -------------------

        """
        parameter={'Bucket': bucket,'Key': object_name}
        try : 
            response = self.s3.generate_presigned_url(
                kind,
                Params=parameter,ExpiresIn=expiration)

            print(response)
            return response
        except Exception as e : print(e)

    def put_object(self,bucket_name:str,object_name:str) :
        """Create an object in aws bucket"""
        try : 
            self.s3.put_object(Bucket=bucket_name,Key=object_name)
        except Exception as e : print(e)
    
    def put_bucket_policy(self,bucket_name:str,policy:dict) :
        try : 
            response = self.s3.put_bucket_policy(Bucket=bucket_name,
                            Policy=dumps(policy))
            print(response)
        except Exception as e : print(e)

    def get_public_access_block(self,bucket_name:str) :
        try : 
            response = self.s3.get_public_access_block(
                Bucket=bucket_name)
            return response
        except Exception as e : print(e)

        
    def delete_public_access_block(self,bucket_name:str) :
        try :
            response = self.s3.delete_public_access_block(
                Bucket=bucket_name)
            return response
        except Exception as e : print(e)

    def public_access_block_config(self) :
        """Return a Public Access Block Configuration"""
        config ={
                'BlockPublicAcls': True,
                'IgnorePublicAcls': True,
                'BlockPublicPolicy': True,
                'RestrictPublicBuckets': True
            }
        return config
        
    def put_public_access_block(self,bucket_name:str,config:dict) :
        """ Put a Public Access Block """ 
        response =self.s3.put_public_access_block(
            Bucket=bucket_name,
            #ContentMD5='string',
            #ChecksumAlgorithm='CRC32'|'CRC32C'|'SHA1'|'SHA256',
            PublicAccessBlockConfiguration=config,
            #ExpectedBucketOwner='string'
        )
        return response
                
    def public_policy_policy(self,bucket_name:str) :
        public_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid":"AllAccess",
                    "Effect": "Allow",
                    "Principal": "*",
                    "Action":"s3:*",
                    "Resource": [
                        f"arn:aws:s3:::{bucket_name}/*",
                        f"arn:aws:s3:::{bucket_name}"
                    ],
                    "Principal": "*"
                }
            ]
        }
        return public_policy
    
    def get_bucket_policy(self,bucket_name:str) :
        try : 
            response = self.s3.get_bucket_policy(
                Bucket=bucket_name )
            return response
        except Exception as e : print(e)

    def get_bucket_acl(self,bucket_name:str) :
        try : 
            response = self.s3.get_bucket_acl(
                Bucket=bucket_name )
            return response
        except Exception as e : print(e)
    
    def delete_bucket_policy(self,bucket_name:str) :
        try :
            response = self.s3.delete_bucket_policy(
                Bucket=bucket_name)
            return response
        except Exception as e : print(e)
