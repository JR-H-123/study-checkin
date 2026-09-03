"""学习打卡器的程序入口。"""

import json
from datetime import date
from pathlib import Path


DATA_FILE = Path("data/checkins.json")


def get_minutes() -> int:
    """反复询问，直到用户输入一个大于 0 的整数。"""
    while True:
        value = input("学习了多少分钟？")
        try:
            minutes = int(value)
        except ValueError:
            print("请输入整数，例如：45。")
            continue

        if minutes <= 0:
            print("学习时长需要大于 0 分钟。")
            continue

        return minutes


def load_checkins() -> list[dict[str, object]]:
    """读取已有记录；第一次使用时返回空列表。"""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("无法读取已有打卡记录：文件内容不是有效的 JSON。")
        return []


def save_checkins(checkins: list[dict[str, object]]) -> None:
    """将所有记录以易读的 JSON 格式保存到本地。"""
    DATA_FILE.parent.mkdir(exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(checkins, file, ensure_ascii=False, indent=2)


def main() -> None:
    """收集一条学习记录并保存。"""
    print("学习打卡器已启动")

    subject = input("你学习了什么科目？").strip()
    while not subject:
        print("科目不能为空。")
        subject = input("你学习了什么科目？").strip()

    minutes = get_minutes()
    note = input("学习备注是什么？（可留空）").strip()

    checkin = {
        "date": date.today().isoformat(),
        "subject": subject,
        "minutes": minutes,
        "note": note,
    }
    checkins = load_checkins()
    checkins.append(checkin)
    save_checkins(checkins)

    print(f"打卡成功！已记录：{subject}，{minutes} 分钟。")


if __name__ == "__main__":
    main()
