# 建立一个名为zh.json的文件，文件里面每一个字典包含'image_id'和'caption'，每一个'image_id'里写的内容是'./ESR-F'的txt文件的文件名，'caption'是对应txt文件里的内容。

# 这里，把 encode == "utf-8"删掉，另一个什么也删掉，这样，才能保障zh3.json里面的文件是Unicode编码。
import os
import json

def read_txt_files(folder_path):
    txt_files_data = []
    for file in os.listdir(folder_path):
        if file.endswith('.txt'):
            with open(os.path.join(folder_path, file), 'r', encoding='utf-8') as f:
                content = f.read()
                txt_files_data.append({'image_id': file, 'caption': content})
    return txt_files_data

def save_to_json(data, json_file):
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)

folder_path = './denggao-caption'
json_file = 'zh3.json'

txt_files_data = read_txt_files(folder_path)
save_to_json(txt_files_data, json_file)
