# Meme Generator

一個簡單的 Python 程式，用於生成梗圖。用戶可以選擇模板，輸入文字，並生成一張新的梗圖。

## 安裝

1. 確保已安裝 Python 3（[下載](https://www.python.org/)）。
2. 安裝 Pillow 庫：
   ```bash
   pip install pillow
   git clone https://github.com/username/meme-generator.git
   cd meme-generator
   ```

## 使用方法
確保 templates 資料夾中有模板圖片（例如 1.jpg、2.jpg）。
運行程式：
```bash
python meme_generator.py
```
按照提示選擇模板並輸入頂部與底部文字。
程式會生成梗圖並保存為 meme.jpg。

## 注意事項
請自行準備免費的梗圖模板圖片並放入 templates 資料夾。
支援白色文字與黑色邊框，字體預設為 Arial（可自行替換）。