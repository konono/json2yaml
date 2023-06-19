# json2yaml
## 概要
Jsonとyamlを相互変換してくれるツールです。

世の中にはそういったツールがたくさんありますが、普段書くyamlのインデントでdumpしてくれるツールがなかったので作りました。

あとは、、、CLIツールのパッケージの勉強も兼ねて。。。

インストール方法
```
pip3 install git+https://github.com/konono/json2yaml
```

## 使い方
-i: input file、jsonもしくはyamlで記述されたファイルを指定します。

-f: format、変換する先のフォーマットであるjsonもしくはyamlを指定します。

-o: output file、もしも変換した内容をファイルに書き出したい場合はこのオプションを利用します。

```
json2yaml --help
usage: python3 cli.py <type> <command> [option]

options:
  -h, --help            show this help message and exit
  -i INPUT_FILE, --input INPUT_FILE
                        Set path of file to be converted
  -o OUTPUT_FILE, --output OUTPUT_FILE
                        user name
  -f FORMAT, --format FORMAT
                        file format, json or yaml
```
