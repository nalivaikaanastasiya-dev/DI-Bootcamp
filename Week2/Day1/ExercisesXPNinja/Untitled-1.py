class Phone:
    
    def __init__(self, phone_number):
        """
        Initializes a Phone object.

        :param phone_number: The unique number of the phone.
        """
        self.phone_number = phone_number
        # Attribute to store call records (strings)
        self.call_history = []
        # Attribute to store message records (dictionaries)
        self.messages = []

    def call(self, other_phone):
        """
        Records a call made from this phone to another Phone object.

        :param other_phone: The Phone object being called.
        """
        call_string = f"📞 CALL: {self.phone_number} called {other_phone.phone_number}"
        print(call_string)
        self.call_history.append(call_string)
        # Also add the call to the other phone's history for a complete record
        other_phone.call_history.append(f"📞 RECEIVED: {self.phone_number} called {other_phone.phone_number}")

    def show_call_history(self):
        """
        Prints the complete call history for this phone.
        """
        print(f"\n--- Call History for {self.phone_number} ---")
        if self.call_history:
            for record in self.call_history:
                print(f"- {record}")
        else:
            print("No calls in history.")
        print("-----------------------------------")

    def send_message(self, other_phone, content):
        """
        Records a message sent from this phone to another Phone object.

        :param other_phone: The recipient Phone object.
        :param content: The content of the message (string).
        """
        message_record = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        
        # Add to the sender's (outgoing) message list
        self.messages.append(message_record)
        
        # Add to the receiver's (incoming) message list
        other_phone.messages.append(message_record)
        
        print(f"✉️ SENT: Message from {self.phone_number} to {other_phone.phone_number}: '{content[:20]}...'")

    def show_outgoing_messages(self):
        """
        Prints all messages sent from this phone.
        """
        print(f"\n--- Outgoing Messages from {self.phone_number} ---")
        found = False
        for msg in self.messages:
            # Check if this phone is the sender ('from')
            if msg['from'] == self.phone_number:
                print(f"TO: {msg['to']} | Content: {msg['content']}")
                found = True
        if not found:
            print("No outgoing messages.")
        print("------------------------------------------")

    def show_incoming_messages(self):
        """
        Prints all messages received by this phone.
        """
        print(f"\n--- Incoming Messages to {self.phone_number} ---")
        found = False
        for msg in self.messages:
            # Check if this phone is the recipient ('to')
            if msg['to'] == self.phone_number:
                print(f"FROM: {msg['from']} | Content: {msg['content']}")
                found = True
        if not found:
            print("No incoming messages.")
        print("------------------------------------------")

    def show_messages_from(self, source_phone_number):
        """
        Prints all messages received by this phone from a specific source number.

        :param source_phone_number: The number to filter messages by.
        """
        print(f"\n--- Messages to {self.phone_number} FROM {source_phone_number} ---")
        found = False
        for msg in self.messages:
            if msg['to'] == self.phone_number and msg['from'] == source_phone_number:
                print(f"Content: {msg['content']}")
                found = True
        if not found:
            print(f"No messages received from {source_phone_number}.")
        print("-----------------------------------------------------")

phone_a = Phone("123-456-7890")
phone_b = Phone("987-654-3210")
phone_c = Phone("555-111-2222")

print("--- Initial Actions ---")

phone_a.call(phone_b)
phone_b.call(phone_c)
phone_a.call(phone_c)

phone_a.send_message(phone_b, "Hey B, what's up?")
phone_b.send_message(phone_a, "Not much, just coding a Phone class!")
phone_c.send_message(phone_a, "Remember our meeting tomorrow.")
phone_a.send_message(phone_c, "Got it, see you then!")
phone_c.send_message(phone_b, "Test message.")

phone_a.show_call_history()
phone_b.show_call_history()
phone_c.show_call_history()

phone_a.show_outgoing_messages()
phone_a.show_incoming_messages()
phone_a.show_messages_from("987-654-3210")
phone_a.show_messages_from("555-111-2222")