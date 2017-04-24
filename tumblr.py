# -*- coding:utf-8 -*-
import time, re, os, urllib.request,sys
from threading import Lock, current_thread, Thread

def main():
    username = []
    for i in range(1,len(sys.argv)):
        username.append(sys.argv[i])
        print(' '.join(username))
    tumblr_id(username)
def download(args):
    print('At',time.ctime(),'开始下载%s'%args)
    url = 'http://%s.tumblr.com/api/read/json?start=0&num=200' %args
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Mobile Safari/537.36')
    data=urllib.request.urlopen(req).read().decode('UTF-8')
    print('%s start at '%args ,time.ctime())
    img = r'photo-url-500":"(.{80,120}500.jpg)'#正则表达式匹配图片
    video = r'source src=\\"(.{80,130})" type.*video-player-500'#正则表达式匹配图片
    l = 0
    for i in re.findall(img,data):#图片下载
        l += 1
        if l >100:#判断下载100张图片跳出循环
            break
        t = i.replace('\\', '')#替换转义字符
        imgfilename = t.split("/")[-1].replace('_500','').replace('_r1','').replace('tumblr','%s'%args)#分割并修改保存的文件名
        print('At',time.ctime(),'Downloadiing %s from userID %s' % (imgfilename, args))
        imgDir = "./etc/img/"
        if not os.path.exists(imgDir):#判断路径是否存在
            os.makedirs(imgDir)
        urllib.request.urlretrieve(t, "%s%s" %(imgDir,imgfilename))
    print('图片已完成下载%s' %args)

    for v in re.findall(video,data):#视频下载
        d = v.replace('\\', '')
        videofilename = d.split("/")[-1]
        videofilename += '.mp4'
        print('At',time.ctime(),'Downloadiing %s from %s' % (videofilename, args))
        videoDir = "./etc/mp4/"
        if not os.path.exists(videoDir):
            os.makedirs(videoDir)
        urllib.request.urlretrieve(d, "%s%s" %(videoDir,videofilename))
        print('视频已完成下载%s' % args)

def tumblr_id(*args):
    args = str(args).strip("[]',)(").split(',')#修改输入的username字符串
    threads = []
    for i in args:#threading多线程下载
        t = Thread(target=download,
                             args=(i,))
        threads.append(t)
    for h in range(len(args)):
        threads[h].start()
    for h in range(len(args)):
        threads[h].join()

if __name__ == '__main__':
    main()
