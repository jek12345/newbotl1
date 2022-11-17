import telebot

bot = telebot.TeleBot('5677308857:AAEy4eSfFVkEHzFfnw6ysLhRbscr8ctu7sY')
val = id(object)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Заявка буде оброблена тільки в разі підтвердження Вашого номера телефону.\n\n'
                                      'Заявка будет обработана только в случае подтверждения Вашего номера телефона.', parse_mode='html')

@bot.message_handler(content_types=['text'])
def get_user_text(message):

    sent = bot.send_message(message.chat.id,'Введіть Ваш номер телефону.\n\nВведите ваш номер телефона.')
    bot.register_next_step_handler(sent, user_answer)


def user_answer(message):
    global answers
    answers = []
    number = message.text
    answers.append(number)

    sent1 = bot.send_message(message.chat.id, 'Вкажіть ПІБ полоненого, в форматі\n\n'
                                              'Прізвище Ім я По Батькові.\n\n'
                                              'Приклад:\n\n'
                                              '<b> Іванов Іван Іванович</b>\n\n'
                                              'Укажите  ФИО пленного, в формате\n\n'
                                              'Фамилия Имя Отчество.\n\n'
                                              'Пример:\n\n'
                                              '<b>Иванов Иван Иванович</b>\n\n',parse_mode='html')

    bot.register_next_step_handler(sent1, user_answer1)
def user_answer1(message):
    fioshykai = message.text
    answers.append(fioshykai)
    sent2 = bot.send_message(message.chat.id,'Введіть дату народження полоненого у форматі\n\n'
                            'ДД.ММ. РРРР.\n\n'
                            ' Приклад::\n\n'
                            ' 24.02.1992\n\n'
                            'Введите дату рождения пленного в формате\n\n'
                            'ДД.ММ.ГГГГ.\n\n'
                            'Пример::\n\n'
                            ' 24.02.1992')
    bot.register_next_step_handler(sent2, user_answer2)
def user_answer2(message):
    data = message.text
    answers.append(data)
    sent3 = bot.send_message(message.chat.id,'Вкажіть контакти полоненого:\n\nУкажите контакты пленного:')
    bot.register_next_step_handler(sent3, user_answer3)
def user_answer3(message):
    kontaktplenn = message.text
    answers.append(kontaktplenn)
    sent4 = bot.send_message(message.chat.id,'Вкажіть адресу проживання полоненого:\n\nУкажите адрес проживания пленного:')
    bot.register_next_step_handler(sent4, user_answer4)
def user_answer4(message):
    adres = message.text
    answers.append(adres)
    sent5 = bot.send_message(message.chat.id, 'Військова частина полоненого (якщо не знаєте, вкажіть не знаю або -):\n\n'
                                              'Воинская часть пленного (если не знаете, укажитe не знаю или -):')
    bot.register_next_step_handler(sent5, user_answer5)
def user_answer5(message):
    piece = message.text
    answers.append(piece)
    sent6 = bot.send_message(message.chat.id,'Звання полоненого (якщо не знаєте, вкажіть не знаю або -):\n\n'
                                             'Звание пленного (если не знаете, укажитe не знаю или -):')
    bot.register_next_step_handler(sent6, user_answer6)
def user_answer6(message):
    rank = message.text
    answers.append(rank)
    sent7 = bot.send_message(message.chat.id,'Додаткова інформація, що б ми могли впізнати Ваших рідних:\n\n'
                                             'Дополнительная информация, что бы мы могли опознать Ваших родных:')
    bot.register_next_step_handler(sent7, user_answer7)
def user_answer7(message):
    dopolinfo = message.text
    answers.append(dopolinfo)
    sent8 = bot.send_message(message.chat.id,'Вкажіть ваше ПІБ, в форматі\n\n'
                                             'Прізвище Ім я По Батькові:\n\n'
                                             'Укажите  Ваше ФИО, в формате\n\n\n'
                                             'Фамилия Имя Отчество:')
    bot.register_next_step_handler(sent8, user_answer8)
def user_answer8(message):
    myfio = message.text
    answers.append(myfio)
    sent9 = bot.send_message(message.chat.id,'Вкажіть вашу електронну пошту, Viber, Telegram або WhatsApp:\n\n'
                                             'Укажите  Вашу электронную почту, Viber, Telegram или WhatsApp:')
    bot.register_next_step_handler(sent9, user_answer9)
def user_answer9(message):
    svz = message.text
    answers.append(svz)
    sent10 = bot.send_message(message.chat.id,'Ким доводитесь полоненому? Спорідненість?:\n\n'
                                              'Кем приходитесь пленному? Родство?:')
    bot.register_next_step_handler(sent10, user_answer10)
def user_answer10(message):
    rodstvo = message.text
    answers.append(rodstvo)
    bot.send_message(message.chat.id,'Ваша заявка збережна. Надішліть фото полоненого в цей чат, воно буде прикріплено до заявки.\n\n'
                                              'Ваша заявка сохранена. Отправьте фото пленного в этот чат, оно будет прикреплено к заявке')
    bot.send_message(5636064377, f'заявка от <b>{message.from_user.username}: </b>', parse_mode='html')
    bot.send_message(5636064377, f''
                                      f'<b>Номер:</b> {answers[0]}\n'
                                      f'<b>ФИО:</b> {answers[1]}\n'
                                      f'<b>Дата:</b> {answers[2]}\n'
                                      f'<b>Контакты пленного:</b> {answers[3]}\n'
                                      f'<b>Aдрес:</b> {answers[4]}\n'
                                      f'<b>Военная часть:</b> {answers[5]}\n'
                                      f'<b>Звание пленного:</b> {answers[6]}\n'
                                      f'<b>Опазнаваемые знаки:</b> {answers[7]}\n'
                                      f'<b>ФИО отправителя:</b> {answers[8]}\n'
                                      f'<b>Мои контакты:</b> {answers[9]}\n'
                                      f'<b>Родство:</b> {answers[10]}\n',parse_mode='html')

@bot.message_handler(content_types=['photo'])
def photo(message):
    mess1 = f'фотография от <b>{message.from_user.username}: </b>'
    bot.send_message(5636064377, mess1, parse_mode='html')
    bot.send_photo(5636064377,message.photo[0].file_id)
    bot.send_message(message.chat.id,
                     'если у вас есть информация для ещё одной заявки,\nнапишите /start\n\n'
                     'якщо у вас є інформація для ще однієї заявки,\nнапишіть /start')
bot.infinity_polling()
