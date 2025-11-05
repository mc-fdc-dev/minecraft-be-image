import requests
from bs4 import BeautifulSoup


r = requests.get("https://www.minecraft.net/ja-jp/download/server/bedrock", headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"
})
soup = BeautifulSoup(r.text, "html.parser")

# found patern link this https://minecraft.azureedge.net/bin-linux/bedrock-server-*.zip
# get link
link = soup.find("a", href=lambda href: href and href.startswith("https://www.minecraft.net/bedrockdedicatedserver/bin-linux/bedrock-server-"))
print(link.get("href"))

# install zip file
r = requests.get(link.get("href"))
with open("bedrock-server.zip", "wb") as f:
    f.write(r.content)
