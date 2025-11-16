# Exercise 1 : Call History

# Instructions
# Create a class called Phone. This class takes a parameter called phone_number. When instantiating an object create an attribute called call_history which value is an empty list.
# Add a method called call that takes both self and other_phone (i.e another Phone object) as parameters. The method should print a string stating who called who, and add this string to the phone’s call_history.
# Add a method called show_call_history. This method should print the call_history.
# Add another attribute called messages to your __init__() method which value is an empty list.
# Create a method called send_message which is similar to the call method. Each message should be saved as a dictionary with the following keys:
# to : the number of another Phone object
# from : your phone number (also a Phone object)
# content
# Create the following methods: show_outgoing_messages(self), show_incoming_messages(self), show_messages_from(self)
# Test your code !!!

class Phone:
    """
    Simulates a phone with history tracking for calls and messages.
    """
    def __init__(self, phone_number):
        """
        Initializes a Phone object with its unique number and empty history lists.

        :param phone_number: The unique identifier for the phone.
        """
        self.phone_number = phone_number
        # Stores strings describing calls made/received
        self.call_history = [] 
        # Stores dictionaries of messages sent/received
        self.messages = []     
        print(f"✅ Phone object created: {self.phone_number}")

    # --- Call Methods ---

    def call(self, other_phone):
        """
        Logs a call made from this phone to another Phone object.

        The call is logged in the history of both the caller and the receiver.

        :param other_phone: The Phone object being called.
        """
        call_string = f"📞 CALL: {self.phone_number} called {other_phone.phone_number}"
        print(call_string)
        
        # Log for the caller (outgoing)
        self.call_history.append(f"Made call to {other_phone.phone_number}")
        
        # Log for the receiver (incoming)
        other_phone.call_history.append(f"Received call from {self.phone_number}")

    def show_call_history(self):
        """
        Prints the complete call history for this phone.
        """
        print(f"\n--- 📞 Call History for {self.phone_number} ---")
        if self.call_history:
            for record in self.call_history:
                print(f"- {record}")
        else:
            print("No calls in history.")
        print("-----------------------------------")

    # --- Message Methods ---

    def send_message(self, other_phone, content):
        """
        Records a message sent from this phone to another Phone object.
        The message is saved as a dictionary in both phones' 'messages' attribute.

        :param other_phone: The recipient Phone object.
        :param content: The text content of the message.
        """
        message_record = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        
        # Add the record to the sender's history
        self.messages.append(message_record)
        
        # Add the record to the receiver's history
        other_phone.messages.append(message_record)
        
        print(f"✉️ SENT: From {self.phone_number} to {other_phone.phone_number}: '{content[:25]}...'")

    def show_outgoing_messages(self):
        """
        Prints all messages sent (outgoing) from this phone.
        """
        print(f"\n--- 📤 Outgoing Messages from {self.phone_number} ---")
        found = False
        for msg in self.messages:
            # An outgoing message is one where 'from' is this phone's number
            if msg['from'] == self.phone_number:
                print(f"TO: {msg['to']} | Content: {msg['content']}")
                found = True
        if not found:
            print("No outgoing messages found.")
        print("------------------------------------------")

    def show_incoming_messages(self):
        """
        Prints all messages received (incoming) by this phone.
        """
        print(f"\n--- 📥 Incoming Messages to {self.phone_number} ---")
        found = False
        for msg in self.messages:
            # An incoming message is one where 'to' is this phone's number
            if msg['to'] == self.phone_number:
                print(f"FROM: {msg['from']} | Content: {msg['content']}")
                found = True
        if not found:
            print("No incoming messages found.")
        print("------------------------------------------")

    def show_messages_from(self, source_phone_number):
        """
        Prints all messages received by this phone from a specific source number.

        :param source_phone_number: The number to filter messages by.
        """
        print(f"\n--- 🔎 Messages to {self.phone_number} FROM {source_phone_number} ---")
        found = False
        for msg in self.messages:
            # Filter by recipient AND sender
            if msg['to'] == self.phone_number and msg['from'] == source_phone_number:
                print(f"Content: {msg['content']}")
                found = True
        if not found:
            print(f"No messages received from {source_phone_number}.")
        print("-----------------------------------------------------")

# --- 🧪 Test Your Code !!! ---

print("\n====================================")
print("       PHOHE CLASS DEMONSTRATION")
print("====================================")

# 1. Create Phone Objects
p1 = Phone("111-222-3333")
p2 = Phone("444-555-6666")
p3 = Phone("777-888-9999")

# 2. Test the call method
print("\n\n--- Testing Calls ---")
p1.call(p2) # p1 calls p2
p2.call(p1) # p2 calls p1
p3.call(p1) # p3 calls p1

# 3. Test the show_call_history method
p1.show_call_history()
p2.show_call_history()
p3.show_call_history()

# 4. Test the send_message method
print("\n\n--- Testing Messages ---")
p1.send_message(p2, "Hello P2, are you available for a quick chat?")
p2.send_message(p1, "Yes, I am. What's up?")
p3.send_message(p1, "Remember the project deadline is Friday.")
p1.send_message(p3, "Thanks for the reminder!")
p2.send_message(p3, "Testing connection with P3.")

# 5. Test message display methods for P1 ("111-222-3333")
print("\n\n--- P1 Message History Analysis ---")
p1.show_outgoing_messages()
p1.show_incoming_messages()
p1.show_messages_from("444-555-6666") # Messages from P2
p1.show_messages_from("777-888-9999") # Messages from P3

# 6. Test message display methods for P3 ("777-888-9999")
print("\n\n--- P3 Message History Analysis ---")
p3.show_outgoing_messages()
p3.show_incoming_messages()
p3.show_messages_from("111-222-3333") # Messages from P1