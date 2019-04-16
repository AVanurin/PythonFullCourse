class PassCard:
	def isValid(self):
		# У кого больше дата у срока окончания работы карты или у сегодня?
		if self.expiration_date > datetime.datetime.now():
			# В таком случае карта еще рабочая
			return True
		else:
			# В таком случае срок работы карты истек
			return False

card_1 = PassCard()
card_1.name = "Виктория Соловьева"
card_1.level = 1
card_1.expiration_date = datetime.datetime(2019, 10, 30)

card_2 = PassCard()
card_2.name = "Олег Ситников"
card_2.level = 2
card_2.expiration_date = datetime.datetime(2019, 1, 1)