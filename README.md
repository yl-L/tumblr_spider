# python3 tumblr多线程爬虫
>给定 tumblr 用户的 username ，下载图片以及视频资源。  
>声明一下:这是一个正经的爬虫，所爬取的资源跟你填入的 username 有关系，请勿随意开车。  
>另外，由于tumblr被墙，请使用代理爬取。
# 资源存储
>图片存放在tumblr.py所在文件夹下的/etc/img中，修改imgDir即可修改文件存放位置。  
>视频存放在tumblr.py所在文件夹下的/etc/mp4中，修改videoDir即可修改文件存放位置。
# 运行
>python tumblr.py username1[,username2,username3...]
# import
>import tumblr  
>tumblr.tumblr_id('username1,username2,username3...')
