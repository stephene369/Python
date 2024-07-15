from __future__ import print_function


import json 
import urllib
import boto3
import datetime

print("Loading function ...")

def process_purchase(message,context) :

    print("Received message from step Functions  : ")
    print(message)

    response = {}
    response['TransationType'] = message['TransationType']
    response['Timestamp'] = datetime.datetime.now().strftime("%Y-%m-d %H-%M-%S")
    response['Message'] = "Hel from lambda land inside the ProcessPurchase function"

    return response