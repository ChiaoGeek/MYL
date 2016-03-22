# encoding:utf-8
import gevent
from gevent import monkey
from gevent.pool import Pool
import requests
import pymongo
import time

gevent.monkey.patch_socket()
gevent.monkey.patch_all()


class FetcherPush():
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
            mongo_conn = self.__connect("myl", "html")
            insert_id = mongo_conn.insert_one(dict).inserted_id
            print insert_id

        except requests.ConnectionError as e:
            error_dict = {}
            error_dict['url'] = url
            error_dict['error_type'] = 'ConnectionError'

            mongo_conn = self.__connect("myl", "error")
            insert_id = mongo_conn.insert_one(error_dict).inserted_id

            print "[ConnectionError]--%s" % url

        except requests.HTTPError as e:
            error_dict = {}
            error_dict['url'] = url
            error_dict['error_type'] = 'HTTPError'

            mongo_conn = self.__connect("myl", "error")
            insert_id = mongo_conn.insert_one(error_dict).inserted_id

            print "[HTTPError]--%s" % url

        except requests.Timeout as e:
            error_dict = {}
            error_dict['url'] = url
            error_dict['error_type'] = 'Timeout'

            mongo_conn = self.__connect("myl", "error")
            insert_id = mongo_conn.insert_one(error_dict).inserted_id

            print "[Timeout]--%s" % url


    def fetcher(self, urls, pool_num=3000, **kargs):
        pool = Pool(pool_num)
        pool.map(self.__get_request, urls)


if __name__ == "__main__":
    fecher_push = FetcherPush()
    start_time = time.time()
    urls = ["https://mm.taobao.com/json/request_top_list.htm?page=%s" % i for i in range(1,4300)]
    fecher_push.fetcher(urls)
    end_time = time.time()
    print end_time - start_time

