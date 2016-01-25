import boto3
client = boto3.client('ses')

fromaddr = 'The SES Borg <stevenkamer@yahoo.com>'
toaddr = 'kamer@amazon.com'
print client.send_email(
        Source = fromaddr,
        Destination = {
            'ToAddresses':[toaddr,],
        },
        Message = {
            'Subject' : {
                'Data' : 'Hello test 1',
                },
            'Body' : {
                'Text' : {
                    'Data' : 'This is the body of my message'
                }
            }

}
)