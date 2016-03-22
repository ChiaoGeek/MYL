# eccoding:utf-8
# encoding:utf-8
import gevent
import urllib2
import gevent.monkey
import time
from gevent.pool import Pool
import ssl
import requests

gevent.monkey.patch_socket()
gevent.monkey.patch_all()
global i
i = 0
def fetch(url):
    global i
    #print url
    try:
        response = requests.get(url, verify=True, timeout=1)
        res = response.text
        i = i + 1
        #print i
        return res
    except requests.ConnectionError as e:
        print "[ConnectionError]--%s" % url
    except requests.HTTPError as e:
        print "[HTTPError]--%s" % url
    except requests.Timeout as e:
        print "[Timeout]--%s" % url

def synchronous():
    for i in range(20):
        fetch(i)


def asynchronous():

    threads = []
    #for i in range(1,1000):
    #    threads.append(gevent.spawn(fetch, i))
    urls = ['https://mm.taobao.com/json/request_top_list.htm'] * 4000
    pool = Pool(3000)
    r = pool.map(fetch, urls)
    #print r[0]

start = time.time()
print "synchronous:"
#synchronous()
print "asynchronous"
asynchronous()
end = time.time()
print end-start