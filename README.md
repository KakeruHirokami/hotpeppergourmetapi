# hotpeppergourmetapi
ホットペッパーAPIを使った情報取得サービス

# 環境構築手順
## hotpepperapiキー取得
以下参照
https://webservice.recruit.co.jp/register

## docker-desktopインストール
以下参照
https://docs.docker.jp/docker-for-windows/toc.html

## ビルド＋コンテナ立ち上げ
cd {hotpeppergourmetapiが入っているパス}
docker build -t hotpeppergourmetapi .
docker compose up -d

## コンテナに接続
docker compose exec -e APIKEY=[APIキー] hotpeppergourmetapi bash

## コンテナ停止・削除
docker stop hotpeppergourmetapi
docker rm hotpeppergourmetapi

## イメージ削除
docker rmi hotpeppergourmetapi

# 参考資料
## apiリファレンス
https://webservice.recruit.co.jp/doc/hotpepper/reference.html