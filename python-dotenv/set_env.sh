#!/bin/bash

# .env ファイルを読み込み、各行を環境変数としてエクスポートする
while read -r line; do
  if [ -n "$line" ]; then
    export "$line"
  fi
done < .env