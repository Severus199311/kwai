import requests
import json


class GetRawData():
	def __init__(self):
		self.sigs_server = 'http://localhost:6780/sigs'

	def get_sigs(self, url, data):
		payload = json.dumps({'url': url, 'data': data})
		headers = {"content-type": "application/json;charset=utf-8"}
		response = requests.post(self.sigs_server, data = payload, headers = headers, timeout = 5)
		result = response.json().get('result')
		return result

	def get_channel(self, cursor): #获取主播id，不需要sig三兄弟
		url = 'https://www.kwaishop.com/rest/app/grocery/ks/square/tab?tabId=534&cursor={}&feedSize={}&channel=LIVESQUARE'.format(str(cursor), str(cursor))
		headers = {
			'Host': 'www.kwaishop.com',
			'Connection': 'keep-alive',
			'Accept': 'application/json',
			'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; V1938T Build/LMY49I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 Kwai/7.4.20.13991 MerchantWeb/1.0',
			'Referer': 'https://www.kwaishop.com/square?source=searchhome&hyId=eshopSquare&layoutType=4&tabId=534&&channel=LIVESQUARE',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'zh-CN,en-US;q=0.8',
			'Cookie': 'mod=vivo%28V1938T%29; lon=116.41025; country_code=cn; kpn=KUAISHOU; oc=GENERIC; egid=DFP4D7522278DFA2D69F99CD926E72065C0B432AA5F9B6379BB42DAA4C03D194; sbh=50; hotfix_ver=; sh=1280; nbh=0; socName=Qualcomm+MSM8996; max_memory=192; isp=CMCC; kcv=192; browseType=1; kpf=ANDROID_PHONE; ddpi=320; net=WIFI; app=0; ud=1958956987; c=GENERIC; sw=720; ftt=; ll=CepYpfRM9UNAEcdLN4lBGl1A; language=zh-cn; darkMode=false; iuid=; lat=39.916411; did_gt=1591951097912; ver=7.4; sys=ANDROID_5.1.1; appver=7.4.20.13991; token=7718a64a3f144211806ee41d028af6ef-1958956987; client_key=3c2cd3f3; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAFdjOEpX5TjDC9lBPmpB1Sq7QjNu60hpTxAjAP0_Hyv_3zY4HypLdRFyFWq06f5e8nNwTnDKojGDUhVaKFNstTCH9OD1Gc0YPowDFKyMygRwDCNJFAbJYkGcTDzeuTG-7Y1tuL4lXl9_tKBW11Adcddf62AgKJokmpGOFzu2iWtStbQZzACauA6R37MHw8539Sap3YJCS_xbTbyG3wuANNCGhLgtQndTL9KcIMccEKwrUv06E4iID-i3oAoTayDiIPlLtwmNKkCIW5Mh7_OT-bkpL1HKghvKAUwAQ; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAZuBsnsR8OKu8jsm6GdhluuofXMzH_lZYLPjhbsDBlrrMC1Ub8AogyWbfWzMxVXdYEaKhJj53EGOeBa4iFhdbqIk8M8hs01WMN64VhWeWa1Xae81_KAcalM0yMfKR5UA6qqrjt6zi4GjJaFESiAmVCCYycvCSfBqznqwaZkVjP1MlZ42DdMlm5PB017GBcgdrJQs8pm8-o9Cz2PCa0tJ2ZsaEjzXXh-w5KSBpkEgON-CMTK0tiIgzuQaz-K60s6OFjjd9RPPMIPZnMRtxmnsm4tZwCmYbBEoBTAB; sid=3c22b76a-5cee-4897-98f7-e770e3d252fe; did=ANDROID_405dee970c2375f2'
		}
		response = requests.get(url, headers=headers)
		return response.text
		#return response.json()

	def get_live(self, live_stream_id):
		url = 'https://lives2.gifshow.com/rest/n/live/infoForLive?mod=vivo(V1938T)&lon=116.41025&country_code=cn&kpn=KUAISHOU&oc=GENERIC&egid=DFP4D7522278DFA2D69F99CD926E72065C0B432AA5F9B6379BB42DAA4C03D194&sbh=50&hotfix_ver=&sh=1280&appver=7.4.20.13991&nbh=0&socName=Qualcomm MSM8996&max_memory=192&isp=CMCC&kcv=192&browseType=1&kpf=ANDROID_PHONE&ddpi=320&did=ANDROID_405dee970c2375f2&net=WIFI&app=0&ud=1958956987&c=GENERIC&sys=ANDROID_5.1.1&sw=720&ftt=&ll=CepYpfRM9UNAEcdLN4lBGl1A&language=zh-cn&darkMode=false&iuid=&lat=39.916411&did_gt=1591951097912&ver=7.4'
		#url = 'https://api3.gifshow.com/rest/n/live/infoForLive?mod=vivo(V1938T)&lon=116.41025&country_code=cn&kpn=KUAISHOU&oc=GENERIC&egid=DFP4D7522278DFA2D69F99CD926E72065C0B432AA5F9B6379BB42DAA4C03D194&sbh=50&hotfix_ver=&sh=1280&appver=7.4.20.13991&nbh=0&socName=Qualcomm MSM8996&max_memory=192&isp=CMCC&kcv=192&browseType=1&kpf=ANDROID_PHONE&ddpi=320&did=ANDROID_405dee970c2375f2&net=WIFI&app=0&ud=1958956987&c=GENERIC&sys=ANDROID_5.1.1&sw=720&ftt=&ll=CepYpfRM9UNAEcdLN4lBGl1A&language=zh-cn&darkMode=false&iuid=&lat=39.916411&did_gt=1591951097912&ver=7.4'
		data = 'liveStreamId={}&kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAFdjOEpX5TjDC9lBPmpB1Sq7QjNu60hpTxAjAP0_Hyv_3zY4HypLdRFyFWq06f5e8nNwTnDKojGDUhVaKFNstTCH9OD1Gc0YPowDFKyMygRwDCNJFAbJYkGcTDzeuTG-7Y1tuL4lXl9_tKBW11Adcddf62AgKJokmpGOFzu2iWtStbQZzACauA6R37MHw8539Sap3YJCS_xbTbyG3wuANNCGhLgtQndTL9KcIMccEKwrUv06E4iID-i3oAoTayDiIPlLtwmNKkCIW5Mh7_OT-bkpL1HKghvKAUwAQ&token=7718a64a3f144211806ee41d028af6ef-1958956987&client_key=3c2cd3f3&os=android'.format(live_stream_id)
		headers = {
			'Host': 'api3.ksapisrv.com',
			'Connection': 'keep-alive',
			#'Content-Length': '687',
			'Cookie': 'region_ticket=RT_2EA4F40180491646AF23D7D261DBD8F85494DC8B88F0A5A426956D307834E;token=7718a64a3f144211806ee41d028af6ef-1958956987',
			#'X-REQUESTID': '159229838147067328',
			'User-Agent': 'kwai-android aegon/1.16.2-curl',
			'Accept-Language': 'zh-cn',
			'Content-Type': 'application/x-www-form-urlencoded',
			'Accept-Encoding': 'gzip, deflate, br'
		}
		sigs = self.get_sigs(url, data)
		data = data + '&sig=' + str(sigs.get('sig')) + '&__NStokensig=' + str(sigs.get('NStokensig')) + '&__NS_sig3=' + str(sigs.get('NS_sig3'))
		response = requests.post(url, headers=headers, data=data)
		return response.text
		#return response.json()

	def get_product_list(self, live_stream_id):
		url = 'https://lives2.gifshow.com/rest/n/live/shop/commodity/byGuest?mod=vivo(V1938T)&lon=116.41025&country_code=cn&kpn=KUAISHOU&oc=GENERIC&egid=DFPAE5DBAF0E2D53C1E1BC86E88B58E6A133CBCE3C0F5E0D46A34F3ECA140070&sbh=50&hotfix_ver=&sh=1280&appver=7.4.20.13991&nbh=0&socName=Qualcomm MSM8996&max_memory=192&isp=CMCC&kcv=193&browseType=1&kpf=ANDROID_PHONE&ddpi=320&did=ANDROID_405dee970c2375f2&net=WIFI&app=0&ud=1958956987&c=GENERIC&sys=ANDROID_5.1.1&sw=720&ftt=&ll=CepYpfRM9UNAEcdLN4lBGl1A&language=zh-cn&darkMode=false&iuid=&lat=39.916411&did_gt=1591951097912&ver=7.4'
		#url = 'https://api3.gifshow.com/rest/n/live/shop/commodity/byGuest?mod=vivo(V1938T)&lon=116.41025&country_code=cn&kpn=KUAISHOU&oc=GENERIC&egid=DFPAE5DBAF0E2D53C1E1BC86E88B58E6A133CBCE3C0F5E0D46A34F3ECA140070&sbh=50&hotfix_ver=&sh=1280&appver=7.4.20.13991&nbh=0&socName=Qualcomm MSM8996&max_memory=192&isp=CMCC&kcv=193&browseType=1&kpf=ANDROID_PHONE&ddpi=320&did=ANDROID_405dee970c2375f2&net=WIFI&app=0&ud=1958956987&c=GENERIC&sys=ANDROID_5.1.1&sw=720&ftt=&ll=CepYpfRM9UNAEcdLN4lBGl1A&language=zh-cn&darkMode=false&iuid=&lat=39.916411&did_gt=1591951097912&ver=7.4'
		data = 'liveStreamId={}&kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAE1DchetdlVOqPThPjRWIsljGdl1UKp5TJmviQHjRRvVN6_AEc76SxRJg_qYfpAK3puxxhZtmuhfNUroueRZDFjP-TBN0Snt44Sft-c57EOfUEmZ7aADiYUQuE2VQgEr8aGvTkfXPK8kKHFphPh-7jK3uj-bSGXZZ1Y_Nq8oAsHCQnjvQvZyA2eHotbCaK-X-_TVPtOiOcwvYEUzCrICJ0qGhLgtQndTL9KcIMccEKwrUv06E4iIACCpZbIinig24K12Zj1OQv3NcBxn-yHT7V9iZufykHDKAUwAQ&token=7718a64a3f144211806ee41d028af6ef-1958956987&client_key=3c2cd3f3&os=android'.format(live_stream_id)
		headers = {
			'Host': 'api3.ksapisrv.com',
			'Connection': 'keep-alive',
			#'Content-Length': '687',
			'Cookie': 'region_ticket=RT_2EA4F40180491646AF23D7D261DBD8F85494DC8B88F0A5A426956D307834E;token=7718a64a3f144211806ee41d028af6ef-1958956987',
			#'X-REQUESTID': '159229838147067328',
			'User-Agent': 'kwai-android aegon/1.16.2-curl',
			'Accept-Language': 'zh-cn',
			'Content-Type': 'application/x-www-form-urlencoded',
			'Accept-Encoding': 'gzip, deflate, br'
		}
		sigs = self.get_sigs(url, data)
		data = data + '&sig=' + str(sigs.get('sig')) + '&__NStokensig=' + str(sigs.get('NStokensig')) + '&__NS_sig3=' + str(sigs.get('NS_sig3'))
		response = requests.post(url, headers=headers, data=data)
		return response.text
		#return response.json()

	def get_shop(self, user_id): #也许能用来判断主播是否有在直播，不需要sig三兄弟
		url = 'https://app.kwaixiaodian.com/rest/app/grocery/product/self/midPage/list'
		headers = {
			'Host': 'app.kwaixiaodian.com',
			'Connection': 'keep-alive',
			#'Content-Length': '210',
			'Accept': 'application/json',
			'Origin': 'https://app.kwaixiaodian.com',
			#'Trace-Id': '1.66858969827253.64807265836.1593313012205.2',
			'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; V1938T Build/LMY49I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 Kwai/7.4.20.13991 MerchantWeb/1.0',
			'Content-Type': 'application/json;charset=UTF-8',
			#'Referer': 'https://app.kwaixiaodian.com/merchant/shop/list?id={}&webviewClose=false&biz=merchant&carrierType=3&from=profile&hyId=kwaishop'.format(user_id),
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'zh-CN,en-US;q=0.8',
			'Cookie': 'mod=vivo%28V1938T%29; lon=116.41025; country_code=cn; kpn=KUAISHOU; oc=GENERIC; egid=DFPAE5DBAF0E2D53C1E1BC86E88B58E6A133CBCE3C0F5E0D46A34F3ECA140070; sbh=50; hotfix_ver=; sh=1280; nbh=0; socName=Qualcomm+MSM8996; max_memory=192; isp=CMCC; kcv=193; browseType=1; kpf=ANDROID_PHONE; ddpi=320; net=WIFI; app=0; ud=1958956987; c=GENERIC; sw=720; ftt=; ll=CepYpfRM9UNAEcdLN4lBGl1A; language=zh-cn; darkMode=false; iuid=; lat=39.916411; did_gt=1591951097912; ver=7.4; sys=ANDROID_5.1.1; appver=7.4.20.13991; token=7718a64a3f144211806ee41d028af6ef-1958956987; client_key=3c2cd3f3; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAE1DchetdlVOqPThPjRWIsljGdl1UKp5TJmviQHjRRvVN6_AEc76SxRJg_qYfpAK3puxxhZtmuhfNUroueRZDFjP-TBN0Snt44Sft-c57EOfUEmZ7aADiYUQuE2VQgEr8aGvTkfXPK8kKHFphPh-7jK3uj-bSGXZZ1Y_Nq8oAsHCQnjvQvZyA2eHotbCaK-X-_TVPtOiOcwvYEUzCrICJ0qGhLgtQndTL9KcIMccEKwrUv06E4iIACCpZbIinig24K12Zj1OQv3NcBxn-yHT7V9iZufykHDKAUwAQ; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAepGVOvduOU_qloJ3QQZxLyERUnh1rLj3Cy-dh9-viKplB5HrdaOnZIif3vvBgxx_At9SJOSSucTsoz1YLRcCz7z2mO4S9Z-Mx4o1X2rzC25ltNfDHnV22zmqo7OHouHJYwJhihxgSi07IyL_rjl4anFDRNAXbc6XAecdGQ3yeOxOgHcGRU_VDJZ2bYj8IRnM3AjFJv7o2nzMquofiANok4aErEJA26FToVlAmaCbr6l_rMcGiIgAx9RneRzxeC5LafmY9iQrzUsgg4R7s8HYMqXMKpOSssoBTAB; sid=a4ee172c-a6b7-4e46-9124-f62b16236263; did=ANDROID_405dee970c2375f2',
			#'X-Requested-With': 'com.smile.gifmaker'
		}
		data = "{\"listProductParam\":{\"id\":\""+ user_id +"\",\"webviewClose\":\"false\",\"biz\":\"merchant\",\"carrierType\":\"3\",\"from\":\"profile\",\"hyId\":\"kwaishop\",\"visitorId\":\"1958956987\",\"clientVersion\":\"7.4.20.13991\",\"clientId\":2,\"page\":1}}"
		response = requests.post(url, headers=headers, data=data)
		return response.text

	def get_product_a(self, product_id): #有赞的商品
		url = 'https://kuaishou.youzan.com/wscgoods/detail/' + product_id
		response = requests.get(url)
		return response.text

	def get_product_b(self, product_id):
		url = 'https://app.kwaixiaodian.com/rest/app/grocery/product/self/detail?itemId=' + product_id
		headers = {
			'Accept': 'application/json',
			'Accept-Encoding': 'gzip, deflate, br',
			'Accept-Language': 'zh-CN,zh;q=0.9',
			'Connection': 'keep-alive',
			'Cookie': '_did=web_539045057211C3F4; did=web_eb31ccde5a8df2677b52f6387dfe9822; didv=1592535539100',
			'Host': 'app.kwaixiaodian.com',
			'Referer': 'https://app.kwaixiaodian.com/merchant/shop/detail?id=9158272992',
			'Sec-Fetch-Mode': 'cors',
			'Sec-Fetch-Site': 'same-origin',
			#'Trace-Id': '1.66858969827253.900889139819.1593323352078.2',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
		}
		response = requests.get(url, headers=headers)
		return response.text

if __name__ == '__main__':
	get_raw_data = GetRawData()
	live_stream_id = 'cJaLmR2TN7M'
	live_stream_id = 'hUiuIVWgwWs'
	live_stream_id = 'ymXT05NHL_k'
	user_id = '749335878'
	product_id = '2g1je2kdvt0mn'
	product_id = '9158272992'
	cursor = 100
	result = get_raw_data.get_channel(cursor)
	#result = get_raw_data.get_shop(user_id)
	#result = get_raw_data.get_live(live_stream_id)
	#result = get_raw_data.get_product_list(live_stream_id)
	#result = get_raw_data.get_product_a(product_id)
	#result = get_raw_data.get_product_b(product_id)
	print(result)



#3xv66iyfnnif8zc XZ11228888 1252032199 小资教穿搭