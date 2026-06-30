import json
from pyecharts import options as opts
from pyecharts.charts import Line


# 1. 抽取核心复用函数：负责把一个原始文本文件直接变成干净的趋势数据字典
def load_country_trend(file_path):
    """读取国家文本数据并解析出 trend 字典"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            raw_data = f.read()
    except FileNotFoundError:
        print(f"❌ 找不到文件: {file_path}")
        return None

    # 动态定位括号，清洗 jsonp
    left = raw_data.find("(")
    right = raw_data.rfind(")")
    if left == -1 or right == -1:
        print(f"⚠️ 文件 {file_path} 格式异常，未找到 JSONP 括号")
        return None

    json_str = raw_data[left + 1 : right]

    # 解析 JSON 并直接提取到 ['trend'] 层级
    try:
        data_dict = json.loads(json_str)
        return data_dict["data"][0]["trend"]
    except (json.JSONDecodeError, KeyError, IndexError) as e:
        print(f"❌ 解析文件 {file_path} 失败，可能数据结构有误: {e}")
        return None


# =====================================================================
# 2. 主流程：调用函数获取各个国家的趋势数据
# =====================================================================
us_trend = load_country_trend("美国.txt")
jp_trend = load_country_trend("日本.txt")
in_trend = load_country_trend("印度.txt")

# 确保所有数据都加载成功再继续，防止后续代码空指针崩溃
if not (us_trend and jp_trend and in_trend):
    print("由于部分数据加载失败，程序终止。")
    exit(1)

# 3. 提取 X 轴和 Y 轴数据 (统一截取前 314 天)
# 因为日期大家都一样，X 轴拿一份即可
x_data = us_trend["updateDate"][:314]

us_y_data = us_trend["list"][0]["data"][:314]
jp_y_data = jp_trend["list"][0]["data"][:314]
in_y_data = in_trend["list"][0]["data"][:314]

# 4. 配置并生成折线图
line = Line()
line.add_xaxis(x_data)

# 统一隐藏折线数字
label_config = opts.LabelOpts(is_show=False)
line.add_yaxis("美国2020年新冠确诊人数", us_y_data, label_opts=label_config)
line.add_yaxis("日本2020年新冠确诊人数", jp_y_data, label_opts=label_config)
line.add_yaxis("印度2020年新冠确诊人数", in_y_data, label_opts=label_config)

# 全局配置
line.set_global_opts(
    title_opts=opts.TitleOpts(title="2020年美、日、印三国新冠确诊人数趋势对比")
)

# 渲染
line.render("covid_trend_clean.html")
print("🎉 图表已成功复用并渲染至 covid_trend_clean.html")