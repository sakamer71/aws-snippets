import boto3
client = boto3.client('sns')
resource = boto3.resource('sns')
topicname = 'test-topic3'
smsphone = '1-630-962-1199'
def create_sns_topic(topic):
    ## create SNS subscription
    response = client.create_topic(
        Name = topic
    )
    return response

def set_topic_displayname(arn,displayname):
    ## set a topic displayname (required for sms communication)
    topic = resource.Topic(arn)
    response = topic.set_attributes(
        AttributeName = 'DisplayName',
        AttributeValue = displayname
    )
    return response


def subscribe_to_topic(arn,protocol,endpoint):
    response = client.subscribe(
        TopicArn = arn,
        Protocol = protocol,
        Endpoint = endpoint
    )
    return response


def confirm_subscription(arn,requestid):
        topic = resource.Topic(arn)
        response = topic.confirm_subscription(
            Token = requestid
        )
        return response


print "Now creating new topic"
response = create_sns_topic(topicname)
arn = response['TopicArn']
print arn

print "Now setting topic displayname"
response = set_topic_displayname(arn,topicname)
print "Now subscribing to topic..."
response = subscribe_to_topic(arn,'sms',smsphone)
print response
token = response['ResponseMetadata']['RequestId']
print "Now trying to confirm subscription"
response = confirm_subscription(arn,token)
print response
