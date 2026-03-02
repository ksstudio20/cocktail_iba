#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from typing import Dict, List

COCKTAILS: List[Dict] = [
  {
    "name": "亚历山大",
    "base": "白兰地",
    "taste": "经典永恒",
    "ingredients": [
      "30 ml 干邑",
      "30 ml 棕可可利口酒",
      "30 ml 鲜奶油"
    ],
    "steps": [
      "将所有材料倒入装满冰块的调酒壶中。",
      "摇和后过滤至预冷鸡尾酒杯中。"
    ]
  },
  {
    "name": "阿美利卡诺",
    "base": "未知",
    "taste": "经典永恒",
    "ingredients": [
      "30 ml 金巴利苦味利口酒",
      "30 ml 甜红味美思",
      "少许苏打水"
    ],
    "steps": [
      "将材料直接加入装满冰块的古典杯中混合。",
      "加入少许苏打水，轻轻搅拌。"
    ]
  },
  {
    "name": "天使之颜",
    "base": "金酒",
    "taste": "经典永恒",
    "ingredients": [
      "30 ml 金酒",
      "30 ml 杏子白兰地",
      "30 ml 卡尔瓦多斯苹果白兰地"
    ],
    "steps": [
      "将所有材料倒入装满冰块的调酒壶中。",
      "摇和后过滤至预冷鸡尾酒杯中。"
    ]
  },
  {
    "name": "航空",
    "base": "金酒",
    "taste": "经典永恒",
    "ingredients": [
      "45 ml 金酒",
      "15 ml 卢萨朵马拉斯奇诺樱桃利口酒",
      "15 ml 新鲜柠檬汁",
      "1 吧匙 紫罗兰利口酒"
    ],
    "steps": [
      "将所有材料加入调酒壶中。",
      "加入碎冰摇和后，过滤至预冷鸡尾酒杯中。"
    ]
  },
  {
    "name": "蜂之膝",
    "base": "金酒",
    "taste": "新时代经典",
    "ingredients": [
      "52.5 ml 干金酒",
      "2 茶匙 蜂蜜糖浆",
      "22.5 ml 新鲜柠檬汁",
      "22.5 ml 新鲜橙汁"
    ],
    "steps": [
      "先将蜂蜜与柠檬汁、橙汁搅拌至溶解，加入金酒后加冰摇和，过滤至预冷鸡尾酒杯中。"
    ]
  },
  {
    "name": "贝里尼",
    "base": "起泡酒",
    "taste": "当代经典",
    "ingredients": [
      "100 ml 普罗赛克",
      "50 ml 白桃果泥"
    ],
    "steps": [
      "将桃泥倒入装有冰块的调和杯中，加入普罗赛克。",
      "轻轻搅拌后倒入预冷香槟笛形杯中。",
      "注：\nPuccini – Fresh M并arin Orange Ju冰;\nRossini – Fresh Strawberry Puree;\nT到retto – Fresh Pomegranate Ju冰."
    ]
  },
  {
    "name": "床笫之间",
    "base": "朗姆",
    "taste": "经典永恒",
    "ingredients": [
      "30 ml 白朗姆酒",
      "30 ml 干邑",
      "30 ml 三重橙酒",
      "20 ml 新鲜柠檬汁"
    ],
    "steps": [
      "将所有材料加入调酒壶中。",
      "加冰摇和后，过滤至预冷鸡尾酒杯中。"
    ]
  },
  {
    "name": "黑俄罗斯",
    "base": "伏特加",
    "taste": "当代经典",
    "ingredients": [
      "50 ml 伏特加",
      "20 ml 咖啡利口酒"
    ],
    "steps": [
      "倒入 材料 到 the 古典杯 装满ed 加 冰块.",
      "搅拌 轻轻地. 过滤 ingredients 到 古典杯 装满ed 加 冰.",
      "注：\nWhite Russian：将鲜奶油漂浮于酒面，缓慢搅入。"
    ]
  },
  {
    "name": "血腥玛丽",
    "base": "伏特加",
    "taste": "当代经典",
    "ingredients": [
      "45 ml 伏特加",
      "90 ml 番茄汁",
      "15 ml 新鲜柠檬汁",
      "2 滴 伍斯特酱",
      "塔巴斯科、芹盐、胡椒（按口味）"
    ],
    "steps": [
      "将所有材料在装有冰块的调和杯中轻轻搅拌，倒入古典杯中。",
      "注：\n如客人要求加冰版本，倒入海波杯。"
    ]
  },
  {
    "name": "大道",
    "base": "威士忌",
    "taste": "经典永恒",
    "ingredients": [
      "45 ml 波本或黑麦威士忌",
      "30 ml 金巴利苦味利口酒",
      "30 ml 甜红味美思"
    ],
    "steps": [
      "将所有材料倒入装有冰块的调和杯中。",
      "充分搅拌后，过滤至预冷鸡尾酒杯中。"
    ]
  },
  {
    "name": "荆棘",
    "base": "金酒",
    "taste": "新时代经典",
    "ingredients": [
      "50 ml 金酒",
      "25 ml 新鲜柠檬汁",
      "12.5 ml 糖浆",
      "15 ml 黑莓利口酒"
    ],
    "steps": [
      "将所有材料倒入调酒壶 except the Crème de Mûre, 摇和 充分 加冰, 过滤 到 预冷古典杯 装满ed with 碎冰,，然后倒入 the blackberry liqueur (Crème de Mûre) 于酒液表面, 以环形方式."
    ]
  },
  {
    "name": "白兰地克鲁斯塔",
    "base": "白兰地",
    "taste": "经典永恒",
    "ingredients": [
      "52.5 ml 白兰地",
      "7.5 ml 卢萨朵马拉斯奇诺樱桃利口酒",
      "1 吧匙 橙味利口酒",
      "15 ml 新鲜柠檬汁",
      "1 吧匙 糖浆",
      "2 滴 芳香苦精"
    ],
    "steps": [
      "Mix together 所有材料 加 冰块 in a mixing",
      "杯，过滤 到 a prepared slim 鸡尾酒杯."
    ]
  },
  {
    "name": "凯匹林纳",
    "base": "未知",
    "taste": "当代经典",
    "ingredients": [
      "60 ml 卡莎萨",
      "1 青柠切成小块",
      "4 茶匙 白蔗糖"
    ],
    "steps": [
      "将青柠和糖放入双份古典杯中，轻轻捣压。",
      "将杯中加入碎冰，再加入卡莎萨，轻轻搅拌使材料融合。",
      "注：\nCaipiroska：将 卡莎萨 改用 伏特加；\nCaipirissima：将 卡莎萨 改用 朗姆酒.\nCaipirão：将 卡莎萨 改用 Licor Beirão."
    ]
  },
  {
    "name": "坎昌查拉",
    "base": "未知",
    "taste": "新时代经典",
    "ingredients": [
      "60 ml 古巴甘蔗烈酒",
      "15 ml 新鲜青柠汁",
      "15 ml 生蜂蜜",
      "50 ml 水"
    ],
    "steps": [
      "将蜂蜜、水和青柠汁混合，并涂抹在杯底与杯壁。",
      "加入碎冰，再加入朗姆酒。",
      "最后由下至上有力搅拌。"
    ]
  },
  {
    "name": "红衣主教",
    "base": "金酒",
    "taste": "当代经典",
    "ingredients": [
      "40 ml 金酒",
      "20 ml 干味美思",
      "10 ml 金巴利苦味利口酒"
    ],
    "steps": [
      "将所有材料倒入装有冰块的调和杯中，充分搅拌。",
      "过滤至预冷鸡尾酒杯中。"
    ]
  },
  {
    "name": "卡西诺",
    "base": "金酒",
    "taste": "经典永恒",
    "ingredients": [
      "40 ml 老汤姆金酒",
      "10 ml 卢萨朵马拉斯奇诺樱桃利口酒",
      "10 ml 新鲜柠檬汁",
      "2 滴 橙味苦精"
    ],
    "steps": [
      "将所有材料倒入调酒壶, 摇和 充分 加冰, 过滤",
      "到 预冷 古典杯 加 冰."
    ]
  },
  {
    "name": "香槟鸡尾酒",
    "base": "白兰地",
    "taste": "当代经典",
    "ingredients": [
      "90 ml 冰镇香槟",
      "10 ml 干邑",
      "2 滴 安格仕苦精",
      "几滴大玛尼耶（可选）",
      "1 方糖"
    ],
    "steps": [
      "Place the 糖 cube 加 2 dashes of 苦精s in a large 香槟 杯, 加入 the cognac.",
      "倒入 轻轻地 预冷 香槟."
    ]
  },
  {
    "name": "夏特勒斯旋转",
    "base": "未知",
    "taste": "新时代经典",
    "ingredients": [
      "45 ml 绿色夏特勒斯",
      "30 ml 新鲜菠萝汁",
      "22.5 ml 新鲜青柠汁",
      "15 ml 法兰恩糖香酒"
    ],
    "steps": [
      "倒入 所有材料 到 a 高杯, 加入 小碎冰.",
      "With the help of a swizzle棒 (or 调酒勺) mix 充分地, complete by 装满ing the 杯 加 more 小碎冰."
    ]
  },
  {
    "name": "三叶草俱乐部",
    "base": "金酒",
    "taste": "经典永恒",
    "ingredients": [
      "45 ml 金酒",
      "15 ml 覆盆子糖浆",
      "15 ml 新鲜柠檬汁",
      "几滴蛋清"
    ],
    "steps": [
      "将所有材料倒入调酒壶, 摇和 充分 加冰, 过滤 到 预冷鸡尾酒杯."
    ]
  },
  {
    "name": "尸体复活者2号",
    "base": "金酒",
    "taste": "当代经典",
    "ingredients": [
      "30 ml 金酒",
      "30 ml 君度橙酒",
      "30 ml 利莱白",
      "30 ml 新鲜柠檬汁",
      "1 滴 苦艾酒"
    ],
    "steps": [
      "将所有材料倒入调酒壶 加冰.",
      "摇和 充分，过滤 in 预冷鸡尾酒杯."
    ]
  },
  {
    "name": "大都会",
    "base": "伏特加",
    "taste": "当代经典",
    "ingredients": [
      "40 ml 香柠伏特加",
      "15 ml 君度橙酒",
      "15 ml 新鲜青柠汁",
      "30 ml 蔓越莓汁"
    ],
    "steps": [
      "将所有材料加入调酒壶 装满冰块.",
      "摇和 well 并 过滤 到 大号鸡尾酒杯."
    ]
  },
  {
    "name": "自由古巴",
    "base": "朗姆",
    "taste": "当代经典",
    "ingredients": [
      "50 ml 白朗姆酒",
      "120 ml 可乐",
      "10 ml 新鲜青柠汁"
    ],
    "steps": [
      "将所有材料直接加入装满冰块的海波杯中调和。"
    ]
  },
  {
    "name": "黛琪莉",
    "base": "未知",
    "taste": "经典永恒",
    "ingredients": [
      "60 ml 古巴白朗姆",
      "20 ml 新鲜青柠汁",
      "2 吧匙细砂糖"
    ],
    "steps": [
      "In a 调酒壶 加入 所有材料. 搅拌 充分 to dissolve the sugar.",
      "加入 冰，摇和. 过滤至预冷鸡尾酒杯中。"
    ]
  },
  {
    "name": "黑暗风暴",
    "base": "金酒",
    "taste": "新时代经典",
    "ingredients": [
      "60 ml 高斯林朗姆",
      "100 ml 金酒ger Beer（待核对）"
    ],
    "steps": [
      "In a 海波杯 装满ed 加 冰 倒入 the 姜汁啤酒 并 top floating 加 the Rum."
    ]
  },
  {
    "name": "唐氏特调黛琪莉",
    "base": "朗姆",
    "taste": "新时代经典",
    "ingredients": [
      "30 ml 金色牙买加朗姆酒",
      "15 ml 古巴朗姆酒",
      "15 ml 百香果糖浆",
      "15 ml 新鲜青柠汁",
      "15 ml 蜂蜜糖浆"
    ],
    "steps": [
      "Blend for a few seconds in a milk摇和 mixer 加 碎冰 并 倒入 到 a 带脚copo杯.",
      "在杯中补充更多碎冰。"
    ]
  },
  {
    "name": "干马天尼",
    "base": "金酒",
    "taste": "经典永恒",
    "ingredients": [
      "60 ml 金酒",
      "10 ml 干味美思"
    ],
    "steps": [
      "将所有材料倒入装有冰块的调和杯中，充分搅拌。",
      "过滤至预冷马天尼杯中。"
    ]
  },
  {
    "name": "浓缩咖啡马天尼",
    "base": "伏特加",
    "taste": "新时代经典",
    "ingredients": [
      "50 ml 伏特加",
      "30 ml 卡鲁哇",
      "10 ml 糖浆",
      "1 浓缩咖啡"
    ],
    "steps": [
      "将所有材料倒入调酒壶，加冰充分摇和后，过滤至预冷鸡尾酒杯中。"
    ]
  },
  {
    "name": "费尔南迪托",
    "base": "未知",
    "taste": "新时代经典",
    "ingredients": [
      "50 ml 布兰卡费尔奈",
      "用可乐补满"
    ],
    "steps": [
      "倒入 the Fernet Branca 到 a 双份古典杯 加冰, 装满 the 杯 up with Cola. Gently 搅拌."
    ]
  },
  {
    "name": "法式75",
    "base": "金酒",
    "taste": "当代经典",
    "ingredients": [
      "30 ml 金酒",
      "15 ml 新鲜柠檬汁",
      "15 ml 糖浆",
      "60 ml 香槟"
    ],
    "steps": [
      "倒入 all 材料, 除 香槟, 到 a 调酒壶.",
      "摇和 well 并 过滤 到 a 香槟笛形杯.",
      "Top up 加 香槟.",
      "轻轻搅拌。"
    ]
  },
  {
    "name": "法国连线",
    "base": "白兰地",
    "taste": "当代经典",
    "ingredients": [
      "35 ml 干邑",
      "35 ml 阿玛雷托"
    ],
    "steps": [
      "倒入 所有材料 直接于to 古典杯 装满冰块.",
      "轻轻搅拌。"
    ]
  },
  {
    "name": "法式马天尼",
    "base": "伏特加",
    "taste": "新时代经典",
    "ingredients": [
      "45 ml 伏特加",
      "15 ml 覆盆子利口酒",
      "15 ml 新鲜菠萝汁"
    ],
    "steps": [
      "将所有材料倒入调酒壶，加冰充分摇和后，过滤至预冷鸡尾酒杯中。"
    ]
  },
  {
    "name": "加里波第",
    "base": "未知",
    "taste": "当代经典",
    "ingredients": [
      "45 ml 金巴利苦味利口酒",
      "120 ml 鲜榨橙汁"
    ],
    "steps": [
      "将所有材料直接加入装满冰块的海波杯中调和。"
    ]
  },
  {
    "name": "罗勒金酒碎击",
    "base": "金酒",
    "taste": "新时代经典",
    "ingredients": [
      "60ml Gin（原文保留）",
      "22.5 ml 鲜榨柠檬汁",
      "22.5 ml 糖浆",
      "10 个 意大利罗勒叶"
    ],
    "steps": [
      "将所有材料加入调酒壶 加冰.",
      "摇和 充分地，倒入 到 预冷鸡尾酒杯."
    ]
  },
  {
    "name": "金酒菲士",
    "base": "金酒",
    "taste": "经典永恒",
    "ingredients": [
      "45 ml 金酒",
      "30 ml 新鲜柠檬汁",
      "10 ml 糖浆",
      "少许苏打水"
    ],
    "steps": [
      "摇和 所有材料 加 冰 除 苏打水.",
      "倒入 到 thin tall Tumbler 杯 , 顶部加入 a splash 苏打水.",
      "注：\n不加冰饮用。"
    ]
  },
  {
    "name": "特级玛格丽塔",
    "base": "龙舌兰",
    "taste": "新时代经典",
    "ingredients": [
      "45 ml 100%龙舌兰酒",
      "30 ml 大玛尼耶",
      "15 ml 新鲜青柠汁"
    ],
    "steps": [
      "Rim the rock 杯 加 good quality sea salt. 倒入 材料 到 the 调酒壶.",
      "加入 冰 to both 杯 并 调酒壶.",
      "摇和 hard for 10 seconds. 过滤 the drink 到 the 杯."
    ]
  },
  {
    "name": "蚱蜢",
    "base": "未知",
    "taste": "当代经典",
    "ingredients": [
      "20 ml 白可可利口酒",
      "20 ml 绿薄荷利口酒",
      "20 ml 鲜奶油"
    ],
    "steps": [
      "将所有材料倒入调酒壶 装满冰块.",
      "摇和 briskly for few seconds. 过滤至预冷鸡尾酒杯中。"
    ]
  },
  {
    "name": "汉基潘基",
    "base": "金酒",
    "taste": "经典永恒",
    "ingredients": [
      "45 ml 伦敦干金酒",
      "45 ml 甜红味美思",
      "7.5 ml 费尔奈"
    ],
    "steps": [
      "将所有材料倒入装有冰块的调和杯中，充分搅拌。",
      "过滤至预冷鸡尾酒杯中。"
    ]
  },
  {
    "name": "海明威特调",
    "base": "朗姆",
    "taste": "当代经典",
    "ingredients": [
      "60 ml 朗姆酒",
      "40 ml 葡萄柚汁",
      "15 ml 卢萨朵马拉斯奇诺樱桃利口酒",
      "15 ml 新鲜青柠"
    ],
    "steps": [
      "将所有材料倒入装有冰块的调酒壶中。",
      "摇和 well 并 过滤 到 a 大号鸡尾酒杯."
    ]
  },
  {
    "name": "马颈",
    "base": "金酒",
    "taste": "当代经典",
    "ingredients": [
      "40 ml 干邑",
      "120 ml 金酒ger Ale（待核对）",
      "少许安格仕苦精（可选）"
    ],
    "steps": [
      "倒入 干邑 并 姜汁汽水 直接 到 海波杯 加 冰块.",
      "轻轻搅拌。",
      "If preferred, 加入 dashes of Angostura Bitter."
    ]
  },
  {
    "name": "IBA 提基",
    "base": "未知",
    "taste": "新时代经典",
    "ingredients": [
      "30 ml 哈瓦那俱乐部 Profundo 朗姆",
      "30 ml 哈瓦那俱乐部 Smoky 朗姆",
      "15 ml 阿玛雷托利口酒",
      "5 ml 榛子利口酒（Frangelico）",
      "5 滴 卢萨朵马拉斯奇诺樱桃利口酒",
      "30 ml 百香果果泥",
      "90 新鲜菠萝汁",
      "30 新鲜青柠汁",
      "1 片 姜片"
    ],
    "steps": [
      "In a 调酒壶 轻捣 a thin sl冰 of Gengibre, 倒入 all other ingredients.",
      "摇和 充分地 加冰.",
      "过滤 到 a 预冷 提基杯 装满ed 加 小碎冰."
    ]
  },
  {
    "name": "非法",
    "base": "朗姆",
    "taste": "新时代经典",
    "ingredients": [
      "30 ml 埃斯帕丁梅斯卡尔",
      "15 ml 牙买加高酒精度白朗姆",
      "15 ml 法兰恩糖香酒",
      "1 吧匙 卢萨朵马拉斯奇诺樱桃利口酒",
      "22.5 ml 新鲜青柠汁",
      "15 ml 糖浆",
      "几滴蛋清（可选）"
    ],
    "steps": [
      "将所有材料倒入调酒壶中，加冰用力摇和。",
      "过滤 到 a 预冷 cocktail 杯, or “加冰” in a traditional clay or terracotta mug."
    ]
  },
  {
    "name": "爱尔兰咖啡",
    "base": "威士忌",
    "taste": "当代经典",
    "ingredients": [
      "50 ml 爱尔兰威士忌",
      "120 ml 热咖啡",
      "50 ml 鲜奶油（冰镇）",
      "1 茶匙 糖"
    ],
    "steps": [
      "Warm black coffee is 倒入ed 到 a preheated Irish coffee 杯.",
      "Whiskey 并 at least one teaspoon of 糖 is 加入ed 并 搅拌red 直至溶解.",
      "Fresh thick 预冷 cream is carefully 倒入ed over the back of a spoon held just above the surface of the coffee.",
      "The layer of cream will float on the coffee without mixing.（步骤原文保留，建议人工校对）",
      "Plain sugar can be replaced with sugar syrup（步骤原文保留，建议人工校对）"
    ]
  },
  {
    "name": "约翰柯林斯",
    "base": "金酒",
    "taste": "经典永恒",
    "ingredients": [
      "45 ml 金酒",
      "30 ml 新鲜柠檬汁",
      "15 ml 糖浆",
      "60 ml 苏打水"
    ],
    "steps": [
      "倒入 所有材料 直接 到 highball 装满ed 加 冰. 搅拌 轻轻地.",
      "注：\nTom Collins 请使用 Old Tom 金酒。"
    ]
  },
  {
    "name": "丛林鸟",
    "base": "朗姆",
    "taste": "新时代经典",
    "ingredients": [
      "45 ml 黑糖蜜朗姆酒",
      "22.5 ml 金巴利",
      "45 ml 菠萝汁",
      "15 ml 鲜榨青柠汁",
      "15 ml 德梅拉拉糖浆"
    ],
    "steps": [
      "将所有材料倒入a 调酒壶 加冰，摇和.",
      "过滤 到 a 古典杯 装满ed 加 冰."
    ]
  },
  {
    "name": "基尔",
    "base": "未知",
    "taste": "当代经典",
    "ingredients": [
      "90 ml 干白葡萄酒",
      "10 ml 黑加仑利口酒"
    ],
    "steps": [
      "倒入 Crème de Cassis 到 杯, 补满 加 white 红酒.",
      "注：\nKir Royal：以香槟代替白葡萄酒。"
    ]
  },
  {
    "name": "最后一句",
    "base": "金酒",
    "taste": "经典永恒",
    "ingredients": [
      "22.5 ml 金酒",
      "22.5 ml 绿色夏特勒斯",
      "22.5 ml 卢萨朵马拉斯奇诺樱桃利口酒",
      "22.5 ml 新鲜青柠汁"
    ],
    "steps": [
      "将所有材料加入调酒壶中。",
      "加冰摇和后，过滤至预冷鸡尾酒杯中。"
    ]
  },
  {
    "name": "柠檬糖马天尼",
    "base": "伏特加",
    "taste": "当代经典",
    "ingredients": [
      "30 ml 伏特加",
      "20 ml 三重橙酒",
      "15 ml 鲜榨柠檬汁"
    ],
    "steps": [
      "将所有材料倒入装有冰块的调酒壶中。",
      "摇和 充分，过滤 到 a 预冷鸡尾酒杯."
    ]
  },
  {
    "name": "长岛冰茶",
    "base": "金酒",
    "taste": "当代经典",
    "ingredients": [
      "15 ml 伏特加",
      "15 ml 龙舌兰",
      "15 ml 白朗姆酒",
      "15 ml 金酒",
      "15 ml 君度橙酒",
      "25 ml 柠檬汁",
      "30 ml 糖浆",
      "顶部加可乐"
    ],
    "steps": [
      "将所有材料加入海波杯 装满冰块.",
      "轻轻搅拌。"
    ]
  },
  {
    "name": "迈泰",
    "base": "朗姆",
    "taste": "当代经典",
    "ingredients": [
      "30 ml 琥珀牙买加朗姆酒",
      "30 ml 马提尼克糖蜜朗姆*",
      "15 ml 橙味库拉索",
      "15 ml 欧榭糖浆（杏仁）",
      "30 ml 鲜榨青柠汁",
      "7.5 ml 糖浆"
    ],
    "steps": [
      "将所有材料加入装有冰块的调酒壶中。",
      "摇和 并 倒入 到 a double 古典杯 or an 海波杯.",
      "* The Martinique molasses rum used by Trader Vic was not an Agricole Rhum but a type of “rummy” from molasses.（步骤原文保留，建议人工校对）"
    ]
  },
  {
    "name": "曼哈顿",
    "base": "威士忌",
    "taste": "经典永恒",
    "ingredients": [
      "50 ml 黑麦威士忌",
      "20 ml 甜红味美思",
      "1 滴 安格仕苦精"
    ],
    "steps": [
      "将所有材料倒入装有冰块的调和杯中。",
      "充分搅拌后，过滤至预冷鸡尾酒杯中。"
    ]
  },
  {
    "name": "玛格丽塔",
    "base": "龙舌兰",
    "taste": "当代经典",
    "ingredients": [
      "50 ml 100%龙舌兰酒",
      "20 ml 三重橙酒",
      "15 ml 鲜榨青柠汁"
    ],
    "steps": [
      "将所有材料加入装有冰块的调酒壶中。",
      "摇和后过滤至预冷鸡尾酒杯中。"
    ]
  },
  {
    "name": "马丁内斯",
    "base": "金酒",
    "taste": "经典永恒",
    "ingredients": [
      "45 ml 伦敦干金酒",
      "45 ml 甜红味美思",
      "1 吧匙 卢萨朵马拉斯奇诺樱桃利口酒",
      "2 滴 橙味苦精"
    ],
    "steps": [
      "将所有材料倒入装有冰块的调和杯中。",
      "充分搅拌后，过滤至预冷鸡尾酒杯中。"
    ]
  },
  {
    "name": "玛丽·碧克馥",
    "base": "朗姆",
    "taste": "经典永恒",
    "ingredients": [
      "45 ml 白朗姆酒",
      "45 ml 新鲜菠萝汁",
      "7.5 ml 卢萨朵马拉斯奇诺樱桃利口酒",
      "5 ml 红石榴糖浆"
    ],
    "steps": [
      "将所有材料倒入调酒壶，加冰充分摇和后，过滤至预冷鸡尾酒杯中。"
    ]
  },
  {
    "name": "含羞草",
    "base": "起泡酒",
    "taste": "当代经典",
    "ingredients": [
      "75 ml 鲜榨橙汁",
      "75 ml 普罗赛克"
    ],
    "steps": [
      "倒入 橙汁 到 flute 杯 并 轻轻地 倒入 the 起泡酒.",
      "轻轻搅拌。",
      "注：\n也称 Buck’s Fizz。"
    ]
  },
  {
    "name": "薄荷朱利普",
    "base": "威士忌",
    "taste": "当代经典",
    "ingredients": [
      "60 ml 波本威士忌",
      "4 新鲜薄荷枝",
      "1 茶匙 糖粉",
      "2 茶匙 水"
    ],
    "steps": [
      "In Julep Stainless Steel Cup 轻轻地 轻捣 the mint 加 糖 并 water.",
      "装满 the 杯 加 碎 冰, 加入 the Bourbon 并 搅拌 well until the cup frosts."
    ]
  },
  {
    "name": "传教士的陨落",
    "base": "朗姆",
    "taste": "新时代经典",
    "ingredients": [
      "30 ml 白朗姆酒",
      "15 ml 桃子白兰地",
      "15 ml 新鲜青柠汁",
      "30 ml 蜂蜜混合液",
      "10 个 薄荷叶",
      "3 至 4 块菠萝块"
    ],
    "steps": [
      "Blend all 材料 加 half cup of 碎冰.",
      "Serve it in a Coppa grande.（步骤原文保留，建议人工校对）"
    ]
  },
  {
    "name": "莫吉托",
    "base": "未知",
    "taste": "当代经典",
    "ingredients": [
      "45 ml 古巴白朗姆",
      "20 ml 新鲜青柠汁",
      "6 个 薄荷枝",
      "2 茶匙 白蔗糖",
      "苏打水"
    ],
    "steps": [
      "Mix mint springs 加 糖 并 青柠汁.",
      "加入 splash of 苏打水 并 装满 the 杯 加 冰.",
      "倒入 the 朗姆酒 并 顶部加入 苏打水. Light 搅拌 to involve 所有材料."
    ]
  },
  {
    "name": "猴腺",
    "base": "金酒",
    "taste": "经典永恒",
    "ingredients": [
      "45 ml 干金酒",
      "45 ml 新鲜橙汁",
      "1 汤匙 苦艾酒",
      "1 汤匙 红石榴糖浆"
    ],
    "steps": [
      "将所有材料倒入调酒壶，加冰充分摇和后，过滤至预冷鸡尾酒杯中。"
    ]
  },
  {
    "name": "莫斯科骡子",
    "base": "金酒",
    "taste": "当代经典",
    "ingredients": [
      "45 ml 斯米诺伏特加",
      "120 ml 金酒ger Beer（待核对）",
      "10 ml 新鲜青柠汁"
    ],
    "steps": [
      "In an Mule Cup or 古典杯, combine the 伏特加 并 姜汁啤酒.",
      "加入 青柠汁 并 轻轻地 搅拌 to involve 所有材料."
    ]
  },
  {
    "name": "赤裸与成名",
    "base": "龙舌兰",
    "taste": "新时代经典",
    "ingredients": [
      "22.5 ml 梅斯卡尔",
      "22.5 ml 黄色夏特勒斯",
      "22.5 ml 阿佩罗",
      "22.5 ml 新鲜青柠汁"
    ],
    "steps": [
      "将所有材料倒入调酒壶，加冰充分摇和后，过滤至预冷鸡尾酒杯中。"
    ]
  },
  {
    "name": "内格罗尼",
    "base": "金酒",
    "taste": "经典永恒",
    "ingredients": [
      "30 ml 金酒",
      "30 ml 金巴利苦味利口酒",
      "30 ml 甜红味美思"
    ],
    "steps": [
      "倒入 所有材料 直接于to 预冷古典杯 装满冰块.",
      "轻轻搅拌。"
    ]
  },
  {
    "name": "纽约酸",
    "base": "威士忌",
    "taste": "新时代经典",
    "ingredients": [
      "60 ml 黑麦威士忌或波本",
      "22.5 ml 糖浆",
      "30 ml 新鲜柠檬汁",
      "几滴蛋清",
      "15 ml 红葡萄酒（设拉子或马尔贝克）"
    ],
    "steps": [
      "将所有材料倒入调酒壶中，加冰用力摇和。",
      "过滤 到 a 预冷 古典杯 装满ed 加 冰. Float the 红酒 on top."
    ]
  },
  {
    "name": "老古巴",
    "base": "朗姆",
    "taste": "新时代经典",
    "ingredients": [
      "6–8 片薄荷叶",
      "45 ml 陈年朗姆酒",
      "22.5 ml 新鲜青柠汁",
      "30 ml 糖浆",
      "2 滴 安格仕苦精",
      "60 ml 干型香槟或普罗赛克"
    ],
    "steps": [
      "将所有材料倒入调酒壶 except the wine, 摇和 充分 加冰, 过滤 到 预冷elegant 鸡尾酒杯.",
      "Top up 加 the 起泡酒."
    ]
  },
  {
    "name": "古典",
    "base": "威士忌",
    "taste": "经典永恒",
    "ingredients": [
      "45 ml 波本或黑麦威士忌",
      "1 方糖",
      "数滴安格仕苦精",
      "少许清水"
    ],
    "steps": [
      "Place 糖 cube in 古典杯 并 saturate 加 苦精, 加入 few dashes of plain water. 轻捣 直至溶解. 装满 the 杯 加 冰块 并 加入 威士忌.",
      "轻轻搅拌。"
    ]
  },
  {
    "name": "帕洛玛",
    "base": "龙舌兰",
    "taste": "新时代经典",
    "ingredients": [
      "50 ml 100%龙舌兰酒",
      "5 ml 新鲜青柠",
      "一撮盐",
      "100 ml 粉红葡萄柚汽水"
    ],
    "steps": [
      "Poor the 龙舌兰 到 a 海波杯, squeeze the 青柠汁.",
      "加入 冰 并 salt, 装满 up pink grapefruit soda.",
      "轻轻搅拌。"
    ]
  },
  {
    "name": "纸飞机",
    "base": "威士忌",
    "taste": "新时代经典",
    "ingredients": [
      "30 ml 波本威士忌",
      "30 ml 诺尼诺阿玛罗",
      "30 ml 阿佩罗",
      "30 ml 新鲜柠檬汁"
    ],
    "steps": [
      "将所有材料倒入调酒壶，加冰充分摇和后，过滤至预冷鸡尾酒杯中。"
    ]
  },
  {
    "name": "天堂",
    "base": "金酒",
    "taste": "经典永恒",
    "ingredients": [
      "30 ml 金酒",
      "20 ml 杏子白兰地",
      "15 ml 新鲜橙汁"
    ],
    "steps": [
      "将所有材料倒入调酒壶，加冰充分摇和后，过滤至预冷鸡尾酒杯中。"
    ]
  },
  {
    "name": "盘尼西林",
    "base": "金酒",
    "taste": "新时代经典",
    "ingredients": [
      "60 ml 调和苏格兰威士忌",
      "7.5 ml 拉加维林16年",
      "22.5 ml 新鲜柠檬汁",
      "22.5 ml 蜂蜜糖浆",
      "2-3 四分之一块新鲜姜片"
    ],
    "steps": [
      "轻捣 新鲜姜 in a 调酒壶 并 加入 the 其余材料 除 for the Islay single malt whisky.",
      "装满 the 调酒壶 加 冰 并 摇和.",
      "Fine train 到 a 预冷 Old Fashioned 杯 加 冰.",
      "Float the single malt whisky on top.（步骤原文保留，建议人工校对）"
    ]
  },
  {
    "name": "椰林飘香",
    "base": "朗姆",
    "taste": "当代经典",
    "ingredients": [
      "50 ml 白朗姆酒",
      "30 ml 椰浆奶油",
      "50 ml 新鲜菠萝汁"
    ],
    "steps": [
      "Blend all 材料 加 冰 in a electric blender,",
      "倒入 到 a large 杯 并 serve 加 straws.",
      "注：\nHistorically a few drops of fresh 青柠汁 was 加入ed to taste. 4 sl冰s of fresh pineapple can be used instead of ju冰"
    ]
  },
  {
    "name": "皮斯科潘趣",
    "base": "未知",
    "taste": "新时代经典",
    "ingredients": [
      "60 ml 皮斯科",
      "22.5 ml 新鲜菠萝汁",
      "15 ml 糖浆",
      "15 ml 新鲜柠檬汁",
      "30 ml 干白葡萄酒",
      "3 个 Cloves（待核对）"
    ],
    "steps": [
      "Gentle mash the simple syrup 加 the cloves, 加入 the 其余材料 除 the 红酒.",
      "摇和 充分地 并 double 过滤 到 a large 高脚杯.",
      "加入 the 红酒 on top 并 轻轻地 搅拌."
    ]
  },
  {
    "name": "皮斯科酸",
    "base": "未知",
    "taste": "当代经典",
    "ingredients": [
      "60 ml 皮斯科",
      "30 ml 新鲜柠檬汁",
      "20 ml 糖浆",
      "1 生蛋清"
    ],
    "steps": [
      "将所有材料加入装有冰块的调酒壶中。",
      "摇和 并 过滤 到 a 预冷 高脚杯 杯."
    ]
  },
  {
    "name": "种植园主潘趣",
    "base": "朗姆",
    "taste": "经典永恒",
    "ingredients": [
      "45 ml 牙买加朗姆酒",
      "15 ml 青柠汁",
      "30 ml 甘蔗汁"
    ],
    "steps": [
      "倒入 所有材料 直接于 a small tumbler or a typical terracotta 杯.",
      "注：\n加入 dilution up to taste, it can be given by water, 冰 or fresh ju冰s."
    ]
  },
  {
    "name": "色情明星马天尼",
    "base": "伏特加",
    "taste": "新时代经典",
    "ingredients": [
      "50 ml 香草伏特加",
      "20 ml 百香果利口酒",
      "50 ml 百香果果泥",
      "2 Bar Spoons Vanilla Sugar（待核对）",
      "50 ml 香槟（另杯随附）"
    ],
    "steps": [
      "将所有材料倒入调酒壶, 摇和 充分 加冰, double 过滤 到 a large 预冷鸡尾酒杯.",
      "Accompany with a shot of champagne.（步骤原文保留，建议人工校对）"
    ]
  },
  {
    "name": "波特翻转",
    "base": "白兰地",
    "taste": "经典永恒",
    "ingredients": [
      "15 ml 白兰地",
      "45 ml 茶色波特酒",
      "10 ml 蛋黄"
    ],
    "steps": [
      "将所有材料倒入调酒壶，加冰充分摇和后，过滤至预冷鸡尾酒杯中。"
    ]
  },
  {
    "name": "公鸡尾",
    "base": "未知",
    "taste": "当代经典",
    "ingredients": [
      "60 ml 卡莎萨",
      "20 ml 仙山露红甜味美思",
      "15 ml 西纳尔",
      "2 滴 安格仕苦精（可选）"
    ],
    "steps": [
      "Combine all 材料 到 a 古典杯, 加入 冰 并 搅拌 短暂地."
    ]
  },
  {
    "name": "记住缅因",
    "base": "威士忌",
    "taste": "经典永恒",
    "ingredients": [
      "60 ml 黑麦威士忌",
      "22.5 ml 甜味美思",
      "15 ml 卢萨朵樱桃白兰地",
      "7.5 ml 苦艾酒"
    ],
    "steps": [
      "倒入 the absinthe 到 a coupe 杯 并 swirl to completely coat the inside.",
      "Discard the absinthe 并 set the 杯 aside. 加入 the other ingredients to a 调和杯 并 装满 it 3/4 full 加 冰. 搅拌 直至冰镇, 然后 过滤 到 the 杯 rinsed 加 the absinthe."
    ]
  },
  {
    "name": "俄罗斯之春潘趣",
    "base": "伏特加",
    "taste": "新时代经典",
    "ingredients": [
      "25 ml 伏特加",
      "25 ml 新鲜柠檬汁",
      "15 ml 黑加仑利口酒",
      "10 ml 糖浆",
      "用起泡酒补满"
    ],
    "steps": [
      "倒入 所有材料 到 调酒壶 除 the 起泡酒, 摇和 well 加 冰, 过滤 到 预冷 tall tumbler 杯 装满ed 加 冰",
      "and top up with sparkling wine.（步骤原文保留，建议人工校对）"
    ]
  },
  {
    "name": "铁锈钉",
    "base": "威士忌",
    "taste": "经典永恒",
    "ingredients": [
      "45 ml 苏格兰威士忌",
      "25 ml 杜林标"
    ],
    "steps": [
      "倒入 所有材料 直接于to an 古典杯 装满冰块.",
      "轻轻搅拌。"
    ]
  },
  {
    "name": "萨泽拉克",
    "base": "白兰地",
    "taste": "经典永恒",
    "ingredients": [
      "50 ml 干邑",
      "10 ml 苦艾酒",
      "1 方糖",
      "2 滴 培乔德苦精"
    ],
    "steps": [
      "Rinse a 预冷 古典杯 加 the absinthe, 加入 碎冰 并 set it aside. 搅拌 the 其余材料 over 冰 in a 调和杯.",
      "Discard the 冰 并 any excess absinthe from the prepared 杯, 过滤 the mixed drink 到 the 杯.",
      "注：\nThe original recipe changed after the American Civil War, 黑麦威士忌 substituted 干邑 as it became hard to obtain."
    ]
  },
  {
    "name": "海风",
    "base": "伏特加",
    "taste": "当代经典",
    "ingredients": [
      "40 ml 伏特加",
      "120 ml 蔓越莓汁",
      "30 ml 葡萄柚汁"
    ],
    "steps": [
      "将所有材料直接加入装满冰块的海波杯中调和。"
    ]
  },
  {
    "name": "海滩性爱",
    "base": "伏特加",
    "taste": "当代经典",
    "ingredients": [
      "40 ml 伏特加",
      "20 ml 蜜桃利口酒",
      "40 ml 新鲜橙汁",
      "40 ml 蔓越莓汁"
    ],
    "steps": [
      "将所有材料直接加入装满冰块的海波杯中调和。"
    ]
  },
  {
    "name": "雪莉科布勒",
    "base": "未知",
    "taste": "新时代经典",
    "ingredients": [
      "45 ml 阿蒙蒂亚多雪莉",
      "45 ml 帕洛科塔多雪莉",
      "1 茶匙 细砂糖（或砂糖）",
      "1/2 Orange Wheel（待核对）",
      "1/2 Lemon Wheel（待核对）"
    ],
    "steps": [
      "Combine sherry, 糖 并 2 quarter wheels each of orange 并 lemon in a 调酒壶 加 冰, 摇和 快速地, 过滤 到 a Julep cocktail cup 装满ed 加 碎冰."
    ]
  },
  {
    "name": "边车",
    "base": "白兰地",
    "taste": "经典永恒",
    "ingredients": [
      "50 ml 干邑",
      "20 ml 三重橙酒",
      "20 ml 新鲜柠檬汁"
    ],
    "steps": [
      "将所有材料倒入调酒壶，加冰充分摇和后，过滤至预冷鸡尾酒杯中。"
    ]
  },
  {
    "name": "新加坡司令",
    "base": "金酒",
    "taste": "当代经典",
    "ingredients": [
      "30 ml 金酒",
      "15 ml Morlacco 樱桃利口酒",
      "7.5 ml 君度橙酒",
      "7.5 ml DOM 本笃酒",
      "120 ml 新鲜菠萝汁",
      "15 ml 新鲜青柠汁",
      "10 ml 红石榴糖浆",
      "一滴安格仕苦精"
    ],
    "steps": [
      "将所有材料倒入装满冰块的调酒壶中。",
      "摇和 充分.",
      "过滤 到 飓风 杯."
    ]
  },
  {
    "name": "南边",
    "base": "金酒",
    "taste": "新时代经典",
    "ingredients": [
      "60 ml 伦敦干金酒",
      "30 ml 新鲜柠檬汁",
      "15 ml 糖浆",
      "5–6 片薄荷叶",
      "几滴蛋清（可选）"
    ],
    "steps": [
      "将所有材料倒入调酒壶，加冰充分摇和后，双重过滤至预冷鸡尾酒杯中。",
      "注：\n若使用蛋清，请更用力摇和。"
    ]
  },
  {
    "name": "辛辣五十",
    "base": "伏特加",
    "taste": "新时代经典",
    "ingredients": [
      "50 ml 香草伏特加",
      "15 ml 接骨木花糖浆",
      "15 ml 新鲜青柠汁",
      "10 ml 莫林蜂蜜糖浆",
      "2 薄切红辣椒片"
    ],
    "steps": [
      "将所有材料倒入调酒壶，加冰充分摇和后，双重过滤至预冷鸡尾酒杯中。"
    ]
  },
  {
    "name": "斯普里茨",
    "base": "起泡酒",
    "taste": "新时代经典",
    "ingredients": [
      "90 ml 普罗赛克",
      "60 ml 阿佩罗",
      "少许苏打水"
    ],
    "steps": [
      "Build 所有材料 到 a 红酒 杯 装满ed 加 冰.",
      "轻轻搅拌。",
      "注：\nSpritz 也有其他版本，可用 Campari、Cynar 或 Select 替代 Aperol。"
    ]
  },
  {
    "name": "毒刺",
    "base": "白兰地",
    "taste": "经典永恒",
    "ingredients": [
      "50 ml 干邑",
      "20 ml 白薄荷利口酒"
    ],
    "steps": [
      "将所有材料倒入装有冰块的调和杯中，充分搅拌。",
      "过滤至预冷马天尼杯中。"
    ]
  },
  {
    "name": "苦命混蛋",
    "base": "金酒",
    "taste": "新时代经典",
    "ingredients": [
      "30 ml 干邑或白兰地",
      "30 ml 金酒",
      "15 ml 新鲜青柠汁",
      "2 滴 安格仕苦精",
      "用姜汁啤酒补满"
    ],
    "steps": [
      "倒入 所有材料 到 调酒壶 除 the 姜汁啤酒, 摇和 well 加 冰.",
      "倒入 un过滤ed 到 a Collins 杯 or in the original.",
      "S. Bastard mug 并 补满 加 姜汁啤酒."
    ]
  },
  {
    "name": "龙舌兰日出",
    "base": "龙舌兰",
    "taste": "当代经典",
    "ingredients": [
      "45 ml 龙舌兰",
      "90 ml 新鲜橙汁",
      "15 ml 红石榴糖浆"
    ],
    "steps": [
      "倒入 龙舌兰 并 橙汁 直接 到 海波杯 装满ed 加 冰块.",
      "加入 the grenadine syrup to create chromatic effect (sunrise), do not 搅拌."
    ]
  },
  {
    "name": "三点一划",
    "base": "朗姆",
    "taste": "新时代经典",
    "ingredients": [
      "45 ml 马提尼克农业朗姆",
      "15 ml 调和陈年朗姆酒",
      "7.5 ml 法兰恩糖香酒",
      "7.5 ml 圣伊丽莎白多香果利口酒；15 ml 新鲜青柠汁（原数据疑似粘连）",
      "15 ml 新鲜橙汁",
      "15 ml 蜂蜜糖浆",
      "2 滴 安格仕苦精"
    ],
    "steps": [
      "倒入 所有材料 in a Blender 加 12 ounces of 碎冰, flash blend, 倒入 the drink 到 a 带脚copo杯.",
      "在杯中补充更多碎冰。"
    ]
  },
  {
    "name": "汤米玛格丽塔",
    "base": "龙舌兰",
    "taste": "新时代经典",
    "ingredients": [
      "60 ml 100%龙舌兰酒",
      "30 ml 新鲜青柠汁",
      "30 ml 龙舌兰糖浆"
    ],
    "steps": [
      "将所有材料倒入a 调酒壶, 摇和 充分 加冰, 过滤 到 预冷古典杯 装满冰块."
    ]
  },
  {
    "name": "特立尼达酸",
    "base": "威士忌",
    "taste": "新时代经典",
    "ingredients": [
      "45 ml 安格仕苦精",
      "30 ml 欧榭糖浆（杏仁糖浆）",
      "22.5 ml 新鲜柠檬汁",
      "15 ml 黑麦威士忌"
    ],
    "steps": [
      "将所有材料倒入a 调酒壶, 摇和 充分 加冰.",
      "过滤至预冷鸡尾酒杯中。"
    ]
  },
  {
    "name": "燕尾服",
    "base": "金酒",
    "taste": "经典永恒",
    "ingredients": [
      "30 ml 老汤姆金酒",
      "30 ml 干味美思",
      "1/2 吧匙 卢萨朵马拉斯奇诺樱桃利口酒",
      "1/4 吧匙 of Absinthe（待核对）",
      "3 滴 橙味苦精"
    ],
    "steps": [
      "将所有材料倒入装有冰块的调和杯中，充分搅拌。",
      "过滤至预冷马天尼杯中。"
    ]
  },
  {
    "name": "Ve.N.To",
    "base": "未知",
    "taste": "新时代经典",
    "ingredients": [
      "45 ml 白格拉巴",
      "22.5 ml 新鲜柠檬汁",
      "15 ml 蜂蜜混合液（可用洋甘菊替代水）*",
      "15 ml 洋甘菊甜酒/cordial",
      "几滴蛋清（可选）"
    ],
    "steps": [
      "将所有材料倒入调酒壶中，加冰用力摇和。",
      "过滤 到 a 预冷 small tumbler 杯 装满ed 加 冰.",
      "注：\n*如需要，蜂蜜混合液中的水可改为洋甘菊浸泡液。"
    ]
  },
  {
    "name": "维斯珀",
    "base": "金酒",
    "taste": "当代经典",
    "ingredients": [
      "45 ml 金酒",
      "15 ml 伏特加",
      "7.5 ml 利莱白"
    ],
    "steps": [
      "将所有材料倒入装满冰块的调酒壶中。",
      "摇和后过滤至预冷鸡尾酒杯中。"
    ]
  },
  {
    "name": "老广场",
    "base": "威士忌",
    "taste": "经典永恒",
    "ingredients": [
      "30 ml 黑麦威士忌",
      "30 ml 干邑",
      "30 ml 甜味美思",
      "1 吧匙 本笃酒",
      "2 滴 培乔德苦精"
    ],
    "steps": [
      "将所有材料倒入装有冰块的调和杯中。",
      "充分搅拌后，过滤至预冷鸡尾酒杯中。"
    ]
  },
  {
    "name": "威士忌酸",
    "base": "威士忌",
    "taste": "经典永恒",
    "ingredients": [
      "45 ml 波本威士忌",
      "25 ml 新鲜柠檬汁",
      "20 ml 糖浆",
      "几滴蛋清（可选）"
    ],
    "steps": [
      "将所有材料倒入调酒壶 装满冰块. 摇和 充分.",
      "过滤 到 cobbler 杯. If served “On the rocks”, 过滤 ingredients",
      "到 古典杯 装满ed 加 冰.",
      "注：\n若使用蛋清，请稍微更用力摇和，以释放并融合蛋白泡沫。"
    ]
  },
  {
    "name": "白衣女郎",
    "base": "金酒",
    "taste": "经典永恒",
    "ingredients": [
      "40 ml 金酒",
      "30 ml 三重橙酒",
      "20 ml 新鲜柠檬汁"
    ],
    "steps": [
      "将所有材料倒入调酒壶，加冰充分摇和后，过滤至预冷鸡尾酒杯中。"
    ]
  },
  {
    "name": "僵尸",
    "base": "朗姆",
    "taste": "当代经典",
    "ingredients": [
      "45 ml 牙买加深色朗姆酒",
      "45 ml 金色波多黎各朗姆酒",
      "30 ml 德梅拉拉朗姆酒",
      "20 ml 新鲜青柠汁",
      "15 ml 法兰恩糖香酒",
      "15 ml Donn’s Mix*（唐氏混合）",
      "1 茶匙 红石榴糖浆",
      "1 滴 安格仕苦精",
      "6 滴 潘诺"
    ],
    "steps": [
      "加入 所有材料 到 an electric blender 加 170 grams of 碎 冰.",
      "With pulse bottom blend for a few seconds. Serve in a tall tumbler 杯.",
      "注：\n*Donn’s Mix：2份新鲜黄葡萄柚汁 + 1份肉桂糖浆。"
    ]
  }
]


