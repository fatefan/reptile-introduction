import requests
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
source = requests.post('http://www.ftchinese.com/rss/news') #获取FT中文 RSS XML数据
root = ET.fromstring(source.text.encode('utf-8')) # 解析 XML
for title in root.iter('title'):
    print title.text.encode('utf-8') # 打印title
