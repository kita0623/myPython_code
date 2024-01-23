# .envファイルをロードする
from dotenv import load_dotenv
load_dotenv()
# load_dotenv(verbose=True, dotenv_path='/path/to/.env') # .envのパスを指定する場合

import os
userName = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
print(userName)
print(password)