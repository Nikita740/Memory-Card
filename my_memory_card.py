from PyQt5.QtCore import Qt# Подключение модулей
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QRadioButton,QGroupBox,QButtonGroup) # Подключение модулей
from random import shuffle, randint # Подключение модулей
app = QApplication([]) # создание приложения
window = QWidget()#создание окна
btn = QPushButton('Ответить.')# создание кнопки
lb_question = QLabel('В каком году была основана Москва?')# созданиенадписи
class Question():
    def __init__ (self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
question_list = []
question_list.append(Question("Государственный язык Бразилии","Португальский","Бразильский","Испанский","Казахский"))
question_list.append(Question("Чего нету на флаге Казахстана?","Красного","Жёлтого","Синего","Орла"))
question_list.append(Question("Сколько государств состоит в  НАТО?","30","14","52","25"))
question_list.append(Question("Какое население в Китае?","меньше полтора миллиарда человек","больше двух миллиардов человек","меньше миллиарда человек","около двух милиардов человек"))
question_list.append(Question("В скольких странах официальная валюта это евро?","19","20","21","18"))
question_list.append(Question("У какой страны нет официальной столицы?","Науру","Ватикан","Монако","Мальта"))
question_list.append(Question("У какой страны больше всего олимпийских медалей","США","Германия","Бразилия","Норвегия"))
question_list.append(Question("Какая страна НЕ граничит с Бразилией?","Чили","Перу","Суринам","Уругвай"))
question_list.append(Question("Канатоходцы - подвижная игра какой страны?","Узбекистан","Белоруссия","Аргентина","Судан"))
question_list.append(Question("уроженцем какой страны был Эрнесто че гевара?","Аргентины","Венгрии","Перу","Китай"))
question_list.append(Question("какие страны первыми вошли в евросоюз?","Бельгия и Франция","Дания и Ирландия","Сен-Пьер и Микелон","Великобитания и Французский Алжир"))
question_list.append(Question("Какая страна считается родиной футбола?","Англия","Италия","Бразилия","Индия"))
question_list.append(Question("Какая страна Африки самая большая по населению?","Нигерия","Эфиопия","Конго","Танзания"))
question_list.append(Question("у какой страны есть остров пасхи?","Чили","Версаль","Шотландия","Англия"))
question_list.append(Question("у какой страны больше всего государственных языков?","Боливия","Бразилия","Германия","Мадагаскар"))
question_list.append(Question("Какая страна считается родиной волейбола?","США","Бруней","Йемен","Мальдивы"))
question_list.append(Question("Какое население у Индии","около 1200000000","около 570000000","около 1630000000","около 300000000"))
question_list.append(Question("Самый населённый  город США","Нью-Йорк","Лос-Анджелес","Чикаго","Филадельфия"))
question_list.append(Question("Самый красивый город в мире в 2021 году по версии pixabay","Кейптаун","Севилья","Лагос","Кулусук"))
question_list.append(Question("Сколько городов в Турции","около 500","около 200","около 800","около 300"))
question_list.append(Question("Какой государственный язык в чили","Испанский","Французский","Португальский","Английский"))
question_list.append(Question("В какой стране больше всего объектов ЮНЕСКО?","Италия","Казахстан","Испания","Африка"))
question_list.append(Question("Между какими странами находится Эверест?","Китай и Непал","Суринам и Бразилия","Франция и Германия","Белорусь и Латвия"))
question_list.append(Question("Сколько материков на земле?","6","7","5","4"))
question_list.append(Question("В каком полушарии находится Евразия?","Северном","Южном","Между ними","Ни один вариант не верен"))
question_list.append(Question("какие столицы были у древнего государства Албания?","Кабала и Партав","Винтан и Арат","Сунт и Фаин","Домав и Шотас"))
question_list.append(Question("В какой стране родился Шекспир?","Великобритания","Шотландия","США","Россия"))
question_list.append(Question("В каком веке существовал Карлукский каганат?","8-10 вв.","7-9 вв.","8-9 вв.","7-10 вв."))
question_list.append(Question("Високосный год происходит каждые","4 года","6 лет","3 года","5 лет"))
question_list.append(Question("Сколько государств входит в ООН","193","154","217","178"))
question_list.append(Question("Самая богатая страна мира","Гонконг","Африка","Китай","Гренландия"))
question_list.append(Question("Чего нету на гербе Беларуси?","Воды","Колосьей","Звезды","цветов"))
question_list.append(Question("Какую страну называли 'страной тысячи городов'?","Греко Бактрийское царство","Персию","Парфянское царство","Хорезм"))
question_list.append(Question("Сколько стран частично или полно захватил наполеон?","8","6","7","9"))
question_list.append(Question("Сколько было общесловянских богов?","2","11","7","9"))
question_list.append(Question("Сколько недель в году?","52","54","53","51"))
question_list.append(Question("Сколько праздников в декабре, в Казахстане в 2019 году?","12","8","6","15"))
question_list.append(Question("В какой стране родилась Мари кюри?","Польша","Англия","Литва","Беларусь"))
question_list.append(Question("Сколько государств входило в СССР?","15","13","17","12"))
question_list.append(Question("Сколько государств входит в СНГ?","8","13","6","10"))
RadioGroupBox = QGroupBox('Варианты ответов.') # создание группы кнопок переключателей
rbtn1 = QRadioButton('1147')# создание кнопки переключателя
rbtn2 = QRadioButton('1242')# создание кнопки переключателя
rbtn3 = QRadioButton('1861')# создание кнопки переключателя
rbtn4 = QRadioButton('1943')# создание кнопки переключателя
layout_ans1 = QHBoxLayout() # создание горизонтальной линии
layout_ans2 = QVBoxLayout() # создание вертикальной линии 
layout_ans3 = QVBoxLayout() # создание вертикальной линии
layout_ans4 = QVBoxLayout()
layout_ans2.addWidget(rbtn1)# добавление кнопки переключателя к линии
layout_ans2.addWidget(rbtn2)# добавление кнопки переключателя к линии
layout_ans3.addWidget(rbtn3)# добавление кнопки переключателя к линии
layout_ans3.addWidget(rbtn4)# добавление кнопки переключателя к линии
layout_ans1.addLayout(layout_ans2)# добавление горизонтальной линии к вертикальной линии
layout_ans1.addLayout(layout_ans3)# добавление горизонтальной линии к вертикальной линии
RadioGroupBox.setLayout(layout_ans1)# добавление вертикальной линии к группе кнопок переключателей
layout_line1 = QHBoxLayout()# создание горизонтальной линии
layout_line2 = QHBoxLayout()# создание горизонтальной линии
layout_line3 = QHBoxLayout()# создание горизонтальной линии
layout_line1.addWidget(lb_question,alignment = (Qt.AlignHCenter | Qt.AlignVCenter))# добавление надписи к горизонтальной линии и выравливание её по горизонтали и вертикали
layout_line2.addWidget(RadioGroupBox)# добавление группы кнопок переключателей к вертикальной линии
RadioGroup = QButtonGroup()# создание группы кнопок
RadioGroup.addButton(rbtn1)# добавление кнопки переключателя к группе кнопок
RadioGroup.addButton(rbtn2)# добавление кнопки переключателя к группе кнопок
RadioGroup.addButton(rbtn3)# добавление кнопки переключателя к группе кнопок
RadioGroup.addButton(rbtn4)# добавление кнопки переключателя к группе кнопок

layout_line3.addStretch(1)# растягивание линии
layout_line3.addWidget(btn,stretch = 2)# добавление кнопки к линии и растянивание её
layout_line3.addStretch(1)# растягивание линии
ansGroupBox = QGroupBox('Результат теста')# создание группы кнопок переключателей
lb_result = QLabel('Прав ты или нет?')# создание надписи
lb_correct = QLabel("Ответ будет тут!")# создание надписи
layout_res = QVBoxLayout()# создание вертикальной линии
layout_res.addWidget(lb_result,alignment=(Qt.AlignLeft | Qt.AlignTop))# добавление надписи к линии и выравнивание её к левому верхнему углу
layout_res.addWidget(lb_correct,alignment=Qt.AlignHCenter ,stretch=2)# добавлеие надписи к линии и выравнивание её по горизонтали, а также растягивание её
ansGroupBox.setLayout(layout_res)# добавление линии к группе кнопок переключателей
ansGroupBox.hide()# скрыть группу кнопок переключатеелей
layout_line2.addWidget(ansGroupBox)# добавление к линии группу кнопок переключателей
layout_card = QVBoxLayout()# создание вертикальной линии
layout_card.addLayout(layout_line1,stretch=2)# добавление к вертикальной линии горизонтальную линию и растягивание её
layout_card.addLayout(layout_line2,stretch=8)# добавление к вертикальной линии горизонтальную линию и растягивание её
layout_card.addStretch(1)# растягивание линии
layout_card.addLayout(layout_line3,stretch=1)# добавление к вертикальной линии горизонтальную линию и растягивание её
layout_card.addStretch(1)# растягивание линии
layout_card.setSpacing(5)# добавление пространаства между содержимым линии
window.total = 0
window.score = 0
#Функционал
def show_result(): # создание функции
    RadioGroupBox.hide()# скрыть группу кнопок
    ansGroupBox.show()# показать группу кнопок переключателей
    btn.setText("Следующий вопрос")# изменить текст кнопки
def show_question(): # создание функции
    RadioGroupBox.show()# показать группу кнопок
    ansGroupBox.hide()# скрыть группу кнопок переключателей
    btn.setText('Ответить')# изменить текст кнопки
    RadioGroup.setExclusive(False)# изменение параметров ограничений
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)# изменение параметров ограничений
answers = [rbtn1, rbtn2, rbtn3, rbtn4] # создание списка
def ask(q:Question): # создание функции
    shuffle(answers)# перетасовка кнопок
    answers[0].setText(q.right_answer) # изменение текста 
    answers[1].setText(q.wrong1)# изменение текста
    answers[2].setText(q.wrong2)# изменение текста
    answers[3].setText(q.wrong3)# изменение текста
    lb_question.setText(q.question)# изменение текста
    lb_correct.setText(q.right_answer)# изменение текста
    show_question()# активировать функцию
