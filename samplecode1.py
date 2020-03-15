from cotoha_nlp.parse import Parser

parser = Parser("Client ID",
  "Client secret",
  "https://api.ce-cotoha.com/api/dev/nlp",
  "https://api.ce-cotoha.com/v1/oauth/accesstokens"
)
s = parser.parse(input())

print(" ".join([token.form for token in s.tokens if token.pos in  ["名詞"]]))