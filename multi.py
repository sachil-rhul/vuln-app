import pickle,os

user_input = input("Enter filename: ")
with open(user_input, 'r') as file:  # Vulnerable to directory traversal
    content = file.read()

directory = input("Enter the directory to list: ")
command = f"ls {directory}"  # Vulnerable to Command Injection
os.system(command)

serialized_data = input("Enter serialized data: ")
deserialized_data = pickle.loads(serialized_data.encode('latin1'))  # Unsafe deserialization
