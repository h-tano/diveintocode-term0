OSにおけるユーザーとは、システムにログインするための  
アカウントのこと。他のユーザーの追加・削除、アプリケーションの  
追加・削除など重要なことが行えるrootユーザーとそれ以外の  
通常ユーザーがある。

自分がどのユーザーであるかを確認するコマンド：whoami

OSにおけるグループとは、１度の操作で特定のファイルや  
フォルダなどに対して同じ権限を持つように設定することが  
できるユーザーの集まりのこと。OS Xではstaffがデフォルト。

自分がどのグループであるかを確認するコマンド：groups

ログの説明  
これはls -l hoge.txt と入力すれば確認できる。  
左端の１０桁は、一番左が横棒なので対象がファイルであることを表し、  
その右隣の３桁rw-は対象の所有者（今回はuser）は読み書き可能、  
実行不可能ということを表し、その右隣の３桁r--は特定のグループ  
（今回はuser）は読むことは可能、書込みと実行が不可能ということ  
を表し、その右隣の３桁r--はグループにも属さないその他のユーザーは  
読むことだけ可能ということを表している。  
その他、さらに右隣はハードリンク数、user userの１つ目は対象の所有者、  
２つ目は対象の属するグループを表し、最後に、ファイルサイズと更新日時が  
書かれている。
