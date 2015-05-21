#-*-encoding:utf-8-*-

import json
f=file('ccc.json')
jsonobj=json.load(f)
print jsonobj[0][0]
f.close


#s = json.loads('{"name":"test", "type":{"name":"seq", "parameter":["1", "2"]}}')

#print s.keys()

#[["username","guibiaob"],["password",123]]