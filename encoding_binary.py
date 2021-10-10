import base64

# 'rb' = reading a binary file
with open('7EA0B5.png', 'rb') as binary_file:
    # read() method = get all data in file into binary_file_data variable
    binary_file_data = binary_file.read()
    base64_encoded_data = base64.b64encode(binary_file_data)
    base64_message = base64_encoded_data.decode('utf-8') 
    
    print(base64_message)
