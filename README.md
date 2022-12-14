# ДЗ №7 К занятию “Symmetric cryptography”

## Выполнил работу Миленин Иван (M33351)

**Задание:**

**Задание:**

- Сделать программу - консольное приложение, используя языки: С/C++, Rust, Python, Go, Node.JS.
- Программа принимает три параметра командной строки, типа:
- ./program --file <filename> --numbilets 20 --parameter 42
    - Параметры: имя файла с ФИО студентов, число билетов, параметр, изменяющий распределение. Программа выдает в
      консоль строку из файла + номер билета. Номера билетов детерминировано связаны с ФИО и параметром, меняющим
      распределение. Распределение должно быть максимально равномерным
- Входные данные (параметры командной строки):
  -
        1) файл, где каждая строка - это ФИО студента, типа:

        - Иванов Иван Иванович
        - Ярцев Ярослав Ярославович
        - …
        - Петров Петр Петрович
    -
        2) число билетов N (билеты нумеруются с 1 до N (включая N))
    -
        3) численный параметр, детерминированно меняющий распределение (при его изменении распределение номеров билетов
           максимально изменяется). При использовании одного и того же параметра, одна и та же строка Фамилия-Имя из
           файла всегда генерирует один и тот же номер билета
- Выходные данные: вывод в STDOUT строк вида:
    - Иванов Иван Иванович: 21
    - Ярцев Ярослав Ярославович: 12
    - …
    - Петров Петр Петрович: 11

___________________

## Запуск

Для запуска необходимо прописать следующую команду

```
python examer.py --file data/names.txt --numbilets 15 --parameter 2 -mode
```

_P.S Флаг `-mode` можно убрать (о нем будет поподробнее далее)_

___________________

### Флаг `-mode`

Есть 2 варианта запуска программы:

1) Использование стандартного генерирования индекса, при котором некоторые билеты могут повторяться (в случае, если
   количество билетов не равно количеству студентов)
2) Исключение выбранного билета при последующих генерациях номеров билетов. Таким образом в случае, если у нас количство
   студентов и количество билетов совпадают, то у каждого студента будето точно уникальный билет (и никто ни у кого не
   сможет списать).

При каждом новом имине я генерирую индекс элементам массива `tickets`. Далее при наличии флага `-mode` удаляю его. Стоит
отметить, что если количество студентов больше количества билетов, то массив билетов генерируется следующим образом:

```
tickets = [1..TICKETS_COUNT] * ((PERSONS_COUNT div TICKETS_COUNT) + 1)

Пример массива билетов: [1, 2, ..., 5, 6, 1, 2, ..., 6, 1, ... 6]
```

## Пример вывода:

```
C:\Users\MILKA\Desktop\DESKTOP_ELEMENTS\HW\blockchain\hw7> python examer.py --file data/names.txt --numbilets 5 --parameter 132436
Иванов Иван Иванович: 1
Миленин Иван Александрович: 4
Ярцев Ярослав Ярославович: 2
Петров Петр Петрович: 5
Николай Александр Второй: 3
```

```
C:\Users\MILKA\Desktop\DESKTOP_ELEMENTS\HW\blockchain\hw7> python examer.py --file data/names.txt --numbilets 5 --parameter 2346 
Иванов Иван Иванович: 4    
Миленин Иван Александрович: 5
Ярцев Ярослав Ярославович: 3
Петров Петр Петрович: 2
Николай Александр Второй: 2
```

```
C:\Users\MILKA\Desktop\DESKTOP_ELEMENTS\HW\blockchain\hw7> python examer.py --file data/names.txt --numbilets 5 --parameter 2346 -mode
Иванов Иван Иванович: 4    
Миленин Иван Александрович: 1
Ярцев Ярослав Ярославович: 2
Петров Петр Петрович: 5
Николай Александр Второй: 3
```

