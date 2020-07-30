# 行程单的各项参数
import time,uuid,random,opencc
from first_name import first_name
#出游日期
app_date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

#获取随机行程单id
last_id = str(random.randint(41910173245681820000,41910173245691820000))
app_id = 'ff8080817324' + last_id

#   行程单号
team_date = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
team_id = 'YNTI' +team_date[:12]

#   入园日期
data_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))

#配置五个景区id对应的景区名称
scenid_name = {'0D047734-D762-48B7-BAC4-5C94E4D574A9': '大理剑川石宝山',
                '9F122E5C-1B18-48A8-AB61-7AAAF3D611A5': '大理巍山古城',
                'BD564076-B23C-4676-B48C-24E687E73A30': '大理宾川鸡足山景区',
                '020572B5-318B-4693-957E-C5A6040366D1': '大理银都水乡新华村景区',
                '18B44CBB-FEA6-4C39-AE53-F1A7345E67FB': '丽江玉龙雪山景区'}
#定义五个景区id
scen_id = ['0D047734-D762-48B7-BAC4-5C94E4D574A9', '9F122E5C-1B18-48A8-AB61-7AAAF3D611A5',
            'BD564076-B23C-4676-B48C-24E687E73A30', '020572B5-318B-4693-957E-C5A6040366D1',
            '18B44CBB-FEA6-4C39-AE53-F1A7345E67FB']
#获取景区随机id
ran_id = random.choice(scen_id)
#获取景区随机id对应景区名称
ran_name = scenid_name[ran_id]

# 随机生成姓名
def get_name():
    name_code = ''
    # 在百家姓列表里面随便选择一个姓
    name_code+=random.choice(first_name)
    ran_num = random.randint(0,1)
    # 为0生成的名字是两个字,为1生成的名字是一个字
    if ran_num ==0:
        for i in range(2):
            # 从十进制汉字编码随机选取一个
            ran = random.randint(19968,40869)
            # 将其转换为汉字
            ran = chr(ran)
            name_code+=ran
    else:
        # 从十进制汉字编码随机选取一个
        ran = random.randint(19968, 40869)
        # 将其转换为汉字
        ran = chr(ran)
        name_code += ran
    # 编码
    name_code.encode('utf-8')
    return name_code
cc_name = opencc.OpenCC('t2s').convert(get_name())





app_time = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
app_no = app_time + str(random.randint(100000,999999))
#获取随机的id
status = ['预约成功','已完成','已失效','已取消']

#	出游日期
goTravelDate= app_date
#   线路名称
lineName= 'csj测试用线路'
#   计调人员电话
codeSendTelNum = '18000298946'
#   行程单ID
electronicOrderId= app_id
#   旅行社名字和id
travelAgentName= None
travelAgentId= None
#   计调人员名字
codeSendPerson= '测试测试'
#   行程单号
teamId= team_id
#   景区信息

scenics =  [{
"date": data_time,
"scenicName": ran_name,
"scenicId": ran_id,
"tourist" : [{
"touristType": "child",
"touristIdType": 1,
"touristIdNumber": "110101201803079612",
"touristName": cc_name,
"touristAge": "",
"touristCity": "xxxx",
"touristCityCode": "xxxx",
"touristId":"xxxxx"}]}]
