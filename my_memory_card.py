#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QGroupBox, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QButtonGroup
from random import *
#создание приложения и главного окна
app = QApplication([])
main_win = QWidget()
main_win.move(700,70)
main_win.setWindowTitle('Memory Card')

btnOK = QPushButton('Ответить')
lb_question = QLabel('abcd')

RadioGroupBox = QGroupBox('Варианты ответа')
btn_ans1 = QRadioButton('a')
btn_ans2 = QRadioButton('b')
btn_ans3 = QRadioButton('c')
btn_ans4 = QRadioButton('d')
answers = [btn_ans1,btn_ans2,btn_ans3,btn_ans4]

class Question():
    def __init__(self, question, right_ans,wrong1,wrong2,wrong3):
        self.question = question
        self.right_ans = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('2+2', '4', '2', '5', '6'))
question_list.append(Question('56*23', '1288', '1344', '1233', '1432'))
question_list.append(Question('4386/51', '86', '67', '87', '76'))
question_list.append(Question('458+584', '1042', '1038', '1034', '1045'))
question_list.append(Question('9742-5227', '4515', '4856', '4521', '4825'))
question_list.append(Question('65*45', '2925', '2985', '2885', '2865'))
question_list.append(Question('3015/45', '67', '56', '63', '53'))
question_list.append(Question('5426-2356', '3070', '3054', '3045', '3065'))



layoutA1 = QHBoxLayout()
layoutA2 = QVBoxLayout()
layoutA3 = QVBoxLayout()

layoutA2.addWidget(btn_ans1)
layoutA2.addWidget(btn_ans2)
layoutA3.addWidget(btn_ans3)
layoutA3.addWidget(btn_ans4)

layoutA1.addLayout(layoutA2)
layoutA1.addLayout(layoutA3)

RadioGroupBox.setLayout(layoutA1)

AnsGroupBox = QGroupBox('Результат теста')
lb_result = QLabel('Прав ты или нет?')
lb_correct = QLabel('Ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_correct, alignment=Qt.AlignCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_ans1)
RadioGroup.addButton(btn_ans2)
RadioGroup.addButton(btn_ans3)
RadioGroup.addButton(btn_ans4)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)

layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btnOK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def next_question():
    main_win.total += 1
    print('Статистика\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов: ', main_win.score)
    cur_question = randint(0, len(question_list)-1)
    q = question_list[cur_question]
    ask(q)

def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_ans)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    lb_correct.setText(q.right_ans)
    show_question()

def show_correct(res):
    lb_result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print('Статистика\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов: ', main_win.score)
        print('Рейтинг: ', round((main_win.score/main_win.total*100), 2), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')


def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btnOK.setText('Ответить')
    RadioGroup.setExclusive(False)
    btn_ans1.setChecked(False)
    btn_ans2.setChecked(False)
    btn_ans3.setChecked(False)
    btn_ans4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btnOK.setText('Следующий вопрос')

def start_test():
    if btnOK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

btnOK.clicked.connect(start_test)



main_win.score = 0
main_win.total = 0
next_question()
main_win.resize(700,400)
main_win.setLayout(layout_card)
main_win.show()
app.exec_()

