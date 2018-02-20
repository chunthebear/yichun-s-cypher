#http://www.codeskulptor.org/#user44_8p1H94G2M5_11.py
#written by Yichun Zhao
#purpose of this program: to encrypt message using ascii code

#ask user for input
key = raw_input("key?")
message = raw_input("message?")

print "<Yichun's cypher>"
print "key:", key
print "message:", message

keyLength = len(key)
messageLength = len(message)
    
keyIndex = 0
messageIndex = 0
encrypted = ""
count = 0
    
while count < messageLength:
    
    #minus 97 to change the range of ascii codes for letters to 0 to 26
    #use ord to convert letter to ascii code
    keyValue = ord(key[keyIndex]) - 97
    
    #move in to next letter of the key
    keyIndex += 1
    
    #use modulus so that the index can start over again from position 0
    #after reaching the maximum position if the key is shorter then the message
    keyIndex = keyIndex % len(key)
    
    
    messageValue = ord(message[messageIndex]) - 97
    
    #move in to next letter of the message
    messageIndex += 1
    
    
    encryValue = keyValue + messageValue
    
    #use modulus so that 
    encryValue = encryValue % 26
    
    #keep adding the encrypted letter to the string encrypted
    #plus 97 to change back to the range of ascii codes for letters to 97 to 122
    #use chr to convert ascii code to letter
    encrypted += chr(encryValue + 97)
        
    count += 1
        
print "encrypted message:", encrypted
