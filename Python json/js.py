import json
x = open('JSON.json')
data = json.load(x)
Interface = '''
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
'''
print(Interface)
for i in data['imdata']:
    print("{DN:50}{Speed:>30}{MTU:>6}".format(DN = i['l1PhysIf']['attributes']['dn'], Speed = i['l1PhysIf']['attributes']['speed'], MTU = i['l1PhysIf']['attributes']['mtu']))