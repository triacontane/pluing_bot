# 本リポジトリについて
本リポジトリは、私の作成したプラグインを定期的にポストするXのbotを作成、管理するためのものです。

## botアカウント
<https://twitter.com/triacontane_bot>

## 概要
プラグイン一覧のスプレットシートからGoogle Sheets APIを用いて内容を取得し、ランダムで選択したプラグインをポストします。

[プラグイン一覧](https://docs.google.com/spreadsheets/d/1BnTyJr3Z1WoW4FMKtvKaICl4SQ5ehL5RxTDSV81oVQc/edit#gid=1411848872)

## 利用技術
### Google Sheets API
Google Sheets APIです。
スプレットシートから情報を取得するために利用しています。

[管理コンソール](https://console.cloud.google.com/apis/api/sheets.googleapis.com/metrics?project=brave-smile-399204)

### Google Cloud Functions
botを実行するスクリプトを配置しています。

[管理コンソール](https://console.cloud.google.com/functions/list?hl=ja&project=brave-smile-399204)

### Secret Manager
Google Cloud上で利用するシークレット情報を管理しています。
[管理コンソール](https://console.cloud.google.com/security/secret-manager?hl=ja&project=brave-smile-399204)

### Google Cloud Scheduler
botを定期実行するためのスケジューラです。

[管理コンソール](https://console.cloud.google.com/cloudscheduler?project=brave-smile-399204)

### XのAPI管理
スクリプトからXに投稿するためのAPIキーやトークンを管理しています。

[管理コンソール](https://developer.twitter.com/en/portal/projects/1702888364108881920/apps)

## 参考文献

[twittbotが停止したので自力でtwitterのBotを作成する（APIv2対応）](https://qiita.com/hatchnson/items/6e3c731a5fd5cd684eff)

[tweepy + Twitter API V2でツイート](https://qiita.com/penguinprogrammer/items/b220be0c203eaaad015a)

[【Google Sheets API】 スプレッドシートのデータをJSONで取得する](https://notes.sharesl.net/articles/2541/)