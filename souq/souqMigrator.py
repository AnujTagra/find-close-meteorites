#aws configure --profile="souqProfile" -> enter accessKey and secert access key
#pipenv install boto3
#pipenv run python souqMigrator.py

import boto3
import json

class ReceiveData:
    def __init__(self, asin, fnsku, iog, glProductGroupId):
        self.asin = asin
        self.fnsku = fnsku
        self.iog = iog
        self.glProductGroupId = glProductGroupId

session = boto3.Session(profile_name='souqProfile')
s3 = session.resource('s3')
bucketName="souqtest"

masterDataObject = s3.Object(bucketName, '02-11/shipment/masterShipmentRetail.json')
masterDataText = masterDataObject.get()['Body'].read().decode('utf-8')
masterDataDictList = json.loads(masterDataText)

masterDataHashMap = {}

for masterDataDict in masterDataDictList:
    masterDataHashMap[masterDataDict['SouqSku']] = ReceiveData(masterDataDict['Asin'], masterDataDict['FnSKU'], masterDataDict['IOG'], masterDataDict['GLProductGroupID'])

print("Master data hash Map")
for key in masterDataHashMap:
    print ("{} -> {}".format(key,masterDataHashMap[key].__dict__))


souqDataObject = s3.Object(bucketName, '02-11/souq/souqAddRetail.json')
souqDataText = souqDataObject.get()['Body'].read().decode('utf-8')
souqDataDictList = json.loads(souqDataText)

souqDataDictListSuccess =[]
souqDataDictListFailure =[]
for souqDataDict in souqDataDictList:
    if(masterDataHashMap.get(souqDataDict['SouqSku'],None) != None):
        souqDataDictListSuccess.append(souqDataDict)
    else:
        souqDataDictListFailure.append(souqDataDict)

print("\n\nSuccess records -")
print(souqDataDictListSuccess)

receiveSuccessFileName = "successReceiveRetail.json"
s3KeyForSuccess="02-11/receive/{}".format(receiveSuccessFileName)
with open(receiveSuccessFileName, 'w') as f:
    json.dump(souqDataDictListSuccess, f)

print("\n\nFailure records -")
print(souqDataDictListFailure)
receiveFailureFileName = "failureReceiveRetail.json"

s3KeyForFailure="02-11/receive/{}".format(receiveFailureFileName)
with open("failureReceiveRetail.json", 'w') as f:
    json.dump(souqDataDictListFailure, f)

print("\n\nUploading success file...")
s3.meta.client.upload_file(receiveSuccessFileName, bucketName, s3KeyForSuccess, ExtraArgs={'ContentType': 'text/plain'})
print("DONE")



print("\n\nUploading failure file...")
s3.meta.client.upload_file(receiveFailureFileName, bucketName, s3KeyForFailure, ExtraArgs={'ContentType': 'text/plain'})
print("DONE")
