import urllib.parse

url = urllib.parse.quote('https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=1D89BB97FBB21580DBBD41D717CFAAC6&country=in&endpoint=/product_feed/rollup_threads/v2?filter=marketplace%28IN%29&filter=language%28en-GB%29&filter=employeePrice%28true%29&filter=attributeIds%2816633190-45e5-4830-a068-232ac7aea82c%2C0f64ecc7-d624-4e91-b171-b83a03dd8550%29&anchor=96&consumerChannelId=d9a5bc42-4b9c-4976-858a-f159cf99c647&count=24')
print(url)