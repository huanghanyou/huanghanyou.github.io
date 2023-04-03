from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType, GeoType

geo = Geo()


geo.add_coordinate(name="America", longitude=-116.231, latitude=40.220)
geo.add_coordinate(name='Australia', longitude=144.58, latitude=-37.50)
geo.add_coordinate(name="England", longitude=0.15, latitude=51.30)
geo.add_coordinate(name="Canada", longitude=-79.23, latitude=45.39)
geo.add_coordinate(name="Japan", longitude=139.69, latitude=35.69)
geo.add_coordinate(name="German", longitude=13.2, latitude=52.31)
geo.add_coordinate(name="Russia", longitude=37.6178, latitude=55.7558)
geo.add_coordinate(name="France", longitude=2.25, latitude=48.52)
geo.add_coordinate(name="New Zealand", longitude=174, latitude=-41)
geo.add_coordinate(name="China", longitude=116.3, latitude=39.9)

geo.add_schema(maptype="world")

geo.add("单位：万人",
        [('America', 37.25),
         ("Australia", 16.58),
         ("England", 12.9),
         ("Canada", 9.86),
         ("Japan", 9.4),
         ("German", 3.99),
         ("Russia", 3.75),
         ("France", 2.84),
         ('New Zealand', 2.00),
         ('China',106.511)
         ],
        type_=ChartType.EFFECT_SCATTER)

geo.add("留学去向",
        [('China', 'America'),
         ('China', "Australia"),
         ('China', "England"),
         ('China', "Canada"),
         ('China', "Japan"),
         ('China', "German"),
         ('China', "Russia"),
         ('China', "France"),
         ('China', 'New Zealand'),
         ],
        type_=GeoType.LINES,
        effect_opts=opts.EffectOpts(symbol=SymbolType.ARROW,
                                    symbol_size=5, color="yellow"),
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
        )

geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=40),
                    title_opts=opts.TitleOpts(title="2019年中国留学生去向前九国家"))

geo.render('./output/out_country.html')