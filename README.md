# hotpeppergourmetapi
ホットペッパーAPIを使った情報取得サービス

# 環境構築手順
1. hotpepperapiキー取得  
以下参照  
https://webservice.recruit.co.jp/register  

2. docker-desktopインストール  
以下参照  
https://docs.docker.jp/docker-for-windows/toc.html  

3. ビルド＋コンテナ立ち上げ  
`cd {hotpeppergourmetapiが入っているパス}`  
`docker build -t hotpeppergourmetapi .`  
`docker compose up -d`  

4. コンテナに接続  
`docker compose exec -e APIKEY=[APIキー] hotpeppergourmetapi bash`  

5. デモコードの実行
`python app/demo.py`  
エラーが発生せずにjsonデータが返ってきたら成功

# 後処理
- コンテナ停止・削除  
`docker stop hotpeppergourmetapi`  
`docker rm hotpeppergourmetapi`  

- イメージ削除  
`docker rmi hotpeppergourmetapi`  

# 参考資料
## apiリファレンス
https://webservice.recruit.co.jp/doc/hotpepper/reference.html