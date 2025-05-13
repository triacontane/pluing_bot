# 本リポジトリについて
本リポジトリは、私が作成したXのbotを作成、管理するためのものです。

## botアカウント
[トリアコンタンのプラグインbot](https://twitter.com/triacontane_bot)
[徳川まつり台詞bot](https://x.com/t_matsuri_bot_2)

## 概要
情報取得元のスプレットシートからGoogle Sheets APIを用いて内容を取得し、ランダムで選択した内容をポストします。

## 利用技術
### Google Sheets API
Google Sheets APIです。
スプレットシートから情報を取得するために利用しています。

### Google Cloud Functions
botを実行するスクリプトを配置しています。

### Secret Manager
Google Cloud上で利用するシークレット情報を管理しています。

### Google Cloud Scheduler
botを定期実行するためのスケジューラです。

### XのAPI管理
スクリプトからXに投稿するためのAPIキーやトークンを管理しています。

## 参考文献

[twittbotが停止したので自力でtwitterのBotを作成する（APIv2対応）](https://qiita.com/hatchnson/items/6e3c731a5fd5cd684eff)

[tweepy + Twitter API V2でツイート](https://qiita.com/penguinprogrammer/items/b220be0c203eaaad015a)

[【Google Sheets API】 スプレッドシートのデータをJSONで取得する](https://notes.sharesl.net/articles/2541/)