`main_demo.ipynb`がメインの調査内容になります。

`git clone`してそのまま使用する場合は、`credentials.yaml`ファイルを作成して、以下の形式で情報を記載してください。

```yaml
# Code Interpreter を使用しない AOAI (価格の都合)
openai:
  key: YOUR_KEY
  version: 2023-12-01-preview
  endpoint: YOUR_ENDPOINT

text_analytics:
  key: YOUR_KEY
  endpoint: YOUR_ENDPOINT

web_search:
  key: YOUR_KEY

# Code Interpreter を使用する AOAI
openai_gpt4:
  key: YOUR_KEY
  version: 2024-02-15-preview
  endpoint: YOUR_ENDPOINT
```