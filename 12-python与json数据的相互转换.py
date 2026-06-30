# 可以导入json包
import json

# 准备符合 json 格式要求的 python 数据
python_data = [{"name": "John", "age": 25},
        {"name": "Michael", "age": 26}, ]

# 通过json.dumps(data)将 python 数转换成 json 数据
json_data = json.dumps(python_data) # 注意：返回值类型是 str
print(type(json_data)) # <class 'str'>
print(json_data)

# 通过json.loads(data)将 json 数转换成 python 数据
python_data1 = json.loads(json_data)
print(type(python_data1)) # <class 'list'>
print(python_data1)