# DEBUG : 通常関心のない詳細な情報  【使用例】数の値など
# INFO : 処理の流れなどの情報  【使用例】プログラムの起動、データの読み込みなど
# WARNING : 警告情報   【使用例】異常な引数の型、ファイル不明など
# ERROR : プログラムのエラー  【使用例】ファイル書き込みエラー、接続タイムアウト
# CRITICAL : プログラムの重大なエラー  【使用例】セキュリティ侵害、サーバー障害など
### 開発中はDEBUG、運用中はINFOにするのが一般的 ###

# logger.debug("### __init__ ###")
# logger.debug('index - {} - {}'.format(type(index), index))


from logging import getLogger, Formatter, FileHandler, DEBUG, INFO

formatter = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler = FileHandler("./test.log")
file_handler.setFormatter(formatter)

main_logger = getLogger(__name__)
main_logger.addHandler(file_handler)
main_logger.setLevel(DEBUG)

main_logger.debug("debug message from main.py")
main_logger.info("info message from main.py")
main_logger.warning("warning message from main.py")

import sample
sample_logger = getLogger("sample")
sample_logger.addHandler(file_handler)
sample_logger.setLevel(INFO)

sample.do_something()