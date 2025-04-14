
# twinx_tick_utils

對齊 Matplotlib 中 `twinx()` 雙 Y 軸的格線，確保兩側格線數量一致、位置對齊、整齊 round，並視需求強制包含 0。

## 🚀 安裝依賴

```bash
make install
```

## 🧪 執行測試

```bash
make test
```

## 🧾 使用方式

```python
from twinx_tick_utils import align_twinx_ticks

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

# 畫圖
ax1.plot(...)
ax2.plot(...)

# 設定 y-lim（必要）
ax1.set_ylim(...)
ax2.set_ylim(...)

# 對齊格線
align_twinx_ticks(ax1, ax2, target_num_ticks=7, prefer='max')
```

## 🛠️ 參數說明

- `target_num_ticks`: 預期格線數量（含兩端）
- `prefer`: 'min' 或 'max'，當兩軸預設格線數不同時，以較小或較大者為基準

## 📦 檔案說明

- `twinx_tick_utils.py`: 主功能模組
- `test_align_ticks.py`: 單元測試腳本
- `Makefile`: 提供 install/test/lint/clean 指令
- `README.md`: 本說明文件

---

Designed for data alignment perfectionists 😎
