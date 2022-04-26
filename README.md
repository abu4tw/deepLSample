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

<H2>##################################################################################</H2>

Use DeepL to translate the text in the clipboard and return it to the clipboard for use by third-party systems.

python 3.5 or above

System idea: Use DeepL core to translate the text from the clipboard into the corresponding country language. Put it back into the cut and paste version.

Functionality: Third party system, put the data to be translated into the clipboard, call and run this program deeplsample.exe --lang=EN-US After the data in the clipboard is translated, then paste it back into the third party system.

Supported languages Please refer to DeepL https://www.deepl.com/zh/docs-api/other-functions/listing-supported-languages/

=====================================================

pip install -r requirements.txt

use tool open deeplsample.py

Translator = deepl.Translator("Authentication Key") <-- Replace the authorization key with the authorization code from DeepL.

4. Test: First copy a pair of text to the clipboard, and run the default translation into English

5. After translation, Ctrl + V paste the translated text to see if it is correct.
