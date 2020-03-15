from cotoha_nlp.parse import Parser
import requests
from bs4 import BeautifulSoup
import re

parser = Parser("Client ID",
  "Client secret",
  "https://api.ce-cotoha.com/api/dev/nlp",
  "https://api.ce-cotoha.com/v1/oauth/accesstokens"
)
# input
s = parser.parse(input())

# get nouns
nouns = [token.form for token in s.tokens if token.pos in  ["名詞"]]

# web scraping
r = requests.get('https://iirou.com/kazoekata/')
soup = BeautifulSoup(r.content, "html.parser")
block = soup.find_all("p")

# output
for noun in nouns:
  for tag in block:
    if noun in str(tag):
      #strongタグ内にある京都弁を切り出し
      output = re.findall('<strong>.*</strong>', str(tag))
      out = output[0]
      out = out.replace("<strong>", "")
      out = out.replace("</strong>", "")
      print(out)