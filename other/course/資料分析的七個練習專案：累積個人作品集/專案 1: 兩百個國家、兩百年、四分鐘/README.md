# 🌍 Dynamic Visualization: 200 Countries, 200 Years, 4 Minutes

這是一個資料視覺化小專案，旨在以動態方式呈現兩百個國家在過去兩百年間的變化趨勢。最終成果為一段約四分鐘的互動式動畫，透過視覺手法傳達時間與地理維度的結合。

## 🛠 使用技術

- **資料處理**：`pandas`
- **資料儲存**：`sqlite3`
- **原型驗證**：`matplotlib`
- **互動式視覺化**：`plotly.express`

## 📦 專案結構

```
├── data/                # 原始資料與處理後的 SQLite 資料庫
├── scripts/             # 各階段處理與視覺化程式碼
│   ├── extract_data.py
│   ├── build_database.py
│   ├── explore_matplotlib.py
│   └── plotly_visualization.py
├── output/              # 動態圖表或影片輸出
└── README.md
```

## 🎯 專案目標

- 建立高品質動態視覺化動畫
- 強調跨國與跨年代的歷史變遷趨勢
- 概念驗證使用 `matplotlib`，最後以 `plotly.express` 提升互動性與美觀

## 📽 預覽

👉 [放置動畫截圖或連結 GIF / MP4 / Plotly 線上頁面]

## 📌 安裝與執行

```bash
git clone https://github.com/yourname/yourproject.git
cd yourproject
pip install -r requirements.txt
python scripts/plotly_visualization.py
```

## 📚 參考資料

- [Gapminder Dataset](https://www.gapminder.org/data/)
- [Plotly Express Documentation](https://plotly.com/python/plotly-express/)
- [Hans Rosling TED Talk](https://www.ted.com/talks/hans_rosling_the_best_stats_you_ve_ever_seen)

## 🔖 備註

此專案靈感來自 Hans Rosling 的經典動態資料視覺化呈現。本專案不使用商業套件，完全以 Python 開源工具完成。

---

若你喜歡這個專案，歡迎 Star⭐ 或提供建議 🙌