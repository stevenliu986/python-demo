import json
from pyecharts.charts import Line
from pyecharts import options as opts

# 1. 使用 with 语句，优雅、安全地读取所有文件
try:
    with open('美国.txt', 'r', encoding='utf-8') as f:
        us_data = f.read()
    with open('日本.txt', 'r', encoding='utf-8') as f:
        jp_data = f.read()
    with open('印度.txt', 'r', encoding='utf-8') as f:
        in_data = f.read()
except FileNotFoundError as e:
    print(f"文件读取失败，请检查文件名或路径是否正确：{e}")
    exit(1)


# 2. 编写一个通用的安全清洗函数：动态寻找 ( 和 ) 的位置
def clean_jsonp(raw_data):
    # 找到第一个左括号的位置
    left_bracket = raw_data.find('(')
    # 找到最后一个右括号的位置
    right_bracket = raw_data.rfind(')')

    if left_bracket != -1 and right_bracket != -1:
        # 刚好切出括号内部的纯正 JSON 字符串
        return raw_data[left_bracket + 1 : right_bracket]
    return raw_data


us_data = clean_jsonp(us_data)
jp_data = clean_jsonp(jp_data)
in_data = clean_jsonp(in_data)

# 3. 解析 JSON 字典
try:
    us_dict = json.loads(us_data)
    jp_dict = json.loads(jp_data)
    in_dict = json.loads(in_data)
except json.JSONDecodeError as e:
    print(f"JSON 解析失败！数据清洗可能损坏了结构：{e}")
    exit(1)

# 4. 提取 trend 数据
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']

# 5. 提取 x 轴和 y 轴数据 (截取前 314 天)
us_x_data = us_trend_data['updateDate'][:314]

us_y_data = us_trend_data['list'][0]['data'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]

# 6. 配置并生成折线图
line = Line()
line.add_xaxis(us_x_data)

# 关掉折线上的数字标签（label_opts），防止 900 多个数字把图表挤爆
line.add_yaxis(
    "美国2020年新冠确诊人数", us_y_data, label_opts=opts.LabelOpts(is_show=False)
)
line.add_yaxis(
    "日本2020年新冠确诊人数", jp_y_data, label_opts=opts.LabelOpts(is_show=False)
)
line.add_yaxis(
    "印度2020年新冠确诊人数", in_y_data, label_opts=opts.LabelOpts(is_show=False)
)

# 加上全局标题配置
line.set_global_opts(
    title_opts=opts.TitleOpts(title="2020年美、日、印三国新冠确诊人数趋势对比")
)

# 渲染生成 HTML 文件
line.render("covid_trend_comparison.html")
print("🎉 恭喜！图表已成功渲染至 covid_trend_comparison.html")