# encoding:utf-8
import gevent
from gevent import monkey
from gevent.pool import Pool
import requests
import pymongo
import time
from operate_db import OperateDb

gevent.monkey.patch_socket()
gevent.monkey.patch_all()


class FetcherPush(OperateDb):
    """
    done
    """

    def __init__(self):
        pass

    def __connect(self, db_name, col_name):
        client = pymongo.MongoClient()
        return client[db_name][col_name]

    #把数据抓取下来并且存入到数据库中
    def __get_request(self, url, **kargs):
        try:
            #爬取数据构造字典
            print "%s starting" %url
            r = requests.get(url, **kargs)
            dict = {}
            dict['url'] = url
            dict['html'] = r.text
            #插入数据库
            self.insert_one("myl", "person_html", dict)
            print "%s end" %url

        except requests.ConnectionError as e:
            error_dict = {}
            error_dict['url'] = url
            error_dict['error_type'] = 'ConnectionError'

            id = self.insert_one("myl", "person_error", error_dict)

            print "[ConnectionError]--%s" % url

        except requests.HTTPError as e:
            error_dict = {}
            error_dict['url'] = url
            error_dict['error_type'] = 'HTTPError'

            id = self.insert_one("myl", "person_error", error_dict)

            print "[HTTPError]--%s" % url

        except requests.Timeout as e:
            error_dict = {}
            error_dict['url'] = url
            error_dict['error_type'] = 'Timeout'

            id = self.insert_one("myl", "person_error", error_dict)

            print "[Timeout]--%s" % url


    def fetcher(self, urls, pool_num=3000, **kargs):
        pool = Pool(pool_num)
        pool.map(self.__get_request, urls)

"""
if __name__ == "__main__":
    fecher_push = FetcherPush()
    start_time = time.time()
    res = fecher_push.read_all("myl", "person_error")
    urls = []
    for x in res:
        urls.append(x["url"])


    #urls = ["https://mm.taobao.com/json/request_top_list.htm?page=%s" % i for i in range(1,2000)]
    fecher_push.fetcher(urls)
    #print urls
    end_time = time.time()
    print end_time - start_time
"""