def show_correct(res): # создание функции 
    lb_result.setText(res)# изменение текста
    show_result()# активировать функцию
def check_answer(): # создание функции
    if answers[0].isChecked(): # если значение с индексом 0 нажато 
        show_correct("Правильно!")# показать 'правильно'
        window.score = window.score + 1
        print("Статистика\n-Всего вопросов:",window.total,"\n-правильных ответов:",window.score)
        print("Рейтинг:",(window.score/window.total*100),"%")
    else: # иначе
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked(): # если данные значения с индексом 1 2 3 будут нажаты 
            show_correct("Неверно!")# показать 'неверно'
def next_question():
    window.total += 1
    print("Статистика\n-Всего вопросов:",window.total,"\n-правильных ответов:",window.score)
    print("Рейтинг:",(window.score/window.total*100),"%")
    cur_question=randint(0,len(question_list)-1)
    q=question_list[cur_question]
    ask(q)
    #window_total = window_total + 1
def click_ok():
    if btn.text() == "Ответить":
        check_answer()
    else:
        next_question()

btn.clicked.connect(click_ok) # если кнопа нажата то активировать функцию
window.cur_question = -1
window.setLayout(layout_card) # присоединение линии к окну
next_question()
window.resize(400,300)
window.show() # показать окно
app.exec_()# не закрывать приложение пока не будет нажата кнопка выхода