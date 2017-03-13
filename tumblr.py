# -*- coding:utf-8 -*-
import time, re, os, urllib.request
from threading import Lock, current_thread, Thread

def main(*args):
    args = ''.join(args)
    print('At',time.ctime(),'开始下载%s'%args)
    url = 'http://%s.tumblr.com/api/read/json?start=0&num=200' %args
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Mobile Safari/537.36')
    data=urllib.request.urlopen(req).read().decode('UTF-8')
    print('%s start at '%args ,time.ctime())
    img = r'photo-url-500":"(.{80,120}500.jpg)'
    video = r'source src=\\"(.{80,130})" type.*video-player-500'
    l = 0
    for i in re.findall(img,data):
        l += 1
        if l >100:
            break
        t = i.replace('\\', '')
        imgfilename = t.split("/")[-1].replace('_500','').replace('_r1','').replace('tumblr','%s'%args)
        print('At',time.ctime(),'Downloadiing %s from userID %s' % (imgfilename, args))
        imgDir = "./etc/img"
        if not os.path.exists(imgDir):
            os.makedirs(imgDir)
        urllib.request.urlretrieve(t, "./etc/img/%s" % imgfilename)
    print('图片已完成下载%s' %args)
    '''
    for v in re.findall(video,data):
        d = v.replace('\\', '')
        videofilename = d.split("/")[-1]
        videofilename += '.mp4'
        print('At',time.ctime(),'Downloadiing %s from %s' % (videofilename, args))
        videoDir = "./etc/mp4"
        if not os.path.exists(videoDir):
            os.makedirs(videoDir)
        urllib.request.urlretrieve(d, "./etc/mp4/%s" % videofilename)
        print('视频已完成下载%s' % args)
'''
def tumblr_id(*args):
    threads = []
    for i in args:
        t = Thread(target=main,
                             args=(i))
        threads.append(t)
    for h in range(len(args)):
        threads[h].start()
    for h in range(len(args)):
        threads[h].join()

if __name__ == '__main__':
    tumblr_id('qiao815')