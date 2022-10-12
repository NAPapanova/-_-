
#Функция для игрового поля
num = list(range(10))
def field(num):
   print("-"*19)
   for i in range(3):
      print("| ", num[(i*3)+1], " | ", num[(i*3)+2], " | ", num[(i*3)+3], " | ") #клетки с цифрами внутри
      print("-"*19)

#Функция для хода игрока
def player_turn(sign): #sign = "X" || "0"
   valid = False #Переменная
   while not valid:
      #Проверка на правильность входных данных
      try:
         position = int(input("Куда поставим " + str(sign)+"?""\nНа цифру: ")) #Переводим в строку для конкатенации
      except:
         print("Возможно вы ввели не число")
         continue
      #Проверка на вхождение входных данных в диапазон
      if position >= 1 and position <= 9:
         if str(num[position]) not in "X0":
            num[position] = sign
            valid = True
         else:
            print("Клетка занята!")
      else:
         print("Ошибочка)\nВведите число от 1 до 9")

#Функция для проверки на выигрыш
def check_win(num):
   win_combinations = (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7)
   for i in win_combinations:
      if num[i[0]] == num[i[1]] == num[i[2]]:
         return num[i[0]] #Возвращаем выигрышный символ при выполнении условия
   return False #Возвращаем False при отсутствии условия

#Основная функция, где включаются остальные функции
def main(num):
   counter = 0 #Заводим счетчик
   win = False #Переменная для остановки цикла(win = True) при выигрыше
   while not win:
      field(num)
      if counter % 2 == 0: #При четных ходах ставим Х
         player_turn("X")
         counter += 1
      else:
         player_turn("0") #При нечетных ставим 0
         counter+=1 #Добавляем при каждой иттерации-ходу игрока 1
      if counter > 4:
         score = check_win(num) #запускаем функцию проверки на выигрыш
         if score:
            print("\n\n")
            print("Игрок, игравший '"+ score +"', Ты выиграл эту битву!\nМои поздравления)")
            win = True
      if counter == 9:
         print("Ничья")
   field(num)
main(num)