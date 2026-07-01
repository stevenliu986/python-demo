import json
from pyecharts import options as opts
from pyecharts.charts import Map


def get_clean_china_map_data(file_path):
    """读取疫情数据并清洗出符合 pyecharts 地图命名规范的数据列表"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = file.read()
    except FileNotFoundError:
        print(f"❌ 找不到 '{file_path}' 文件，请检查路径！")
        return None

    # 1. 转换为 python 字典
    try:
        covid_data = json.loads(data)
    except json.JSONDecodeError:
        print("❌ JSON 格式解析失败，请检查文件内容是否完整！")
        return None

    # 2. 过滤出各个省份的数据并自动补全“省/市/自治区/特别行政区”后缀
    provinces_list = []
    provinces = covid_data["areaTree"][0]["children"]

    # 映射表，用于精确匹配和修复少数民族自治区
    autonomous_regions = {
        "新疆": "新疆维吾尔自治区",
        "西藏": "西藏自治区",
        "内蒙古": "内蒙古自治区",
        "宁夏": "宁夏回族自治区",
        "广西": "广西壮族自治区",
    }
    municipalities = ["北京", "上海", "天津", "重庆"]
    special_zones = ["香港", "澳门"]

    for province in provinces:
        name = province["name"]  # 原始名字，例如 "广东"
        confirm_cases = province["total"]["confirm"]  # 确诊人数

        # ---- 核心修复：将简称转换为 pyecharts 认识的标准全称 ----
        if name in municipalities:
            name += "市"
        elif name in autonomous_regions:
            name = autonomous_regions[name]
        elif name in special_zones:
            # 香港、澳门、台湾在 pyecharts 内部直接使用简称即可匹配
            pass
        else:
            # 普通省份如果结尾没有“省”，则补上
            if not name.endswith("省"):
                name += "省"
        # ------------------------------------------------------

        provinces_list.append((name, confirm_cases))

    return provinces_list


def generate_covid_map():
    # 获取清洗后的标准数据
    provinces_data = get_clean_china_map_data("疫情.txt")
    if not provinces_data:
        return

    # =====================================================================
    # 3. 创建大尺寸的地图对象
    # =====================================================================
    # 通过 width 和 height 放大画布，彻底解决地图缩在一团、名字挤在一起的问题
    covid_map = Map(init_opts=opts.InitOpts(width="1200px", height="800px"))

    covid_map.add(
        series_name="累计确诊人数",
        data_pair=provinces_data,
        maptype="china",
        # is_roam=True 允许用户在生成的 HTML 网页中通过鼠标滚轮放大、缩小以及拖拽地图
        is_roam=True,
        # 隐藏静态显示在地图上的标签，鼠标悬停到省份上时会自动高亮并弹出确诊数字
        label_opts=opts.LabelOpts(is_show=False),
    )

    # =====================================================================
    # 4. 全局配置项（加入标题和视觉映射染色组件）
    # =====================================================================
    covid_map.set_global_opts(
        title_opts=opts.TitleOpts(
            title="中国各省份新冠肺炎累计确诊地图",
            pos_left="center",
            pos_top="20px",
        ),
        # 视觉映射配置：根据确诊人数给各省份渲染深浅不一的红色
        visualmap_opts=opts.VisualMapOpts(
            is_piecewise=True,  # 是否分段显示颜色
            pos_left="10%",
            pos_bottom="10%",
            # 分段区间：如果你的数据更大，可以继续调大第一档的 min 值
            pieces=[
                {"min": 10000, "label": ">= 10000 人", "color": "#7f1100"},
                {"min": 1000, "max": 9999, "label": "1000 - 9999 人", "color": "#bd1316"},
                {"min": 500, "max": 999, "label": "500 - 999 人", "color": "#e64b45"},
                {"min": 100, "max": 499, "label": "100 - 499 人", "color": "#fde8cd"},
                {"min": 1, "max": 99, "label": "1 - 99 人", "color": "#ffe8db"},
                {"value": 0, "label": "0 人", "color": "#ffffff"},
            ],
        ),
    )

    # 5. 渲染生成网页文件
    output_filename = "covid_confirm_cases.html"
    covid_map.render(output_filename)
    print(f"🎉 地图已成功渲染！请在项目目录下用浏览器打开 '{output_filename}' 查看。")


if __name__ == "__main__":
    generate_covid_map()