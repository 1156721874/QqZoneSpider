1、次爬虫对爬取的QQ用户数量通过com.qq.qzone.user.QzoneSpider的maxQQCount控制，使用时可以设置次数量，比如需要
10000个QQ用户的资料，那么maxQQCount=10000。
2、qqlist.txt文件存放当前QQ的所属的所有QQ列表，注意初始化时最后一行必须换行，即敲一下“enter”键。
3、初始化当前QQ空间主页地址：
com.qq.qzone.user.QzoneSpider的login的方法第一行设置当前QQ的主页。
4、本爬虫只在Windows下测试，需要电脑登录qq，然后在运行爬虫
5、默认开发使用的是chrome浏览器。
