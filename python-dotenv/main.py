# .envファイルをロードする
from dotenv import load_dotenv
load_dotenv()

import os
userName = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
print(userName)
print(password)