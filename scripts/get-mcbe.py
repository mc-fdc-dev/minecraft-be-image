import requests
from bs4 import BeautifulSoup


r = requests.get("https://www.minecraft.net/ja-jp/download/server/bedrock", headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"
})
soup = BeautifulSoup(r.text, "html.parser")

# found patern link this https://minecraft.azureedge.net/bin-linux/bedrock-server-*.zip
# get link
link = soup.find("a", href=lambda href: href and href.startswith("href="https://www.minecraft.net/bedrockdedicatedserver/bin-linux/bedrock-server-"))
print(link.get("href"))

# install zip file
r = requests.get(link.get("href"))
with open("bedrock-server.zip", "wb") as f:
    f.write(r.content)
