# 星等分成三種等級：「流水席」、「宴會廳」、「五星級飯店」，
# 熟識程度則分為四個等級：「泛泛之交」、「普通朋友」、「好朋友」、「死黨」。

# 紅包的金額 1600, 1800, 2200, 2600, 2800, 3200, 3600, 6000, 6600, 8000 共十個級距。

# Level = ["流水席", "宴會廳", "五星級飯店"]
# friend = ["泛泛之交", "普通朋友", "好朋友", "死黨"]
# red =["1600, 1800, 2200, 2600, 2800, 3200, 3600, 6000, 6600, 8000"]

def calculate_red_packet():
    Level = ["流水席", "宴會廳", "五星級飯店"]
    friend = ["泛泛之交", "普通朋友", "好朋友", "死黨"]
    red = [1600, 1800, 2200, 2600, 2800, 3200, 3600, 6000, 6600, 8000]

    line1 = input().split()
    star_level = line1[0]
    friendship = line1[1]
    has_company = input()

    base_index = -1
    if star_level == "流水席":
        base_index = 0
    elif star_level == "宴會廳":
        base_index = 2
    elif star_level == "五星級飯店":
        base_index = 4

    friend_level_increase = friend.index(friendship)

    company_increase = 0
    if has_company == "Y":
        company_increase = 2

    final_index = base_index + friend_level_increase + company_increase

    # 確保最終的 index 不超出紅包金額列表的範圍
    if final_index >= len(red):
        final_index = len(red) - 1

    red_packet_amount = red[final_index]

    if friendship == "死黨" and red_packet_amount < 6000:
        red_packet_amount = 6000

    print(red_packet_amount)

calculate_red_packet()
