def show_messages(messages):
    for message in messages:
        msg = f"{message.title()}"
        print(msg)

messages = ['hello, world', 'n+1', 'object-oriented programming', 'functional programming']
show_messages(messages[:])
show_messages(messages)

def send_message(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print('Sending message, shortly')
        sent_messages.append(current_message)

def show_sent_mesages(sent_messages):
    print("The message is as follows: ")
    for message in sent_messages:
        msg = f"{message.title()}"
        print(msg)


messages = ['hello, world', 'n+1', 'object-oriented programming', 'functional programming']
sent_messages = []

send_message(messages, sent_messages)
show_sent_mesages(sent_messages)