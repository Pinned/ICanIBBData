## Python 爬取数据并进行分析

> 本项目仅作学习之用，如有侵权，请联系作者删除。谢谢。

### 0x 01 数据库创建

代码参见：[DataBaseCreater.py](DataBaseCreater.py)

> 因Demo写得比较简单，所以只需要执行一次创建就OK了。
> 数据库创建了两个文件: [i_can_i_bb.db](i_can_i_bb.db) --- 存储原始数据, [deal_data.db](deal_data.db) --- 存储处理过的数据

### 获取爱奇艺评论接口数据并存储

代码参见：[GetICanIBBData.py](GetICanIBBData.py)

> 代码没有处理重复数据合并，且没有处理更新逻辑，如果你有兴趣完善，欢迎提交`Pull Request`

### 将原始数据清洗并存储

将原始数据中需要的字段拿出来存储到 `deal_data`中
代码参见: [ConvertData.py](ConvertData.py)

### 性别比数据并输出餅图

代码参见: [UserSex.py](UserSex.py)

###  每一期评论数量

将movieId更新到 `deal_data.bd`中
代码参见: [ConvertMovieId.py](ConvertMovieId.py)

显示评论柱状图：
代码参见: [UserCommentCount.py](UserCommentCount.py)

### 周评论数据

1. 将日期数据转换成周并存储在 `deal_data.db` 中
代码参见: [ConvertWeek.py](ConvertWeek.py)
2. 展示周评论数据
代码参见:  [UserCommentDate.py](UserCommentDate.py)

### 用户评论“字数长度”

1. 更新长度范围并存储在 `deal_data.db` 中
代码参见: [ConvertCommentLength.py](ConvertCommentLength.py)
2. 显示评论字数长度
代码参见： [UserCommentLength.py](UserCommentLength.py)

### 词云

使用 jieba 进行分词，并使用 wordcloud 来生成词云图
代码参见：[UserCommentJieba.py](UserCommentJieba.py)