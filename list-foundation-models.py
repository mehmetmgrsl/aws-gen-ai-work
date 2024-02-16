import boto3
import json

bedrock = boto3.client(service_name='bedrock', region_name='eu-central-1')

listModels = bedrock.list_foundation_models(byProvider='Amazon')
print("\n".join(list(map(lambda x: f"{x['modelName']} : { x['modelId'] }", listModels['modelSummaries']))))