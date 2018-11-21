# 使い方

## 注意

このツールは高度な変換機能を提供します。ツールを使用するためには、プログラムを直接読むか、以下の内容で理解できるスキルを必要とします。

## つかいかた

1: Pythonスクリプトとして実行する

**初回のみ：setup-venv.bat と setup-libs.bat を実行してください。依存している外部ライブラリをインストールします。**

`python main.py <midifile>`

2: exe形式から実行する(ZIPファイルを添付しています。 : 64bit OS のみ)

`BSMConverter.exe <midifile>`

or

`midiファイルをBSMConverter.exeへドラッグ・アンド・ドロップする`

**正常に変換できた場合はクリップボードにJSON形式のテキストがコピーされます**

## MIDIファイル仕様

### BPM

BPMの検知を試みます。予めテンポ情報を埋め込んでおいてください。

### ビートの向き

MIDI ノートイベント（音階）で表現します。

| Note |             Beat Direction             |
|:----:|:------------------:|
| C    | 上 (direction:0)   |
| D    | 下 (direction:1)   |
| E    | 左 (direction:2)   |
| F    | 右 (direction:3)   |
| F#   | 左上 (direction:4) |
| G    | 右上 (direction:5) |
| G#   | 左下 (direction:6) |
| A    | 右下 (direction:7) |
| B    | Any (direction:8)  |

### レイヤーマッピング

 MIDIノートイベント（ベロシティ）で表現します。

~~~
1-42      43-83      84-127
  |         |          *
  |         *          |
  *         |          |
~~~

### ラインマッピング

MIDI ノートイベント（音階のオクターブ）で表現します。

~~~
Octave4: *---
Octave5: -*--
Octave6: --*-
Octave7: ---*
~~~

### ビートタイプ

MIDI CC2 の値を使用します。

| CC2 Value | Beat Type |
|:---------:|:---------:|
| 0-31      | 赤        |
| 32-63     | 青        |
| 64-96     | トゲトゲ  |

## 想定使用例

DAW (Cubase, Studio One, Logic, etc.)の使用を想定しています。

1. 元となるオーディオデータをオーディオトラックにセット
2. MIDIトラックを２つ作成
3. Track1: MIDI CC2( value:0 ) を先頭にセット -\> **赤**
4. Track2: MIDI CC2( value:32 ) を先頭にセット -\> **青**
5. MIDIノートを打ち込み
6. SMFでエクスポート (ティック解像度は480推奨)
7. 変換
8. 外部の Beat Saber エディタでチェック (e.g.: EditSaber)