def print_header() -> None:
    print("\n=== 鸡尾酒小程序（中文离线版）===")
    print("1) 随机推荐")
    print("2) 按基酒筛选")
    print("3) 按分类筛选")
    print("4) 查看全部酒谱")
    print("0) 退出")


def show_cocktail(cocktail: Dict) -> None:
    print(f"\n--- {cocktail['name']} ---")
    print(f"基酒: {cocktail['base']} | 分类: {cocktail['taste']}")
    print("配料:")
    for item in cocktail["ingredients"]:
        print(f"- {item}")
    print("步骤:")
    for idx, step in enumerate(cocktail["steps"], start=1):
        print(f"{idx}. {step}")


def list_names(cocktails: List[Dict]) -> None:
    if not cocktails:
        print("没有结果。")
        return
    for idx, cocktail in enumerate(cocktails, start=1):
        print(f"{idx}. {cocktail['name']} ({cocktail['base']}, {cocktail['taste']})")


def choose_and_show(cocktails: List[Dict]) -> None:
    if not cocktails:
        print("没有匹配的鸡尾酒。")
        return

    list_names(cocktails)
    selected = input("\n输入编号查看详情（直接回车跳过）: ").strip()
    if not selected:
        return

    if not selected.isdigit():
        print("输入无效。")
        return

    idx = int(selected)
    if idx < 1 or idx > len(cocktails):
        print("编号超出范围。")
        return
    show_cocktail(cocktails[idx - 1])


