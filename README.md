# GDGs/GDGoC Chuo p5.js workshop

2026年3月29日\
[v76nl.github.io/gdgs-p5-workshop](https://v76nl.github.io/gdgs-p5-workshop/)

## Routine
1. docs/ にマークダウンファイル作成
2. mkdocs.ymlにそのファイル名を記載
3. serveコマンドでビルド・確認
4. deployコマンドでデプロイ

## Usage
- 書いたマークダウンファイルをhtmlにする \
    `python run.py build`
- ローカルサーバーを立ち上げる \
    `python run.py serve`
- gh-pagesブランチをgithub pagesとしてdeployする \
    `python run.py deploy`