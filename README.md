# マイクから音声入力した音声をリアルタイム翻訳で字幕表示するアプリ
# Real-time Voice Translation and Subtitling App

このアプリケーションは、マイクからの音声入力をリアルタイムで翻訳し、字幕表示するものです。

<img width="966" alt="スクリーンショット 2024-01-06 102626" src="https://github.com/suzunayui/streamer-translation-deepl/assets/148876956/69ac90d3-b464-442d-b663-a9e3464953e4">

## 必要なもの

- [DeepL API](https://www.deepl.com/ja/account/summary) の認証キー
- Python 3.10
- (Optional) OBS Studio (ウィンドウキャプチャで利用可能)
- (Optional) Windows PowerShell の透明度を99%に設定

## DeepL API

2024年1月6日現在、開発者向けの「DeepL API Free」は1か月あたり500,000文字まで無料で使用できます。利用が制限に達した場合は、月額630円から始まる「DeepL API Pro」にアップグレードできます。

1. [DeepL アカウントを作成](https://www.deepl.com/ja/account/summary)
2. APIキーを取得してください。

## アプリのセットアップ

1. `sample.env` ファイルを `.env` にリネームしてください。
2. `.env` ファイル内の `apikey` 部分を取得したDeepL APIの認証キーに置き換えてください。

## 実行

1. Microsoft Store から Python 3.10 をインストールしてください。
2. `run.bat` をダブルクリックしてアプリを起動します。

## 使用方法

マイクに日本語の音声を入力すると、日本語の字幕と翻訳された英語の字幕が表示されます。OBS Studioを使用する場合は、ウィンドウキャプチャなどで取り込むことができます。

PowerShell を使用する場合、設定＞Windows PowerShell＞外観＞背景の不透明度を99%にすると良い感じになります。

## 注意事項

- このアプリケーションはDeepL APIを使用しています。制限に注意してください。

---

**Enjoy the real-time voice translation and subtitling experience!**
