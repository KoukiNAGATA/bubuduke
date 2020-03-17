# bubuduke
Qiita投稿記事[そうだ、ぶぶ漬け食べよう。【京都弁で始める自然言語処理】](https://qiita.com/KoukiNAGATA/items/a81d547fedd2d6b7b309) 
の実際のコードを載せています。
COTOHA APIの構文解析を使っています。

## コード
- samplecode1.py 文章から名詞だけを抽出して返します。
- bubuduke.py 文章から抽出した名詞単位でスクローリングして、その単語が含まれるものと同じ単語を直訳に含む京都弁があれば返します。
