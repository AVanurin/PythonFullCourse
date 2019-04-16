class PassCard:
	def isValid(self):
		# У кого больше дата у срока окончания работы карты или у сегодня?
		if self.expiration_date > datetime.datetime.now():
			# В таком случае карта еще рабочая
			return True
		else:
			# В таком случае срок работы карты истек
			return False

# Создаем экземпляр card_1 класса PassCaed
card_1 = PassCard()

# Определяем все свойства экземпляра card_1
card_1.name = "Виктория Соловьева"
card_1.level = 1
card_1.expiration_date = datetime.datetime(2019, 10, 30)

# Аналогично для второй карты
card_2 = PassCard()
card_2.name = "Олег Ситников"
card_2.level = 2
card_2.expiration_date = datetime.datetime(2019, 1, 1)

# Проверим работает ли первая карта
if card_1.isValid():
	print("Пока работает")
else:
	print("Срок действия истек")

# Проверяем работает ли вторая карта
if card_2.isValid():
	print("Пока работает")
else:
	print("Срок действия истек")