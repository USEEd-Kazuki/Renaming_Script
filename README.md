## Unreal Engine <br /> アセットの一括リネームツール
このPythonスクリプトは、Unreal Engine内の複数のアセットの名前を一括で変更するためのツールです。


## 使い方
<br />1 , Unreal Engine内でPythonスクリプトを実行します。
<br />    PythonコンソールやPythonスクリプトエディターで実行できます。
<br />2 , rename_assets 関数を呼び出して、アセットの名前を変更します。

<br />引数は下記の通りです。
-   　search_pattern: 置換したいアセットの名前を指定します。
-   　replaced_pattern: search_pattern にマッチした部分を置換する文字列を指定します。
-   　use_case: 大文字小文字を区別するかどうかを指定します。Trueの場合は大文字小文字を区別します。

(例)
<br /> rename_assets("対象アセット名", "新しいアセット名", "True or False")
<br />* Line34を変更

<br />3 , スクリプトを実行すると、選択したアセットの名前が変更されます。

## インストール
<br />このスクリプトをUnreal Engineプロジェクトに組み込むには、以下の手順を実行してください：
<br />1 , Content/Scriptsや適切なディレクトリにPythonスクリプトを配置します。
<br />2 , Unreal Engine内でPythonスクリプトを実行します。

## 注意事項
- このスクリプトを使用する前に、変更されるアセットのバックアップを作成することをお勧めします。
<br />現時点では、このスクリプトは特定のパターンに一致するアセットの名前の一部を置換するために設計されています。そのため、置換が予期しない結果をもたらす可能性があります。

## 作者
UESSd-Kazuki
