"""
pyecharts演示
"""

# 导包
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# 生成 line 对象
line = Line()

# 给 line 对象添加 x 轴数据
line.add_xaxis(['中国','美国', '英国'])

# 给 line 对象添加 y 轴数据
line.add_yaxis('GDP',[30,20,10])

# 设置全局配置项
line.set_global_opts(
    title_opts= TitleOpts(title='GDP展示',pos_right='center', pos_top='2%'),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
)
# 使用 render 方法，生成图像
line.render()
