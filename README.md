# model
相关的算法模型与数据爬虫

## 获取数据集

```shell
python get_dataset.py
```
该脚本会自动爬取一系列电影的豆瓣和猫眼评论信息(带评分标签)

你需要在config.json中配置相关信息:

```json
{
    "cookies":"XXXX",  // 豆瓣cookies(豆瓣不登录评论仅限前200多条)
    "tmp_path":"./tmp",  //电影临时评论的输出文件夹,默认为tmp
    "output_file":"res.xlsx", //最终的全部数据文件,默认为res
    "douban":[36208094,34951373], // 要爬取的豆瓣电影id
    "maoyan":[43] // 同理的猫眼电影id
}
```

