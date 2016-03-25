# encoding:utf-8

import pymongo
import time

class OperateDb():

    def __get_col(self, db_name, col_name):
        client = pymongo.MongoClient()
        collection = client[db_name][col_name]
        return collection

    def read_one(self, db_name, col_name, **kwargs):
        db = self.__get_col(db_name, col_name)
        return db.find_one(kwargs)

    def read_all(self, db_name, col_name, **kwargs):
        db = self.__get_col(db_name, col_name)
        return db.find(kwargs)

    def insert_one(self, db_name, col_name, data_dict):
        db = self.__get_col(db_name, col_name)
        print data_dict
        db.insert(data_dict)





if __name__ == "__main__":
    operate_db = OperateDb()
    start_time = time.time()
    condition = {}
    res = {}
    res = operate_db.read_all("myl", "person_url")
    i = 0
    for x in res:
        i = i + 1
        condition['url'] = x['url']
        res = operate_db.read_one("myl", "person_html", **condition)
        if res["url"]:
            print i
            print res["url"]
        else:
            print x['url']
            print "-----"
            break
    end_time = time.time()
    print end_time - start_time

