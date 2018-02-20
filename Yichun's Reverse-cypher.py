#http://www.codeskulptor.org/#user44_b8zZrWtPJ0_5.py
#written by Yichun Zhao
#purpose of this program: to decrypt message encrypted using ascii code

key = raw_input("key?")
encrypted = raw_input("encrypted message?")

print "<Yichun's reverse-cypher>"
print "key:", key
print "encrypted message:", encrypted

keyLength = len(key)
encryptedLength = len(encrypted)
    
keyIndex = 0
encryptedIndex = 0
original = ""
count = 0
    
while count < encryptedLength:
        
    keyValue = ord(key[keyIndex]) - 97
        
    keyIndex += 1
    keyIndex = keyIndex % len(key)
    
    encryptedValue = ord(encrypted[encryptedIndex]) - 97
    
    encryptedIndex += 1

    encryptedValue = encryptedValue - keyValue
    encryptedValue = encryptedValue % 26
        
    original += chr(encryptedValue + 97)
        
    count += 1
        
print "original message:", original