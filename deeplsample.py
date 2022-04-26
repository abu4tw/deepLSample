# coding=utf8


import deepl
import argparse
import clipboard


#撿貼版
flow = clipboard.paste()
print(flow)

# #啟動傳入質 轉換語言
parser = argparse.ArgumentParser(description='Select translation language')
parser.add_argument('--lang', type=str, default = 'EN-US')
args = parser.parse_args()

lang = args.lang

print("To --> ", lang)

for line in open('dictionary.ini', "r", encoding='utf-8'):  # 设置文件对象并读取每一行文件
    re = line.split("||")  # 将每一行文件加入到list中
    flow = flow.replace(re[0], re[1].strip())


translator = deepl.Translator("******Authentication Key******")

#Single String
result = translator.translate_text(flow, target_lang=lang)
print(result)

clipboard.copy(str(result))
