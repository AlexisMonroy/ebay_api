from ebaysdk.trading import Connection as Trading

api = Trading(config_file='myebay.yaml')
response = api.execute('GetUser', {})
print(response.dict())
print("\n\n\n")
print(response.reply)

#write response.dict() and response.reply to a notepad file:
with open('response_output/response.txt', 'w') as f:
    f.write(str(response.dict()))
    f.write("\n\n\n")
    f.write(str(response.reply))


