import requests
from bs4 import BeautifulSoup


r = requests.get("https://www.minecraft.net/ja-jp/download/server/bedrock")
soup = BeautifulSoup(r.text, "html.parser")

# found patern link this https://minecraft.azureedge.net/bin-linux/bedrock-server-*.zip
# get link
link = soup.find("a", href=lambda href: href and href.startswith("https://minecraft.azureedge.net/bin-linux/bedrock-server-"))
print(link.get("href"))

# install zip file
r = requests.get(link.get("href"))
with open("bedrock-server.zip", "wb") as f:
    f.write(r.content)
