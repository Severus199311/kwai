# -*- coding: utf-8 -*-

import json
from get_raw_data import GetRawData

class GetChannel():
	def __init__(self):
		self.get_raw_data = GetRawData()
		self.valid_user_list = []
		self.stupid_words = ['公司', '店', '铺', '厂', '工', '产', '行', '瑙', '号', '绒', '纺', '鞋', '装', '价', '市', '县', '区', '服', '饰', '商', '贸', '牌', '汇', '潮', '馆', '裤', '业', '专', '卖', '时尚', '品', '妆', '玩具', '语文', '数学', '语', '科学', '物理', '化学', '生物', '政治', '历史', '地理', '官方', '殖','宠物', '户外', '少儿', '教', '课', '坊', '海鲜', '车', '学', '旅游', '剪', '制', '电影', '机', '口才', '拍', '书', '字', '榜', '音乐', '手工', '思维', '咨', '球', '琴', '州', '针织', '说', '水果', '园', '讲', '考', '动画', '情感', '星座', '销售', '心理', '段子', '镯', '瑜伽', '老师', '舞', '游戏', '鲜花', '萌宠', '大码', '珠宝', '翡翠', '吉他', '乐器', '零食', '绘画', '科技', '武术', '中医']

	def get_channel(self, cursor):
		try:
			channel_raw_data = self.get_raw_data.get_channel(cursor)
		except Exception as e:
			print('get_channel,' + e.args[0])
			channel_raw_data = None

		if channel_raw_data:
			self.parse_channel(json.loads(channel_raw_data))

	def is_qualified(self, live):
		for word in self.stupid_words:
			if word in live.get('nick'):
				return False
		if int(live.get('onlineNum')) < 5000:
			return False
		superman = live.get('relationProductInfo')
		if superman:
			if superman.get('productCount') < 15:
				return False
		else:
			return False
		return True

	def parse_channel(self, channel_raw_data):
		try:
			live_list = channel_raw_data.get('data').get('works').get('works')
			for live in live_list:
				if self.is_qualified(live):
					self.valid_user_list.append(live.get('nick'))
		except Exception as e:
			print('parse_channel,' + e.args[0])

if __name__ == '__main__':
	get_channel = GetChannel()
	get_channel.get_channel(10)
	print(get_channel.valid_user_list)



