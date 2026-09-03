# 学习打卡器

一个用于记录学习时长和连续打卡天数的小工具。使用Codex辅助开发。

## 当前进度

目前可以新增一条学习打卡记录；之后会逐步加入连续打卡统计和导出功能。

## 如何运行

1. 在终端中进入项目文件夹。
2. 运行下面的命令：

   ```powershell
   python src/main.py
   ```

3. 依次输入学习科目、学习分钟数和学习备注。
4. 如果看到“打卡成功”，说明记录已保存到 `data/checkins.json`。

## 打卡记录示例

每一条记录都会自动包含当天日期，并保存在本地文件 `data/checkins.json` 中：

```json
[
  {
    "date": "2026-09-03",
    "subject": "Python",
    "minutes": 45,
    "note": "完成第一个 Python 程序"
  }
]
```

`data/checkins.json` 不会上传到 GitHub，因此你的个人学习记录会保留在本机。
