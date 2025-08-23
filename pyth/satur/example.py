
# import json

path = "C:/Users/HP/OneDrive/Desktop/Lang/pyth/satur/users.csv"


# data = {
#     "name" : "anish",
#     "age" : 22
# }


# with open(path , 'w') as f:
#     json.dump(data , f , indent= 2 )

# with open(path,'r') as f :
#     load = json.load(f)
#     print(load)


# email_args = json.dumps({"table" : "User",
#                          "ingstion_date": "date",
#                          "type" : "Transformation"})

# arguments = {"args" : email_args}


# str = json.loads(email_args)

# print(str)



# pd.json_normalize()


# dump -> files -> write
# dumps -> String -> API

# load -> file JSON reading
# loads -> String JSON reading

# data = [
#         {"id": 1, "name": {"first": "Coleen", "last": "Volk"}},
#         {"name": {"given": "Mark", "family": "Regner"}},
#         {"id": 2, "name": "Faye Raker"},
#     ]

# df = pd.json_normalize(data).fillna(0.0)
# df.dropna()

# print(df)


import pandas as pd
import json

with open(path,'r') as f:
    df = pd.read_csv(f)

# data = df['history']

# data = json.load(data)
df['history'] = df['history'].apply(json.loads)

h_title = df['history'].apply(pd.Series)
# print(h_title)

del df['history']

df = pd.concat([df,h_title],axis=1) # axis=1
print(df)
    

