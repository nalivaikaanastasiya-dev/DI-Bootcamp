class Phone:

    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        call_string = f" call: {self.phone_number} called {other_phone.phone_number}"
        print(call_string)
        self.call_history.append(call_string)
        other_phone.call_history.append(f" received: {self.phone_number} called {other_phone.phone_number}")

    def show_call_history(self):
        print(f"\nCall History for {self.phone_number}")
        if self.call_history:
            for record in self.call_history:
                print(f"- {record}")
        else:
            print("No calls in history.")

    def send_message(self, other_phone, content):
        "to": other_phone, phone_number,
        "from": self.phone_number,
        "content": content

        self.messages.append(message_record)
        other_phone.messages.append(message_record)
        print(f"sent: Message from {self.phone_number} to {other_phone.phone_number}: '{content[:20]}...'")

    def show_outgoing_messages(self):
        print(f"\nOutgoing Messages from {self.phone_number}")
        found = False
        for msg in self.messages:
            if msg['from'] == self.phone_number:
                print(f"to: {msg['to']} | Content: {msg['content']}")
                found = True
        if not found:
            print("No outgoing messages.")

    def show_incoming_messages(self):
        print(f"\nIncoming Messages to {self.phone_number}")
        found = False
        for msg in self.messages:
            if msg['to'] == self.phone_number:
                print(f"from: {msg['from']} | Content: {msg['content']}")
                found = True
        if not found:
            print("No incoming messages.")

    def show_messages_from(self, source_phone_number):
        print(f"\nMessages to {self.phone_number} from {source_phone_number}")
        found = False
        for msg in self.messages:
            if msg['to'] == self.phone_number and msg['from'] == source_phone_number:
                print(f"Content: {msg['content']}")
                found = True
        if not found:
            print(f"No messages received from {source_phone_number}.")




