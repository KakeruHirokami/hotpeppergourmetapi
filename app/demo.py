import os
import requests

# グルメサーチAPI実施
def main():
  apikey = os.getenv('APIKEY')
  payload = {"key": apikey, "large_area": "Z011", "format": "json"}
  url = f'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'
  res_json = api_get_requests(url, payload)
  print(res_json)

def api_get_requests(url, payload):
  try:
    response = requests.get(url, params=payload)
    response.raise_for_status()   # 200番台以外だったらエラーに投げる
    response_json = response.json()
    return response_json["results"]
  except requests.exceptions.RequestException as e:
    return e



main()