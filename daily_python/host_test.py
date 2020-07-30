#!/usr/bin/env python
# -*- encoding:utf-8 -*-
import sys
import urllib2, sys, platform

reload(sys)
sys.setdefaultencoding('utf-8')


url = 'http://www.360kb.com/kb/2_150.html'
if platform.uname()[0] == 'Windows':
    file = r'c:\windows\system32\drivers\etc\hosts'
else:
    file = r'/etc/hosts'
data = urllib2.urlopen(url, None, 10).read()
if data is not None:
    a = data.find('#google-hosts-2015')
    #    b=data.find('#google-hosts-2015-end')

    b = data.find('</pre>')
    if a == -1 or b == -1:
        sys.exit(-1)
    # back hosts
    # shutil.copyfile(file,'%s.bak-%s'%(file,time.strftime('%Y%m%d%H%M%S')))
    # write hosts
    fpr = open(file, 'r')
    lines = fpr.readlines()
    fpr.close()
    fpw = open(file, 'w')
    flag = 0
    data = data[a:b].split("\n")
    for eachLine in lines:
        if "google-hosts" in eachLine:
            if flag == 0:
                for eachData in data[:-3]:
                    fpw.write(
                        eachData.replace('<br />', '').replace('&nbsp;', '').replace('<span>', '').replace('</span>',
                                                                                                           '') + "\n")
                    if data.index(eachData) == 2:
                        fpw.write(eachData[0:18] + "google.com.hk" + "\n")
                fpw.write(data[-2].replace('<br />', ''))
            flag += 1
        elif flag != 1:
            fpw.write(eachLine)
    if flag == 0:
        fpw.write(data[a:b].replace('<br />', ''))
    fpw.close()
    print
    'ok'
else:
    print
    'url not found'
raw_input()