# myPython_code

## grep
- grep -rin "思考プロセス" . | cut -c 1-500

## sed
- grep -rl DY . | xargs sed -i 's/DY/dy/g'    //DY→dy (カレントディレクトリ内の全ファイル)

## HDD空き容量
- sudo du -shc /home/* 

## その他
- pushd .   カレントディレクトリを保存
- popd       保存した場所に戻る