import requests
from urllib import request, parse

url = 'https://t-openscenic.ybsjyyn.com/openscenic/appoint/appointMange/api/getAppointList'

headers = {
    # 'openid': 't-30fb3696795b3b7cd053d50eca2b3ead',
    # 'uid': '8b274ae64b8c60bcab1605bf243885b3',
    # 'wskey': 'AHmSpC4MSqVchATRCMenlJU74PwPNiJRVB8md8tkI7R4pvHySB6k98wqfc\
    #          jJ0hAg3qtjspuKe-iIJz4DTtILOA_iH9r0XOCRvEgD0YE0zfMGwr8GBWgYyF\
    #          wEg2PPXUGA4F1GShF6W_ho3iuaYp-P5Z0jirQwkG36hP8M2-GD2Rc.@Gh3f\
    #         3Wn_UTyY-fOdnmLVrYqekbsAdPYLW8Srw6ZWr0asIASYwZLLZZDI8YTzmx3ywwX\
    #         fuwDLT9a16MIV555CAWu-sxA099d2btyMLSztY2n3cyHuQyxB2VY4lYJ_srGWh8X\
    #         oyd12mORJOGWlWMrGkswD-lD0ZHN4lyXCyI9iww8.',
    'channelType': 1,
    'idCodeStatus': 1,
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'jwt=AHmSpC4MSqVchATRCMenlJU74PwPNiJRVB8md8tkI7R4pvHySB6k98wqfcjJ0hAg3qtjspuKe-iIJz4DTtILOA_iH9r0XOCRvEgD0YE0zfMGwr8GBWgYyFwEg2PPXUGA4F1GShF6W_ho3iuaYp-P5Z0jirQwkG36hP8M2-GD2Rc.@Gh3f3Wn_UTyY-fOdnmLVrYqekbsAdPYLW8Srw6ZWr0asIASYwZLLZZDI8YTzmx3ywwXfuwDLT9a16MIV555CAWu-sxA099d2btyMLSztY2n3cyHuQyxB2VY4lYJ_srGWh8Xoyd12mORJOGWlWMrGkswD-lD0ZHN4lyXCyI9iww8.; w_skey=AHmSpC4MSqVchATRCMenlJU74PwPNiJRVB8md8tkI7R4pvHySB6k98wqfcjJ0hAg3qtjspuKe-iIJz4DTtILOA_iH9r0XOCRvEgD0YE0zfMGwr8GBWgYyFwEg2PPXUGA4F1GShF6W_ho3iuaYp-P5Z0jirQwkG36hP8M2-GD2Rc.@Gh3f3Wn_UTyY-fOdnmLVrYqekbsAdPYLW8Srw6ZWr0asIASYwZLLZZDI8YTzmx3ywwXfuwDLT9a16MIV555CAWu-sxA099d2btyMLSztY2n3cyHuQyxB2VY4lYJ_srGWh8Xoyd12mORJOGWlWMrGkswD-lD0ZHN4lyXCyI9iww8.; w_uid=8b274ae64b8c60bcab1605bf243885b3; w_open_id=t-30fb3696795b3b7cd053d50eca2b3ead; w_expires_in=604800',
    'openid': 't-30fb3696795b3b7cd053d50eca2b3ead',
    'referer': 'https://t-openscenic.ybsjyyn.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'uid': '8b274ae64b8c60bcab1605bf243885b3',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'wskey': 'AHmSpC4MSqVchATRCMenlJU74PwPNiJRVB8md8tkI7R4pvHySB6k98wqfcjJ0hAg3qtjspuKe-iIJz4DTtILOA_iH9r0XOCRvEgD0YE0zfMGwr8GBWgYyFwEg2PPXUGA4F1GShF6W_ho3iuaYp-P5Z0jirQwkG36hP8M2-GD2Rc.@Gh3f3Wn_UTyY-fOdnmLVrYqekbsAdPYLW8Srw6ZWr0asIASYwZLLZZDI8YTzmx3ywwXfuwDLT9a16MIV555CAWu-sxA099d2btyMLSztY2n3cyHuQyxB2VY4lYJ_srGWh8Xoyd12mORJOGWlWMrGkswD-lD0ZHN4lyXCyI9iww8.',
    'x-request-type-ajax': 1
}

body = {
    'appointDate': "2020-07-27 11:38:15",
    'appointId': "ff8080817384704e01738e2bb12b003f",
    'appointNo': "2020072711381422982917676843558",
    'appointNum': 1,
    'appointStatus': 1,
    'appointStatusName': "预约成功",
    'auditStatus': 'null',
    'auditStatusName': 'null',
    'automaticCheckTime': 15,
    'checkTime': 'null',
    'codeSendName': "测试俊pycharm",
    'codeSendTelNum': "18000298946",
    'comeScenicStatus':15,
    'comeScenicStatusName': "待入园",
    'inParkDate': "2020-07-27 12:00-14:00",
    'inParkNum': 'null',
    'inParkStatus': 15,
    'isEpidemicFlag': 1,
    'lineName': "测试俊线路修改版",
    'rejectReason': 'null',
    'scenicId': "18B44CBB-FEA6-4C39-AE53-F1A7345E67FB",
    'scenicName': "丽江玉龙雪山景区",
    'subsidyNum': "1",
    'travelAgentName': "昆明腾云旅行社",
    'travelItineraryNo': "YNTI202007240007",
    'travelItineraryUrl': "https://t-tio.ybsjyyn.com/lxsdygl/web/index.html#/QRCode?id=YNTI202007270001"

}

#忽略安全警告
requests.packages.urllib3.disable_warnings()

data = bytes(parse.urlencode(body), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='GET')
response = request.urlopen(req)
print(response.read().decode('utf-8'))