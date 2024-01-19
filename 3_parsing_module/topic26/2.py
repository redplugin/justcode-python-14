import json

data = {"name": "scdc", "description": "test"}

# print(data)
# print(type(data))
# json_data = json.dumps(data)
# print("===============")
# print(json_data)
# print(type(json_data))

json_data_test = '{"test": "name", "type": "sdfdf"}'
print(type(json_data_test))
print("============")

json_dict_data = json.loads(json_data_test)
print(json_dict_data)
print(type(json_dict_data))
