import os,sys,unittest,time
from lib.test_abstract import TestAbstract
from lib.wxls import *

#url = 'http://gis-rss.intsit.sfdc.com.cn:1080/geo'
url=geturl("geo")
ak=getak("ak")
name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]

class rh(TestAbstract):
    def test_1(self):
        data = {'address': '广东省深圳市南山区南园村新二坊18栋', \
                'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])
        print('1: ', res)

    def test_2(self):
        data = {'address': '武汉市武昌区白沙洲街办事处武金堤路中大长江紫都4期2栋2303', \
                'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])
        print('2: ', res)

    def test_3(self):
        data = {'address': '北京市朝阳区孙河乡东苇路301号西院4层', \
                'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])
        print('3: ', res)

    def test_4(self):
        data = {'address': '上海市长宁区法华鎮路635弄9号201室 ', \
                'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])
        print('4: ', res)

    def test_5(self):
        data = {'address': '广州市天河区兴安路15号天空别墅516室', \
                'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])
        print('2: ', res)

    def test_12(self):
        data = {'address': '重庆市江津区鼎山街道祥瑞时尚天街89号', \
                'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])
        print('12: ', res)

    def test_6(self):
        data = {'address': '天津天津市河北区七马路仁恒河滨花园7—2001孙怡', \
                 'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])
        print('6: ', res)

    def test_7(self):
        data = {'address': '东莞市清溪镇三中金龙工业区莲塘路67号', \
                'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])
        print('7: ', res)

    def test_8(self):
        data = {'address': '杭州市富阳市富阳区富春街道文教鹿苑90号', \
                'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])
        print('8: ', res)

    def test_9(self):
        data = {'address': '郑州市惠济区天河路36号郑州财经学院', \
                'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        self.append = p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])
        print('9: ', res)

    def test_10(self):
        data = {'address': '长沙市长沙县星沙大道阳光丽景小区4-1501', \
                'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])
        print('10: ', res)

    def test_11(self):
        data = {'address': '南京市鼓楼区下关金碧花园4栋101', \
                'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])
        print('11: ', res)

    def test_13(self):
        data = {'address': '苏州市吴江区黎里镇黎民北路895号', \
                'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])
        print('13: ', res)

    def test_14(self):
        data = {'address': '西安市未央区三桥街道武警路武警工程大学', \
                'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])
        print('14: ', res)

    def test_15(self):
        data = {'address': '兰州市城关区渭源路街道天水南路222号兰州大学10号楼', \
                'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])
        print('15: ', res)

    def test_16(self):
        data = {'address': '南昌市东湖区建德观街140号', \
                'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])
        print('16: ', res)

    def test_17(self):
        data = {'address': '石家庄市红旗大街98号银河证券', \
                'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])
        print('17: ', res)

    def test_18(self):
        data = {'address': '保定市涿州市东城坊镇中国劳动关系学院', \
                'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])
        print('18: ', res)

    def test_19(self):
        data = {'address': '绍兴市越城区绍兴天下花园观澜苑7幢', \
                'opt': '', \
                'city': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])


    def test_20(self):
        data = {'address': '温州市瓯海区茶山街道霞岙', \
                'opt': '', \
                'city': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])


    def test_21(self):
        data = {'address': '金华市义乌市义乌市雪枫西路296号义乌信宝行汽车销售服务有限公司', \
                'opt': '', \
                'city': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])

    def test_22(self):
        data = {'address': '衢州市柯城区荷三路147号', \
                'opt': '', \
                'city': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])
        
    def test_23(self):
        data = {'address': '丽水市松阳县古市镇横街109号', \
                'opt': '', \
                'city': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])
        
    def test_24(self):
        data = {'address': '嘉兴市桐乡市石门镇羔羊工业区羔羊路501号', \
                'opt': '', \
                'city': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])
        
    def test_25(self):
        data = {'address': '湖州市长兴县李家巷镇天马服装皮件有限公司', \
                'opt': '', \
                'city': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])
        
    def test_26(self):
        data = {'address': '宁波市北仑区小浃江中路518号宁波海天驱动有限公司', \
                'opt': '', \
                'city': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])

    def test_27(self):
        data = {'address': '舟山市普陀区六横镇浦西村天福堂路3号', \
                'opt': '', \
                'city': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])

    def test_28(self):
        data = {'address': '台州市温岭市城东街道楼山村二区31幢', \
                'opt': '', \
                'city': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])

    def test_29(self):
        data = {'address': '惠州市惠城区龙丰街道办刘屋山60栋', \
                'opt': '', \
                'city': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])

    def test_30(self):
        data = {'address': '梅州市梅县区扶大镇剑英大道外国语学校', \
                'opt': '', \
                'city': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])

    def test_31(self):
        data = {'address': '河源市源城区广东鸿盛消防检测河源分公司源城区新风路351号', \
                'opt': '', \
                'city': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])

    def test_32(self):
        data = {'address': '黑龙江省哈尔滨市巴彦县步行街', \
                'opt': '', \
                'city': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])
        
    def test_33(self):
        data = {'address': '泉州市洛江区双阳南山新世界超市', \
                'opt': '', \
                'city': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])

    def test_34(self):
        data = {'address': '南昌市红谷滩新区江西日报社', \
                'opt': '', \
                'city': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])
        
    def test_35(self):
        data = {'address': '贵州省贵阳市观山湖区观山湖区', \
                'opt': '', \
                'city': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])
        
    def test_36(self):
        data = {'address': '内蒙古自治区包头市昆都仑区阿尔丁大街街道', \
                'opt': '', \
                'city': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])
        
    def test_37(self):
        data = {'address': '宁夏回族自治区银川市西夏区金波街与宝湖交叉口农民失地创业园', \
                'opt': '', \
                'city': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])

    def test_38(self):
        data = {'address': '吉林省长春市德惠市郭家镇戈家村田洼屯5社', \
                'opt': '', \
                'city': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])


    def test_39(self):
        data = {'address': '安徽省宣城市皖南第一街c2---307', \
                'opt': '', \
                'city': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])

    def test_40(self):
        data = {'address': '南昌市南昌县小蓝工业园金沙三路1155号', \
                'opt': '', \
                'city': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        self.assertIn('rh', res['result']['src'])

    @classmethod
    def tearDownClass(clz):
        reporttxt(name, url, p, r)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(rh))
    runner = unittest.TextTestRunner()
    runner.run(suite)



# 广东省深圳市南山区南园村新二坊18栋
# 广东省深圳市南山区南园村新二坊4号一楼鞋店
# 山东省潍坊市奎文区东风东街世纪泰华泰华中心22楼2205
# 广东省深圳市南山区南园村新四坊6号203
# 山东省东营区胜利建安公司对面友锋汽修
# 山西省太原市小店区南坪头村3号三毛物流大院
# 三亚市榆亚路红郊社区1组内园中巷116号
# 山西省太原市小店区国信嘉园15-604
# 山东省东营区西四路66号粮食局1楼
# 广东省潮州市潮安区庵埠镇振兴路37号