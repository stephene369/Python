from Session.session import Session
from Resources.iam import Iam
from Resources.s3 import S3
from Resources.awslambda import Lamnda as Lamb
from pprint import pprint
import boto3

#iam.create_group("tring_group")
#session = Session(id="AKIAVNEMEULAV4FYREKX",key="nGjnS93VJ+wT6qIgwzw83WQQVrH2O24EHQoXPIf7",region=None )
#session.Sign_In()

#boto3.Session(aws_access_key_id="AKIAVNEMEULAV4FYREKX",aws_secret_access_key="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")

lamb = Lamb()
#lamb.create_function_from_path(name="Invoker",description="Fonction Inkateur",role="arn:aws:iam::371808576193:role/InvokeOtherLambdaRole",runtime="python3.8",filename="D:\Projects\Python\PythonBoto3\Functions\Invoker.py",handler="Invoker.lambda_handler" )


r = lamb.list_functions_name()
pprint(r)


pprint(lamb.update_function_vpc(funtion_name="ToInvoke" ,
	SubnetIds=["subnet-041eb9d4f5838af58"],
    SecurityGroupIds=["sg-08988f9b1654619f0"] )  )
#pprint(lamb.get_region('ToInvoke')['ResponseMetadata']['HTTPHeaders']['x-amz-function-region'])