def random_cocktail(cocktails: List[Dict]) -> None:
    show_cocktail(random.choice(cocktails))


def filter_by_base(cocktails: List[Dict]) -> None:
    bases = sorted({c["base"] for c in cocktails})
    print("\n可选基酒:", "、".join(bases))
    target = input("输入基酒: ").strip()
    result = [c for c in cocktails if c["base"] == target]
    choose_and_show(result)


def filter_by_taste(cocktails: List[Dict]) -> None:
    tastes = sorted({c["taste"] for c in cocktails})
    print("\n可选分类:", "、".join(tastes))
    target = input("输入分类: ").strip()
    result = [c for c in cocktails if c["taste"] == target]
    choose_and_show(result)


def list_all(cocktails: List[Dict]) -> None:
    choose_and_show(cocktails)


def main() -> None:
    cocktails = COCKTAILS
    print(f"已加载 {len(cocktails)} 条鸡尾酒酒谱（内嵌数据）。")

    while True:
        print_header()
        cmd = input("请选择: ").strip()

        if cmd == "1":
            random_cocktail(cocktails)
        elif cmd == "2":
            filter_by_base(cocktails)
        elif cmd == "3":
            filter_by_taste(cocktails)
        elif cmd == "4":
            list_all(cocktails)
        elif cmd == "0":
            print("已退出。")
            break
        else:
            print("未知选项，请重试。")


if __name__ == "__main__":
    main()
