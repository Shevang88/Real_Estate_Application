import json
aJSON='sdsd'
#parsing to object(dict)
a=json.loads(aJSON)
print(type(a))

b={"one":1,"two":2,"three":3,"four":4}
#object(dict) to string
bJSON=json.dumps(b)
print(type(bJSON))