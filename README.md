
# juzimiSpider


![](https://img.shields.io/badge/-python3-brightgreen.svg)
![](https://img.shields.io/badge/-selenuim-yellowgreen.svg)

爬取句子迷中的句子




用Scrapy爬这个网站的时候，发现了一个很有意思的地方。
- 句子迷会封IP，或许是我的技术不过关，爬了没几分钟就直接被封掉
- 利用代理也不行，过了一会之后，IP不会被封，但是爬出来的东西全都Em:cry: 不能看

爬出来的结果是这样

> 鲁迅,鲁迅杂文精选,猛兽比路子是是独于和大，牛羊风这成群结队。

> 汤显祖,牡丹亭,情不知所起，一当小里子当深。

> 泰戈去格,飞鸟集,当你为错过太阳里子当哭泣的时候，你也么种却将夫西错过群星了。

> 七堇年,尘曲,心然时所大这 素履以是自 生如逆旅 一苇以航

> 泰戈得们,生如夏花,生如夏花然时绚烂，死如秋叶然时静美。


呃，这些也暂时没有搞清楚是什么原因，怎么触发的这个机制，怎么解决


这个网站比较简单 就做用selenuim做了一个爬虫，比较顺利，没被封IP，也没有这种加盐的操作。
![爬取出来的结果](https://i.loli.net/2019/04/29/5cc640aeb6c8d.png)
![爬取出来的结果](https://i.loli.net/2019/04/29/5cc6414048a37.png)

