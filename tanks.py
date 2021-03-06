"""
Класс позволяет мониторить данные с console.worldoftanks.com (PS4 и Xbox) за сутки/неделю/месяц. Данные хранятся в формате.
Параметры, за которыми следит скрипт: количество боев (побед/поражений), кол-во убитых врагов, 
кол-во паданий и пробитий, кол-во обнаруженных врагов, суммарный нанесенный урон и полученный опыт.

The class allows you to monitor data from console.worldoftanks.com (PS4 and Xbox) a day / week / month. The data is stored in.
The parameters monitored by the script: the number of battles (victories / defeats), 
the number of enemies killed, the number of falls and penetrations, the number of detected enemies, 
the total damage done and the experience gained.

"""
import requests
import json
import time
import os

class Tanks(object):
	def __init__(self, name):
		API = ''
		resp = requests.get('https://api-console.worldoftanks.com/wotx/account/list/?application_id=' + API + '&search=' + name)
		wot = resp.json()
		if wot['meta']['count'] == 0:
			self.error = True
		else:
			self.error = False
			self.id = str(wot['data'][0]['account_id'])
			self.name = wot['data'][0]['nickname']
			resp = requests.get('https://api-console.worldoftanks.com/wotx/account/info/?application_id=' + API + '&account_id=' + str(self.id))
			self.data = resp.json()
			if os.path.exists('./dataUser/' + self.id + '_data.json') == False:
				self.updateFirst()
			self.updateDay()
			self.updateWeek()
			self.updateMonths()

	def delStat(self):
		if os.path.exists('./dataUser/' + self.id + '_data.json') == True:
			os.remove('./dataUser/' + self.id + '_data.json')
	
	def getList(self):
		files = os.listdir('./dataUser/')
		for x in range(0,len(files)):
			listName = files[x] 
			files[x] = listName[:9]
		self.list = files

	def status(self):
		return self.error

	def info(self):
		mess = self.name + ' - ' + self.id
		return mess

	def sDay(self, data):
		with open('./dataUser/' + self.id + '_data.json', 'r') as f:
			loadData = json.load(f)
		if data == 'xp':
			return loadData['xp_d']
		elif data == 'hits':
			return loadData['hits_d']
		elif data == 'piercing':
			return loadData['piercings_d']
		elif data == 'spotted':
			return loadData['spotted_d']
		elif data == 'damage':
			return loadData['damage_dealt_d']
		elif data == 'battles':
			return loadData['battles_d']
		elif data == 'frags':
			return loadData['frags_d']
		elif data == 'wins':
			return loadData['wins_d']
		elif data == 'losses':
			return loadData['losses_d']
		elif data == 'date':
			return loadData['update_day']
		else:
			return 0

	def sWeek(self, data):
		with open('./dataUser/' + self.id + '_data.json', 'r') as f:
			loadData = json.load(f)
		if data == 'xp':
			return loadData['xp_w']
		elif data == 'hits':
			return loadData['hits_w']
		elif data == 'piercing':
			return loadData['piercings_w']
		elif data == 'spotted':
			return loadData['spotted_w']
		elif data == 'damage':
			return loadData['damage_dealt_w']
		elif data == 'battles':
			return loadData['battles_w']
		elif data == 'frags':
			return loadData['frags_w']
		elif data == 'wins':
			return loadData['wins_w']
		elif data == 'losses':
			return loadData['losses_w']
		elif data == 'date':
			return loadData['update_week']
		else:
			return 0

	def sMonth(self, data):
		with open('./dataUser/' + self.id + '_data.json', 'r') as f:
			loadData = json.load(f)
		if data == 'xp':
			return loadData['xp_m']
		elif data == 'hits':
			return loadData['hits_m']
		elif data == 'piercing':
			return loadData['piercings_m']
		elif data == 'spotted':
			return loadData['spotted_m']
		elif data == 'damage':
			return loadData['damage_dealt_m']
		elif data == 'battles':
			return loadData['battles_m']
		elif data == 'frags':
			return loadData['frags_m']
		elif data == 'wins':
			return loadData['wins_m']
		elif data == 'losses':
			return loadData['losses_m']
		elif data == 'date':
			return loadData['update_mounth']
		else:
			return 0

	def updateFirst(self):
		loadData = {}
		# day
		loadData['battles_d'] = self.data['data'][self.id]['statistics']['all']['battles']
		loadData['frags_d'] = self.data['data'][self.id]['statistics']['all']['frags']
		loadData['wins_d'] = self.data['data'][self.id]['statistics']['all']['wins']
		loadData['losses_d'] = self.data['data'][self.id]['statistics']['all']['losses']

		loadData['xp_d'] = self.data['data'][self.id]['statistics']['all']['xp']
		loadData['hits_d'] = self.data['data'][self.id]['statistics']['all']['hits']
		loadData['piercings_d'] = self.data['data'][self.id]['statistics']['piercings']
		loadData['spotted_d'] = self.data['data'][self.id]['statistics']['all']['spotted']
		loadData['damage_dealt_d'] = self.data['data'][self.id]['statistics']['all']['damage_dealt']
        # week
		loadData['battles_w'] = self.data['data'][self.id]['statistics']['all']['battles']
		loadData['frags_w'] = self.data['data'][self.id]['statistics']['all']['frags']
		loadData['wins_w'] = self.data['data'][self.id]['statistics']['all']['wins']
		loadData['losses_w'] = self.data['data'][self.id]['statistics']['all']['losses']

		loadData['xp_w'] = self.data['data'][self.id]['statistics']['all']['xp']
		loadData['hits_w'] = self.data['data'][self.id]['statistics']['all']['hits']
		loadData['piercings_w'] = self.data['data'][self.id]['statistics']['piercings']
		loadData['spotted_w'] = self.data['data'][self.id]['statistics']['all']['spotted']
		loadData['damage_dealt_w'] = self.data['data'][self.id]['statistics']['all']['damage_dealt']
		# months
		loadData['battles_m'] = self.data['data'][self.id]['statistics']['all']['battles']
		loadData['frags_m'] = self.data['data'][self.id]['statistics']['all']['frags']
		loadData['wins_m'] = self.data['data'][self.id]['statistics']['all']['wins']
		loadData['losses_m'] = self.data['data'][self.id]['statistics']['all']['losses']

		loadData['xp_m'] = self.data['data'][self.id]['statistics']['all']['xp']
		loadData['hits_m'] = self.data['data'][self.id]['statistics']['all']['hits']
		loadData['piercings_m'] = self.data['data'][self.id]['statistics']['piercings']
		loadData['spotted_m'] = self.data['data'][self.id]['statistics']['all']['spotted']
		loadData['damage_dealt_m'] = self.data['data'][self.id]['statistics']['all']['damage_dealt']
		# Date
		loadData['update_day'] = time.time()
		loadData['update_week'] = time.time()
		loadData['update_months'] = time.time()

		with open('./dataUser/' + self.id +'_data.json', 'w') as f:
			json.dump(loadData, f)

	def updateDay(self):
		with open('./dataUser/' + self.id + '_data.json', 'r') as f:
			loadData = json.load(f)
		day = round((time.time() - loadData['update_day']) / (60*60))
		if day > 24:
			loadData['battles_d'] = self.data['data'][self.id]['statistics']['all']['battles'] - loadData['battles_d']
			loadData['frags_d'] = self.data['data'][self.id]['statistics']['all']['frags'] - loadData['frags_d']
			loadData['wins_d'] = self.data['data'][self.id]['statistics']['all']['wins'] - loadData['wins_d']
			loadData['losses_d'] = self.data['data'][self.id]['statistics']['all']['losses'] - loadData['losses_d']

			loadData['xp_d'] = self.data['data'][self.id]['statistics']['all']['xp'] - loadData['xp_d']
			loadData['hits_d'] = self.data['data'][self.id]['statistics']['all']['hits'] - loadData['hits_d']
			loadData['piercings_d'] = self.data['data'][self.id]['statistics']['piercings'] - loadData['piercings_d']
			loadData['spotted_d'] = self.data['data'][self.id]['statistics']['all']['spotted'] - loadData['spotted_d']
			loadData['damage_dealt_d'] = self.data['data'][self.id]['statistics']['all']['damage_dealt'] - loadData['damage_dealt_d']
			loadData['update_day'] = time.time()
			with open('./dataUser/' + self.id + '_data.json', 'w') as f:
				json.dump(loadData, f)
		else:
			pass

	def updateWeek(self):
		with open('./dataUser/' + self.id + '_data.json', 'r') as f:
			loadData = json.load(f)
		week = round((time.time() - loadData['update_week']) / (60*60*24))
		if week > 7:
			loadData['battles_w'] = self.data['data'][self.id]['statistics']['all']['battles'] - loadData['battles_w']
			loadData['frags_w'] = self.data['data'][self.id]['statistics']['all']['frags'] - loadData['frags_w']
			loadData['wins_w'] = self.data['data'][self.id]['statistics']['all']['wins'] - loadData['wins_w']
			loadData['losses_w'] = self.data['data'][self.id]['statistics']['all']['losses'] - loadData['losses_w']

			loadData['xp_w'] = self.data['data'][self.id]['statistics']['all']['xp'] - loadData['xp_w']
			loadData['hits_w'] = self.data['data'][self.id]['statistics']['all']['hits'] - loadData['hits_w']
			loadData['piercings_w'] = self.data['data'][self.id]['statistics']['piercings'] - loadData['piercings_w']
			loadData['spotted_w'] = self.data['data'][self.id]['statistics']['all']['spotted'] - loadData['spotted_w']
			loadData['damage_dealt_w'] = self.data['data'][self.id]['statistics']['all']['damage_dealt'] - loadData['damage_dealt_w']
			loadData['update_week'] = time.time()
			with open('./dataUser/' + self.id + '_data.json', 'w') as f:
				json.dump(loadData, f)
		else:
			pass

	def updateMonths(self):
		with open('./dataUser/' + self.id + '_data.json', 'r') as f:
			loadData = json.load(f)
		week = round((time.time() - loadData['update_months']) / (60*60*24))
		if week > 7:
			loadData['battles_m'] = self.data['data'][self.id]['statistics']['all']['battles'] - loadData['battles_m']
			loadData['frags_m'] = self.data['data'][self.id]['statistics']['all']['frags'] - loadData['frags_m']
			loadData['wins_m'] = self.data['data'][self.id]['statistics']['all']['wins'] - loadData['wins_m']
			loadData['losses_m'] = self.data['data'][self.id]['statistics']['all']['losses'] - loadData['losses_m']

			loadData['xp_m'] = self.data['data'][self.id]['statistics']['all']['xp'] - loadData['xp_m']
			loadData['hits_m'] = self.data['data'][self.id]['statistics']['all']['hits'] - loadData['hits_m']
			loadData['piercings_m'] = self.data['data'][self.id]['statistics']['piercings'] - loadData['piercings_m']
			loadData['spotted_m'] = self.data['data'][self.id]['statistics']['all']['spotted'] - loadData['spotted_m']
			loadData['damage_dealt_m'] = self.data['data'][self.id]['statistics']['all']['damage_dealt'] - loadData['damage_dealt_m']
			loadData['update_months'] = time.time()
			with open('./dataUser/' + self.id + '_data.json', 'w') as f:
				json.dump(loadData, f)
		else:
			pass