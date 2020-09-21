## Description

Twitter で有名な[theoremoon](https://github.com/theoremoon)さんの[シェル芸 bot](https://github.com/theoremoon/ShellgeiBot)を Discord 上で実現する bot です．

......といっても自力で Docker コンテナを動かしているわけではなく[jiro4989](https://github.com/jiro4989)さんの[websh](https://github.com/jiro4989/websh)の API を叩くだけ．

## Usage

- **この bot へのメンションに反応して**シェルコマンドを実行します．またその際この bot へのメンションはコードから削除されます．
- メンションなどの MessageFormat の文字数によるズレをなるべく吸収し，表示に近い字幅でシェルを実行します．
- コードブロック (\`\`\` ~ \`\`\`) が存在する場合，１つ目のコードブロックの中身のみをコードとして認識します．
- 30 秒以上の処理はタイムアウトします．
- その他の仕様は本家のリポジトリか[こちら](https://furutsuki.hatenablog.com/entry/2018/07/13/221806)を御覧ください．

## Link

- [シェル芸 bot (theoremoon)](https://github.com/theoremoon/ShellgeiBot): 本家大本
- [websh (jiro4989)](https://github.com/jiro4989/websh): API 利用先
- [今の所判明しているシェル芸 bot の仕様](https://furutsuki.hatenablog.com/entry/2018/07/13/221806): Twitter のシェル芸 bot の仕様

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author

[kairi003](https://github.com/kairi003)
