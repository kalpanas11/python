import boto3


# ecr repository to hold the docker image
ecr_client = boto3.client('ecr', region_name='us-east-1',
                            aws_access_key_id=access_key_id,
                            aws_secret_access_key=secret_access_key)
repo_name = "my-first-cloud-native-repo"
response = ecr_client.create_repository(repositoryName=repo_name)
repositoryUri = response['repository']['repositoryUri']
print(repositoryUri)
