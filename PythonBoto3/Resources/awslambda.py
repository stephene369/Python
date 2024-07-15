from .Common import * 
from .Common.zipper import Zipper

class Lamnda :
    def __init__(self , region:str=None) -> None:
        self.region = region
        self.lamb = boto3.client('lambda',region_name=self.region)
        self.id = boto3.client('sts').get_caller_identity()['Account']

        print("Lambda client created for id = ", self.id)

    def create_function(self,name:str,description:str,
                bucket:str,key:str,
                role:str,runtime:str,
                handler:str) :
        self.lamb.create_function(
            Code={
                'S3Bucket': bucket,
                'S3Key': key 
            },
            FunctionName=name,
            Description=description,
            Handler=handler,
            Role=role,
            Publish=True,
            Runtime=runtime
        )
    
    def create_function_from_zip(self,name:str,
            description:str,role:str,runtime:str,
            filename:str,handler:str) :
        try : 
            with open(filename,'rb') as  file :
                bytes_content = file.read()

                self.lamb.create_function(
                    Code={
                        'ZipFile':bytes_content
                    },
                    FunctionName=name,
                    Description=description,
                    Handler=handler,
                    Role=role,
                    Publish=True,
                    Runtime=runtime 
                )        
        except Exception as e : print(e)

    def create_function_from_path(self,name:str,
            description:str,role:str,runtime:str,
            filename:str,handler:str) :
        z = Zipper(filename)
        filename = z.zippath
        try : 
            with open(filename,'rb') as  file :
                bytes_content = file.read()

                self.lamb.create_function(
                    Code={
                        'ZipFile':bytes_content
                    },
                    FunctionName=name,
                    Description=description,
                    Handler=handler,
                    Role=role,
                    Publish=True,
                    Runtime=runtime 
                )        
        except Exception as e : print(e)



    def list_functions(self) -> dict :
        return self.lamb.list_functions()

    def list_functions_name(self) :
        response = self.lamb.list_functions()
        name = []

        Funcs = response["Functions"]
        for funcs in Funcs :
            name.append( funcs['FunctionName'] )
        
        return name

    def list_functions_attributs(self,attributs:list) :
        """ 
        Attributs : ['FunctionName', 'FunctionArn', 'Runtime', 'Role', 'Handler', 'CodeSize', 'Description', 'Timeout', 'MemorySize', 'LastModified', 'CodeSha256', 'Version', 'TracingConfig', 'RevisionId', 'PackageType', 'Architectures', 'EphemeralStorage', 'SnapStart']
        """
        response = self.lamb.list_functions()

        Funcs = response["Functions"]
        response = {}
        for funcs in Funcs :
            name = funcs['FunctionName'] 
            print( funcs.keys() )
            response.update( { name:{} } )
            
            for attribut in attributs :
                att = funcs[attribut ]
                response[name].update( { attribut:att } )
        
        return response
    
    def get_region(self , function_name:str) :
        return self.lamb.get_function_configuration(
            FunctionName=function_name
        )
    
    def update_function_vpc(self,funtion_name:str ,  
           SubnetIds:list,SecurityGroupIds:list ) :

        return self.lamb. update_function_configuration(
            FunctionName=funtion_name, 
            VpcConfig= {
                "SubnetIds":SubnetIds , 
                'SecurityGroupIds':SecurityGroupIds
            }
            
        )

    