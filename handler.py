import boto3
from boto3.dynamodb.conditions import Key
from baseDAO import BaseDAO
import random
from datetime import datetime
import json
 
dao = BaseDAO('monitor-jpg-ppw')
global nomearquivo

def handlerCreateObject(event, context):
    for i in event['Records']:
        nomearquivo = i.get('s3').get('object').get('key')
    dao.put_item({'nomearquivo':nomearquivo, 'ativo':True})
    print(nomearquivo)
def handlerDeleteObject(event, context):
    for i in event['Records']:
        nomearquivo = i.get('s3').get('object').get('key')
    dao.put_item({'nomearquivo':nomearquivo, 'ativo':False})
    print(nomearquivo)
