# encoding:utf-8
from operate_db import OperateDb
from lxml import etree


class GetContent(OperateDb):
    """
    解析HTML网页并将内容存储
    """


    def __html_to_etree(self, html_str):
        return etree.HTML(html_str)

    #生成XPATH
    def __get_xpath(self, html_str, xpath_condition):
        html_etree = self.__html_to_etree(html_str)
        res = html_etree.xpath(xpath_condition)
        return res

    #获取索引页的文字链接并入库
    def get_index_href(self, html_str, xpath_condition):
        target = self.__get_xpath(html_str, xpath_condition)
        for url in target:
            data_dic = {}
            data_dic["url"] =  "https:" + url
            id = self.insert_one("myl", "person_url", data_dic)
            print id

    def get_all(self,html_str, url ,**condition):
        dict = {}
        dict["url"] = url
        for key, value in condition.items():
            res = self.__get_xpath(html_str, "//div[@class='mm-p-model-info-left-top']/ul/li[1]")
            dict[key] = 1
            print res
        print html_str







if __name__ == "__main__":

    condition = {}
    condition["name"] = "/html/body/div[@class='mm-g-wrap clearfix']/div[@id='J_MmInfo']/div[@class='mm-p-middle mm-p-sheShow']/div[@class='mm-p-info mm-p-base-info']/ul[@class='mm-p-info-cell clearfix']/li[1]/span/text()"
    condition["city"] = "/html/body/div[@class='mm-g-wrap clearfix']/div[@id='J_MmInfo']/div[@class='mm-p-middle mm-p-sheShow']/div[@class='mm-p-info mm-p-base-info']/ul[@class='mm-p-info-cell clearfix']/li[@class='mm-p-cell-right'][1]/span/text()"
    condition["birthday"] = "/html/body/div[@class='mm-g-wrap clearfix']/div[@id='J_MmInfo']/div[@class='mm-p-middle mm-p-sheShow']/div[@class='mm-p-info mm-p-base-info']/ul[@class='mm-p-info-cell clearfix']/li[@class='mm-p-cell-left'][1]/span/text()"
    condition["profession"] = "/html/body/div[@class='mm-g-wrap clearfix']/div[@id='J_MmInfo']/div[@class='mm-p-middle mm-p-sheShow']/div[@class='mm-p-info mm-p-base-info']/ul[@class='mm-p-info-cell clearfix']/li[@class='mm-p-cell-left'][2]/span/text()"
    condition["blood"] = "/html/body/div[@class='mm-g-wrap clearfix']/div[@id='J_MmInfo']/div[@class='mm-p-middle mm-p-sheShow']/div[@class='mm-p-info mm-p-base-info']/ul[@class='mm-p-info-cell clearfix']/li[@class='mm-p-cell-right'][2]/label/text()"
    condition["school"] = "/html/body/div[@class='mm-g-wrap clearfix']/div[@id='J_MmInfo']/div[@class='mm-p-middle mm-p-sheShow']/div[@class='mm-p-info mm-p-base-info']/ul[@class='mm-p-info-cell clearfix']/li[6]/span/text()"
    condition["type"] = "/html/body/div[@class='mm-g-wrap clearfix']/div[@id='J_MmInfo']/div[@class='mm-p-middle mm-p-sheShow']/div[@class='mm-p-info mm-p-base-info']/ul[@class='mm-p-info-cell clearfix']/li[7]/span/text()"
    condition["height"] = "/html/body/div[@class='mm-g-wrap clearfix']/div[@id='J_MmInfo']/div[@class='mm-p-middle mm-p-sheShow']/div[@class='mm-p-info mm-p-base-info']/ul[@class='mm-p-info-cell clearfix']/li[@class='mm-p-small-cell mm-p-height']/p/text()"
    condition["weight"] = "/html/body/div[@class='mm-g-wrap clearfix']/div[@id='J_MmInfo']/div[@class='mm-p-middle mm-p-sheShow']/div[@class='mm-p-info mm-p-base-info']/ul[@class='mm-p-info-cell clearfix']/li[@class='mm-p-small-cell mm-p-weight']/p/text()"
    condition["bwh"] = "/html/body/div[@class='mm-g-wrap clearfix']/div[@id='J_MmInfo']/div[@class='mm-p-middle mm-p-sheShow']/div[@class='mm-p-info mm-p-base-info']/ul[@class='mm-p-info-cell clearfix']/li[@class='mm-p-small-cell mm-p-size']/p/text()"
    condition["breast"] = "/html/body/div[@class='mm-g-wrap clearfix']/div[@id='J_MmInfo']/div[@class='mm-p-middle mm-p-sheShow']/div[@class='mm-p-info mm-p-base-info']/ul[@class='mm-p-info-cell clearfix']/li[@class='mm-p-small-cell mm-p-bar']/p/text()"
    condition["feet"] = "/html/body/div[@class='mm-g-wrap clearfix']/div[@id='J_MmInfo']/div[@class='mm-p-middle mm-p-sheShow']/div[@class='mm-p-info mm-p-base-info']/ul[@class='mm-p-info-cell clearfix']/li[@class='mm-p-small-cell mm-p-shose']/p/text()"

    get_content = GetContent()
    res = get_content.read_one("myl", "person_html")
    get_content.get_all(res["html"], res["url"], **condition)










