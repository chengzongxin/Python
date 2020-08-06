import requests
import re
import time
import os
# 导入urlopen
from urllib.request import urlopen,urlretrieve

net = 'https://www.vmgirls.com/13344.html'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'
}
response = requests.get(net,headers = headers)
html = response.text
urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">',html)
dir_name = re.findall('<h1 class="post-title h3">(.*?)</h1>',html)[-1]

if not os.path.exists(dir_name):
    os.mkdir(dir_name)

print(dir_name)
current_file = net.split('/')[-1]
print(len(urls))
for url in urls:
    full_url = net.replace(current_file,'') + url
    print(full_url)
    time.sleep(1)
    file_name = url.split('/')[-1]

    # urlretrieve(full_url, dir_name + '/' + file_name)
    response = requests.get(full_url,headers=headers,stream='true')
    with open(dir_name + '/' + file_name,'wb') as f:
        f.write(response.content)