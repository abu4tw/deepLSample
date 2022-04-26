# deepLSample
利用DeepL來翻譯剪貼版裡的文字, 並再回傳剪貼版裡, 方便第三方程式利用.

python 3.5 以上

系統想法
從剪貼版裡的文字利用DeepL核心, 翻譯成對應的國家語言.再放回剪貼版裡

實用功能:
第三方系統, 將要翻譯的資料, 放到剪貼版, 調用並執行此程式
deeplsample.exe --lang=EN-US
剪貼版裡資料翻譯後, 再貼回第三方系統裡.

支援語言
請參考DeepL網站 
https://www.deepl.com/zh/docs-api/other-functions/listing-supported-languages/

=====================================================

1. pip install -r requirements.txt

2. use tool open deeplsample.py

3.translator = deepl.Translator("Authentication Key") <-- 將授權碼替換掉
授權碼請至DeepL網站申請..

4.測試 先複制一對文字到剪貼版, 執行默認是翻譯成英文

5.翻譯後, 再Ctrl + V貼上翻譯後的內文是否正確..
