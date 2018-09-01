import nexmo

client = nexmo.Client(key='64fd0daa', secret='c094860ef6c90264')


response=client.send_message({
  'from': 'Alert',
  'to': '94784514723',
  'text': 'A text message alert from VmiT'
})
response=response['messages'][0]
if response['status']=='0':
  print 'Send message',response['message-id']

else:
  print 'Error: ',response['error-text']