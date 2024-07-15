from json import dumps,load
import boto3

boto3.Session(aws_access_key_id="AKIAVNEMEULAV4FYREKX",aws_secret_access_key="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")
client = boto3.client('lambda')


def lambda_handler(event, context):
	inputForInvoker = {'CustumerId': '123', 'Amount': 50 }

	response = client.invoke(
		FunctionName='arn:aws:lambda:us-east-1:371808576193:function:ToInvoke',
		InvocationType='RequestResponse', # Event
		Payload=dumps(inputForInvoker)
		)

	responseJson = load(response['Payload'])

	print('\n')
	print(responseJson)
	print('\n')

