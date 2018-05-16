dict1 = {"name":"shu","age":23,"name":"zhang"}
print dict1["name"]
#Do not allow the same key to appear twice. If the same key is assigned twice during creation, the latter value will be remembered.


dict2 = {['Name']: 'Zara', 'Age': 7}
print "dict2['Name']: ", dict['Name']
#The keys must not be variable, so they can be used as numbers, strings, or tuples, so the list won't work.

test = {"a":"1","b":"2",True:"3",False:"4"}
print test

test1 = {0:"1",1:"2",True:"3",False:"4"}
print test1

#the value in the dictionary can use the type of boolean
# True defaults to 1,  False defaults to 0, and boolean types cannot be used if they contain 0 or 1.