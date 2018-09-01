import nexmo
import pyttsx

client = nexmo.Client(key='64fd0daa', secret='c094860ef6c90264')
engine = pyttsx.init()
engine.say('To whom! do you call? ')
engine.runAndWait()

number=raw_input("Enter number");

engine = pyttsx.init()
engine.say('Please tell me the message you want to send ')
engine.runAndWait()

message=raw_input("Enter message ")

response=client.send_message({
  'from': 'Alert',
  'to': number,
  'text': message
})
response=response['messages'][0]
if response['status']=='0':
  print 'Send message',response['message-id']

else:
  print 'Error: ',response['error-text']