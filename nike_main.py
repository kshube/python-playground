import requests
import urllib.parse

base_url = 'https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=1D89BB97FBB21580DBBD41D717CFAAC6&country=in&endpoint='
# The API endpoint
first_url = "%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(IN)%26filter%3Dlanguage(en-GB)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(16633190-45e5-4830-a068-232ac7aea82c%2C0f64ecc7-d624-4e91-b171-b83a03dd8550)%26anchor%3D72%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24&language=en-GB&localizedRangeStr=%7BlowestPrice%7D%E2%80%94%7BhighestPrice%7D"

url = base_url + first_url
decoded_url = urllib.parse.unquote(url)
print(decoded_url)

while(True):
    response = requests.get(url)
    response_json = response.json()
    products = response_json['data']['products']['products']
    for product in products:
        print(product['title'])
        print(len(product['colorways']))
        print(product['price']['currentPrice'])
    next_page = response_json['data']['products']['pages']['next']
    print(base_url+urllib.parse.quote(next_page))
    if(next_page): 
        continue
    else: 
        break