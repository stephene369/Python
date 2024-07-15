import json 
import uuid 

def lambda_handler(event , context) :
    custumerId = event["CustumerId"] 

    transactionId = str(uuid.uuid1())

    return {
        "CustumerId":custumerId , 
        "Sucsess":"True",
        "TransactionId":transactionId,
    }

