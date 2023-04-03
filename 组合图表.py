from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Liquid, Page, Pie
from pyecharts.components import Table


def bar_datazoom_slider() -> Bar:
    c = (
        Bar()
        .add_xaxis(["{}日".format(i) for i in range(1, 31)])
        .add_yaxis("单位：摄氏度",
                   [24, 23, 22, 20, 18, 15, 16, 22, 17, 24, 17, 18, 16, 19, 24, 16, 17,
                    16, 14, 15, 17, 17, 18, 18, 19, 18, 18, 19, 23, 21])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="四月北京未来30天最高气温预测）"),
            datazoom_opts=[opts.DataZoomOpts()],
        )
    )
    return c


def line_markpoint() -> Line:
    c = (
        Line()
        .add_xaxis(['周一', '周二', '周三', '周四', '周五'])
        .add_yaxis(
            "周上课时长",
            [3.00, 6.67, 1.67, 3.33, 1.67],
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min")]),
        )
        .add_yaxis(
            "周玩抖音时长",
            [3.38, 3.05, 3.17, 5.30, 2.28],
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="学习和娱乐（第六周）"))
    )
    return c


def pie_rosetype() -> Pie:
    v = ['舞蹈', '音乐', '沙雕', '摄影', '影视剧', '帅哥美女', '新闻']
    c = (
        Pie()
        .add(
            "",
            [list(z) for z in zip(v, [0.0809, 0.1593, 0.3995, 0.1324, 0.0662, 0.1544, 0.0833])],
            radius=["30%", "75%"],
            center=["25%", "50%"],
            rosetype="radius",
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add(
            "",
            [list(z) for z in zip(v, [0.0809, 0.1593, 0.3995, 0.1324, 0.0662, 0.1544, 0.0833])],
            radius=["30%", "75%"],
            center=["75%", "50%"],
            rosetype="area",
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="我的抖音点赞视频取向"))
    )
    return c


def grid_mutil_yaxis() -> Grid:
    x_data = ["前{}月".format(i) for i in range(12, 0, -1)]
    bar = (
        Bar()
        .add_xaxis(x_data)
        .add_yaxis(
            "通货膨胀率",
            [8.5, 8.3, 8.6, 9.1, 8.5, 8.3, 8.2, 7.7, 7.1, 6.5, 6.4, 6],
            yaxis_index=0,
            color="#d14a61",
        )
        .add_yaxis(
            "居民消费指数CPI",
            [287.504, 289.109, 292.296, 296.311, 296.276, 296.171, 296.808, 298.012, 297.711, 296.797, 299.17, 300.84],
            yaxis_index=1,
            color="#5793f3",
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                name="居民消费指数CPI",
                type_="value",
                min_=280,
                max_=310,
                position="right",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#5793f3")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value}"),
            )
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                type_="value",
                name="月首US500指数",
                min_=3500,
                max_=4600,
                position="left",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#675bba")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value}"),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                ),
            )
        )
        .set_global_opts(
            yaxis_opts=opts.AxisOpts(
                name="通货膨胀率",
                min_=5,
                max_=9.5,
                position="right",
                offset=80,
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#d14a61")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value}%"),
            ),
            title_opts=opts.TitleOpts(title="美国近12个月的金融概况"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        )
    )

    line = (
        Line()
        .add_xaxis(x_data)
        .add_yaxis(
            "月首US500指数",
            [4545.86, 4155.38, 4101.23, 3825.33, 4118.63, 3966.85,
             3687.73, 3856.1, 4076.57, 3839.5, 4119.21, 3951.39],
            yaxis_index=2,
            color="#675bba",
            label_opts=opts.LabelOpts(is_show=False),
        )
    )

    bar.overlap(line)
    return Grid().add(
        bar, opts.GridOpts(pos_left="5%", pos_right="20%"), is_control_axis_index=True
    )


def liquid_data_precision() -> Liquid:
    c = (
        Liquid()
        .add(
            "lq",
            [0.27],
            label_opts=opts.LabelOpts(
                font_size=50,

                position="inside",
            ),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="3.30北京海淀区湿度"))
    )
    return c


def table_base() -> Table:
    table = Table()

    headers = ["日", "抖音", "微信", "QQ"]
    rows = [
        ["3.24", 2.17, 5.14, 0.15],
        ["3.25", 0.35, 2.44, 0.09],
        ["3.26", 3.27, 1.28, 0.12],
        ["3.27", 3.23, 2.50, 0.29],
        ["3.28", 3.03, 2.18, 0.30],
        ["3.29", 3.10, 3.46, 0.59],
        ["3.30", 5.18, 1.41, 0.33],
    ]
    table.add(headers, rows).set_global_opts(
        title_opts=opts.ComponentTitleOpts(title="前三应用使用时长（时.分）")
    )
    return table


def page_draggable_layout():
    page = Page(layout=Page.DraggablePageLayout)
    page.add(
        grid_mutil_yaxis(),
        line_markpoint(),
        pie_rosetype(),
        table_base(),
        bar_datazoom_slider(),
        liquid_data_precision(),
             )
    page.render("./output/contain.html")


if __name__ == "__main__":
    page_draggable_layout()
