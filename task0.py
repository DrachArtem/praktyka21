від  випадкового  імпорту  randint


def  rand_arr ():
    RArr  = []
    для  i  в  діапазоні ( 0 , 30 ):
        RArr . append ( randint ( - 100 , 100 ))
    повернути  RArr


def  max_in_arr ( arr ):

    arr_i  =  список ( перерахувати ( arr , 0 ))
    max_i  =  max ( arr_i , ключ = lambda  i : i [ 1 ])

    повернути  max_i [ 1 ], max_i [ 0 ]


def  unpaired_arr ( arr ):
    un_p_arr  = []
    для  i  in  arr :
        якщо  i  %  2  ! =  0 :
            un_p_arr . додати ( i )
    якщо  len ( un_p_arr ) ==  0 :
        повернути  "немає непарних номерів"
    ще :
        повернути  un_p_arr


arr  =  rand_arr ()
print ( "початковий випадковий список: \ n " , обр. )
print ( "max num>" , max_in_arr ( arr ) [ 0 ], " \ n положення максимального числа>" , max_in_arr ( arr ) [ 1 ] + 1 )

# isinstance () перевіряє належність об'єкта до певного типу даних isinstance (об'єкт, тип даних)
якщо  isinstance ( unpaired_arr ( обр ), список ):
    print ( "Список неспарених чисел, відсортованих від найвищого до найнижчого: \ n " ,
          відсортовано ( неспарений_арр ( обр ), зворотний = True ))
ще :
    print ( unpaired_arr ( arr ))


# 1-Сформувати список із 30 випадкових цілих чисел від -100 до + 100.
# Знайдіть максимальний список продуктів та його порядковий номер.
# Отримати інший список, що створюється лише з непарних чисел вихідного списку
# або повідомити, що таких чисел немає.
# Отриманий список виводити за зменшенням елементів.