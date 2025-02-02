import requests
from bs4 import BeautifulSoup

# 网页地址
url = 'https://news.ycombinator.com/'  # 将其替换为你想要爬取的网址

# 发送HTTP请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    print("Successfully fetched the page.")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
    exit()

# 解析网页内容
soup = BeautifulSoup(response.text, 'html.parser')

# 获取网页标题
title = soup.title.string
print(f"The title of the webpage is: {title}")

# 获取所有超链接
links = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href and not href.startswith('#'):
        links.append(href)
        print(f"Found link: {href}")

# 打印所有找到的链接
print(f"Total links found: {len(links)}")
for link in links:
    print(link)