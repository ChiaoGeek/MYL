# encoding:utf-8
import gevent
import urllib2
import gevent.monkey
import time
from gevent.pool import Pool

gevent.monkey.patch_socket()
gevent.monkey.patch_all()

def fetch(url):
    print url
    request = urllib2.Request(url)
    response = urllib2.urlopen(request, timeout=10)
    res = response.read().decode('gbk')
    print res


def synchronous():
    for i in range(20):
        fetch(i)


def asynchronous():

    threads = []
    #for i in range(1,1000):
    #    threads.append(gevent.spawn(fetch, i))
    urls = ['http://mm.taobao.com/json/request_top_list.htm'] * 10
    pool = Pool(3)
    pool.map(fetch, urls)

start = time.time()
print "synchronous:"
#synchronous()
print "asynchronous"
asynchronous()
end = time.time()
print end-start