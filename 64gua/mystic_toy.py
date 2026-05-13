import random


# =========================
# 1. 八卦基础数据
# =========================
# tuple 顺序是“从下往上”的三爻：
# 1 = 阳爻 ———
# 0 = 阴爻 — —
TRIGRAMS = {
    (1, 1, 1): ("乾", "天"),
    (0, 0, 0): ("坤", "地"),
    (1, 0, 0): ("震", "雷"),
    (0, 1, 1): ("巽", "风"),
    (0, 1, 0): ("坎", "水"),
    (1, 0, 1): ("离", "火"),
    (0, 0, 1): ("艮", "山"),
    (1, 1, 0): ("兑", "泽"),
}


# key = (上卦, 下卦)
HEXAGRAMS = {
    ("乾", "乾"): "乾为天",
    ("坤", "坤"): "坤为地",
    ("坎", "震"): "水雷屯",
    ("艮", "坎"): "山水蒙",
    ("坎", "乾"): "水天需",
    ("乾", "坎"): "天水讼",
    ("坤", "坎"): "地水师",
    ("坎", "坤"): "水地比",
    ("巽", "乾"): "风天小畜",
    ("乾", "兑"): "天泽履",
    ("坤", "乾"): "地天泰",
    ("乾", "坤"): "天地否",
    ("乾", "离"): "天火同人",
    ("离", "乾"): "火天大有",
    ("坤", "艮"): "地山谦",
    ("震", "坤"): "雷地豫",
    ("兑", "震"): "泽雷随",
    ("艮", "巽"): "山风蛊",
    ("坤", "兑"): "地泽临",
    ("巽", "坤"): "风地观",
    ("离", "震"): "火雷噬嗑",
    ("艮", "离"): "山火贲",
    ("艮", "坤"): "山地剥",
    ("坤", "震"): "地雷复",
    ("乾", "震"): "天雷无妄",
    ("艮", "乾"): "山天大畜",
    ("艮", "震"): "山雷颐",
    ("兑", "巽"): "泽风大过",
    ("坎", "坎"): "坎为水",
    ("离", "离"): "离为火",
    ("兑", "艮"): "泽山咸",
    ("震", "巽"): "雷风恒",
    ("乾", "艮"): "天山遁",
    ("震", "乾"): "雷天大壮",
    ("离", "坤"): "火地晋",
    ("坤", "离"): "地火明夷",
    ("巽", "离"): "风火家人",
    ("离", "兑"): "火泽睽",
    ("坎", "艮"): "水山蹇",
    ("震", "坎"): "雷水解",
    ("艮", "兑"): "山泽损",
    ("巽", "震"): "风雷益",
    ("兑", "乾"): "泽天夬",
    ("乾", "巽"): "天风姤",
    ("兑", "坤"): "泽地萃",
    ("坤", "巽"): "地风升",
    ("兑", "坎"): "泽水困",
    ("坎", "巽"): "水风井",
    ("兑", "离"): "泽火革",
    ("离", "巽"): "火风鼎",
    ("震", "震"): "震为雷",
    ("艮", "艮"): "艮为山",
    ("巽", "艮"): "风山渐",
    ("震", "兑"): "雷泽归妹",
    ("震", "离"): "雷火丰",
    ("离", "艮"): "火山旅",
    ("巽", "巽"): "巽为风",
    ("兑", "兑"): "兑为泽",
    ("巽", "坎"): "风水涣",
    ("坎", "兑"): "水泽节",
    ("巽", "兑"): "风泽中孚",
    ("震", "艮"): "雷山小过",
    ("坎", "离"): "水火既济",
    ("离", "坎"): "火水未济",
}


# =========================
# 2. 掷筊功能
# =========================

