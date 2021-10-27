### 金融数据爬虫项目

------------------------------------------

**项目描述**

​		从公开的新浪财经、东方财富等财经类网站爬取A股全市场每只个股的日线行情（包括高开低收价格以及成交量、成交额等统计数据）



**具体要求**

- 设计爬虫，在财经类网站爬取尽可能多的历史行情数据；部署实盘服务，每天定时爬取当天的数据。
- 在Jupyter notebook或Jupyter lab中对上述数据进行简单聚合分析



### 文件说明

------------------------

```python
Stock_market
|
|	data_format.txt		# 爬虫获取到的数据格式
|	Diary.md		# 工程日志 记录完成project的记录
|	README.md	
|
|-----------current			# 实时股票大盘
|		|
|		|	connect.py		# 获取数据库连接
| 		|  	get_stocks.py		# 爬虫获取A股大盘数据
|		|	query.py		# 主查询程序
|		|	stock.sql		# 数据库相关语句
|		|	tools.py		# 股票操作tools
|		|	update_details.py	# 更新数据库
|		|
|		|-----------web		# 实盘网页部署
|			|
|			|	app.py		#网页部署主程序
|			|	get_stocks.py 	# 获取股票信息相关函数
|			|	utils.py	# 获取网页实时更新数据相关函数
|			|
|			|--------static		# CSS与Javascript
|			|
|			|--------templates	# HTML
|
|-----------history		# 个股历史数据
|		|
|		| 	get_stock_history.py	# 获取个股历史数据demo
|		|	tools.py		# 对历史数据的相关操作tools
|		|	test_history.ipynb		# jupyter notebook分析数据
|
|-----------log		# Diary.md与README.md中的图片
```



### 实现效果

---------

* **大盘数据爬取与入库：**对于大盘数据，在爬虫获取后存入服务器端的数据库里，并设置周一至周五每天9:00-12:00/13:00-15:00每30min更新一次（若需要更频繁的数据可修改服务器中配置），登录mysql查看数据情况如下：

  ![image-20211026001012869](/log/image-20211026001012869.png)

* **网页部署实盘数据：**编写网页显示数据库中大盘股票的情况，并展示当前高开低走、涨停与跌停的股票，以及涨停与跌停的股票支数，以便直观了解大盘行情。网页中使用ajax实时获取涨跌停股票指数与界面时间，通过刷新网页可获得实时股票数据信息。网页界面如下：

  ![image-20211026001540634](/log/image-20211026001540634.png)

* 股票大盘分析操作：除了在网页上部署相应实时信息，本项目还在/current/tools.py中定义了四个接口函数，在运行/current/query.py中可直接调用进行分析

  > 1. 获取代码为code的股票行情信息get_stock_info(code)
  > 2. 获取当前全部涨停股票信息get_rise_limit()
  > 3. 获取当前全部跌停股票信息get_drop_limit()
  > 4. 获取当前涨跌股票支数get_rise_drop_num()

* **指定时间历史数据获得：**历史数据通过jupyter notebook进行分析，使用编写好的函数接口可以获得某股（此处使用浦发银行sh600000为例）近N天或某段时间内每一天的开盘价/收盘价/最高价/最低价/成交量，以DataFrame的形式展示：

  ![image-20211027234308682](/log/image-20211027234308682.png)

  ![image-20211027234230673](/log/image-20211027234230673.png)

  

* 获取个股成交量最多的一天的信息：使用接口get_maxVol()

  ![image-20211027234346480](/log/image-20211027234346480.png)

* **K线均线及成交量柱状图绘制：**调用mpf包中candlestick2_ochl函数绘制历史数据的K线图，使用matplotlib绘制交易量柱状图，并使用红绿双色代表涨跌情况：

  ![image-20211027234001372](/log/image-20211027234001372.png)

* 个股最高价最低价走势图绘制：使用matplotlib绘制某股一段时间内的最高价与最低价走势折线图

  ![image-20211027234435366](/log/image-20211027234435366.png)

* 个股每日涨跌走势图绘制：使用matplotlib绘制某股一段时间内涨跌的走势折线图

  ![image-20211027234556441](/log/image-20211027234556441.png)

