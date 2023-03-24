# 例如我们要存储两个list：name_list 和 err_list 到 Excel 两列
# name_list和err_list均已存在
name_list = [10, 20, 30]  # 示例数据
err_list = [0.99, 0.98, 0.97]  # 示例数据

# 导包，如未安装，先 pip install xlwt
import xlwt

data = [
    {
        "rating": [
            "7.9",
            "40"
        ],
        "rank": 332,
        "cover_url": "https://img1.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2192369280.jpg",
        "is_playable": False,
        "id": "1439205",
        "types": [
            "动画"
        ],
        "regions": [
            "日本"
        ],
        "title": "熊猫家族",
        "url": "https:\/\/movie.douban.com\/subject\/1439205\/",
        "release_date": "1972-12-17",
        "actor_count": 19,
        "vote_count": 15084,
        "score": "7.9",
        "actors": [
            "杉山佳寿子",
            "熊仓一雄",
            "太田淑子",
            "山田康雄",
            "濑能里子",
            "市川治",
            "丸山裕子",
            "梶哲也",
            "柯克·桑顿",
            "莫娜·马歇尔",
            "道格·斯通",
            "史蒂夫·克莱默",
            "Melissa Fahn",
            "布瑞安·西尔多",
            "W.T. Hatch",
            "芭芭拉·古德森",
            "Julie Maddalena",
            "Chet Huntley",
            "Jake Martin"
        ],
        "is_watched": False
    },
    {
        "rating": [
            "8.2",
            "45"
        ],
        "rank": 333,
        "cover_url": "https://img2.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2315133763.jpg",
        "is_playable": True,
        "id": "20278795",
        "types": [
            "剧情",
            "动画",
            "冒险"
        ],
        "regions": [
            "法国",
            "丹麦"
        ],
        "title": "漫漫北寻路",
        "url": "https:\/\/movie.douban.com\/subject\/20278795\/",
        "release_date": "2015-06-16",
        "actor_count": 9,
        "vote_count": 11524,
        "score": "8.2",
        "actors": [
            "克丽丝塔·特瑞特",
            "费奥多尔·阿特金",
            "安东尼·希克林",
            "卢瓦克·乌德雷",
            "克洛伊·唐",
            "托马斯·萨果斯",
            "安德丽·萨宾",
            "雷米·卡里比特",
            "凯斯特·洛夫莱斯"
        ],
        "is_watched": False
    },
]
# 设置Excel编码
file = xlwt.Workbook('encoding = utf-8')

# 创建sheet工作表
sheet1 = file.add_sheet('sheet1', cell_overwrite_ok=True)
obj = data[0]
key_list = list(obj.keys())
for i in range(len(obj)):
    # 先填标题
    # sheet1.write(a,b,c) 函数中参数a、b、c分别对应行数、列数、单元格内容
    # sheet1.write(0, 0, "序号")  # 第1行第1列
    # sheet1.write(0, 1, "数量")  # 第1行第2列
    # sheet1.write(0, 2, "误差")  # 第1行第3列
    sheet1.write(0, i, key_list[i])
    print("i=" + str(i) + "key_list=" + key_list[i])
#
# # 循环填入数据
for i in range(len(data)):
    # sheet1.write(i + 1, 0, i)  # 第1列序号
    # sheet1.write(i + 1, 1, name_list[i])  # 第2列数量
    # sheet1.write(i + 1, 2, err_list[i])  # 第3列误差
    # 1.获取list中第i个元素，元素类型为字典
    dict_obj = data[i]
    # 2.获取字典所有值
    value_list = list(dict_obj.values())
    k = i + 1
    for j in range(len(dict_obj)):
        # sheet1.write(i + 1, 0, i)
        # sheet1.write(i + 1, 1, name_list[i])
        sheet1.write(k, j, value_list[j])
# # 保存Excel到.py源文件同级目录
file.save('Data.xls')