def throw_jiaobei_once():
    """
    单次掷筊。
    返回：cup1, cup2, result, meaning
    """
    cup1 = random.choice(["正", "反"])
    cup2 = random.choice(["正", "反"])

    if cup1 != cup2:
        result = "圣筊"
        meaning = "同意 / 可以 / 答案偏向 Yes"
    elif cup1 == "反" and cup2 == "反":
        result = "阴筊"
        meaning = "不同意 / 不可以 / 答案偏向 No"
    else:
        result = "笑筊"
        meaning = "问题不清楚 / 时机未到 / 可以重新问"

    return cup1, cup2, result, meaning


def throw_jiaobei():
    """
    普通掷筊。
    """
    cup1, cup2, result, meaning = throw_jiaobei_once()

    print("\n=== 掷筊结果 ===")
    print(f"筊杯一：{cup1}")
    print(f"筊杯二：{cup2}")
    print(f"结果：{result}")
    print(f"解释：{meaning}")


def three_shengjiao_confirm():
    """
    连续三次圣筊确认。
    只要中途不是圣筊，就失败。
    """
    question = input("\n请输入你想确认的问题：").strip()

    print("\n=== 三圣筊确认 ===")
    print(f"问题：{question if question else '未输入问题'}")
    print("规则：连续三次圣筊，才算确认通过。\n")

    for round_num in range(1, 4):
        cup1, cup2, result, meaning = throw_jiaobei_once()

        print(f"第 {round_num} 次：{cup1} / {cup2} => {result}")

        if result != "圣筊":
            print("\n确认失败。")
            print(f"原因：第 {round_num} 次不是圣筊。")
            print(f"解释：{meaning}")
            print("建议：问题可能不够明确，或者现在不适合。")
            return False

    print("\n确认成功：连续三次圣筊。")
    print("结论：可以。")
    return True


# =========================
# 3. 六爻起卦功能
# =========================

def generate_one_yao():
    """
    三枚铜钱法的简化版：

    正面 = 3
    反面 = 2

    三枚相加：
    6 = 老阴，变爻，阴变阳
    7 = 少阳，不变
    8 = 少阴，不变
    9 = 老阳，变爻，阳变阴
    """

    coins = [random.choice([2, 3]) for _ in range(3)]
    total = sum(coins)

    if total == 6:
        return {
            "value": 6,
            "line": 0,
            "changed_line": 1,
            "name": "老阴",
            "changing": True,
            "symbol": "— —  x",
            "coins": coins,
        }
    elif total == 7:
        return {
            "value": 7,
            "line": 1,
            "changed_line": 1,
            "name": "少阳",
            "changing": False,
            "symbol": "———",
            "coins": coins,
        }
    elif total == 8:
        return {
            "value": 8,
            "line": 0,
            "changed_line": 0,
            "name": "少阴",
            "changing": False,
            "symbol": "— —",
            "coins": coins,
        }
    else:
        return {
            "value": 9,
            "line": 1,
            "changed_line": 0,
            "name": "老阳",
            "changing": True,
            "symbol": "———  o",
            "coins": coins,
        }


def get_hexagram_name(lines):
    """
    lines 是从下往上的 6 爻。
    例如：
    [1, 1, 1, 0, 0, 0]

    前三爻 = 下卦
    后三爻 = 上卦
    """

    lower_bits = tuple(lines[0:3])
    upper_bits = tuple(lines[3:6])

    lower_name, lower_image = TRIGRAMS[lower_bits]
    upper_name, upper_image = TRIGRAMS[upper_bits]

    hexagram_name = HEXAGRAMS.get((upper_name, lower_name), "未知卦")

    return {
        "upper_name": upper_name,
        "upper_image": upper_image,
        "lower_name": lower_name,
        "lower_image": lower_image,
        "hexagram_name": hexagram_name,
    }


def draw_hexagram(yaos, title):
    """
    打印卦象。
    yaos 内部是从下往上存储；
    显示时要从上往下打印。
    """
    print(f"\n=== {title} ===")
    print("从上往下显示：\n")

    for index in range(5, -1, -1):
        yao = yaos[index]
        position = index + 1
        changing_text = "  变爻" if yao["changing"] else ""
        print(f"{yao['symbol']:<8} 第{position}爻  {yao['name']}{changing_text}")


