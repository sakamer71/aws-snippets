import boto3
resource = boto3.resource('sns')
arn = 'arn:aws:sns:us-east-1:473303284226:test-topic3'
token = '2336412f37fb687f5d51e6e241d7700bdc2fd530312002c16ff522664ff1f7aecbf654c69a9b0449629404842e73d288e526d982ffe00c2c3d7548537c68b37d0189ee86bf386c9b3c9bc868c3a95d39237bf716912aabde5d713ce2fad166cea2ddd48c7c23474765a71bab32af47eb'

def confirm_subscription(arn,token):
        topic = resource.Topic(arn)
        response = topic.confirm_subscription(
            Token = token
        )
        return response

print confirm_subscription(arn,token)