# gdgs p5 workshop

2026年3月29日, GDGs Chuo, p5.js workshop

- docs/ にマークダウンファイル作って、mkdocs.ymlにそのファイル名足して、serveで確認して、deployでv76nl.github.io/gdgs-p5-workshop にデプロイ

## つかいかた
- 書いたマークダウンファイルをhtmlにする \
    `python run.py build`
- ローカルサーバーを立ち上げる \
    `python run.py serve`
- gh-pagesブランチをgithub pagesとしてdeployする \
    `python run.py deploy`