def cast_hexagram():
    """
    六爻起卦。
    """
    question = input("\n请输入你想问的问题：").strip()

    yaos = []

    for _ in range(6):
        yaos.append(generate_one_yao())

    original_lines = [yao["line"] for yao in yaos]
    changed_lines = [yao["changed_line"] for yao in yaos]

    original_info = get_hexagram_name(original_lines)
    changed_info = get_hexagram_name(changed_lines)

    print("\n==============================")
    print("你的问题：", question if question else "未输入问题")
    print("==============================")

    draw_hexagram(yaos, "本卦")

    print("\n本卦信息：")
    print(f"上卦：{original_info['upper_name']}，象：{original_info['upper_image']}")
    print(f"下卦：{original_info['lower_name']}，象：{original_info['lower_image']}")
    print(f"本卦：{original_info['hexagram_name']}")

    changing_positions = [
        str(index + 1)
        for index, yao in enumerate(yaos)
        if yao["changing"]
    ]

    if changing_positions:
        print(f"变爻：第 {'、'.join(changing_positions)} 爻")
    else:
        print("变爻：无")

    print("\n变卦信息：")
    print(f"上卦：{changed_info['upper_name']}，象：{changed_info['upper_image']}")
    print(f"下卦：{changed_info['lower_name']}，象：{changed_info['lower_image']}")
    print(f"变卦：{changed_info['hexagram_name']}")

    print("\n娱乐性解释：")
    print("本卦可以理解为当前状态。")
    print("变爻代表事情正在变化的位置。")
    print("变卦可以理解为趋势或后续状态。")
    print("本程序只做娱乐和学习，不代表真实预测。")


# =========================
# 4. Deploy Oracle 功能
# =========================

def deploy_oracle():
    """
    今日宜不宜 deploy。
    本质上就是三圣筊确认，但加了一点开发者梗。
    """
    print("\n=== FlowMagik Deploy Oracle ===")
    print("正在询问：今天是否适合 deploy / push production？")
    print("规则：需要连续三次圣筊。\n")

    for round_num in range(1, 4):
        cup1, cup2, result, meaning = throw_jiaobei_once()

        print(f"第 {round_num} 次：{cup1} / {cup2} => {result}")

        if result != "圣筊":
            print("\nOracle 结果：不建议 deploy。")

            if result == "阴筊":
                print("神明建议：先别动 production。")
                print("请先检查：")
                print("1. git status")
                print("2. migration 是否安全")
                print("3. 数据库是否备份")
                print("4. server logs 是否正常")
                print("5. docker compose ps 是否正常")
            else:
                print("神明建议：问题不清楚。")
                print("请先问清楚：你是 deploy dev、staging，还是 production？")

            print(f"\n解释：{meaning}")
            return False

    print("\nOracle 结果：可以 deploy。")
    print("但神明补充：")
    print("1. 先 git status")
    print("2. 先 git pull / git push 确认")
    print("3. 先备份数据库")
    print("4. 先看 migration")
    print("5. 再 docker compose up -d --build")
    print("6. 最后 docker compose logs --tail=80 web")
    return True


# =========================
# 5. 主菜单
# =========================

def main():
    while True:
        print("\n==============================")
        print("玄学玩具 v0.2")
        print("==============================")
        print("1. 掷筊")
        print("2. 三圣筊确认")
        print("3. 六爻起卦")
        print("4. 今日宜不宜 Deploy")
        print("5. 退出")

        choice = input("\n请选择功能：").strip()

        if choice == "1":
            throw_jiaobei()
        elif choice == "2":
            three_shengjiao_confirm()
        elif choice == "3":
            cast_hexagram()
        elif choice == "4":
            deploy_oracle()
        elif choice == "5":
            print("退出。")
            break
        else:
            print("输入无效，请重新选择。")


if __name__ == "__main__":
    main()