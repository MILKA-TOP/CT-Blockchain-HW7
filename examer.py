import sys
import hashlib

#
# Получение аргументов из командной строки и занесение их в словарь.
#

args = sys.argv
FILE_ARG = "--file"
NUM_TICKETS_ARG = "--numbilets"
PARAMETER_ARG = "--parameter"
MODE_ARG = "-mode"

params = {FILE_ARG: "", NUM_TICKETS_ARG: 1, PARAMETER_ARG: 1, MODE_ARG: False}

if len(args) < 7:
    print("Please, input correct args: ./program --file <filename> --numbilets <count> --parameter <parameter>")
    exit(1)

i = 1
args_dict = {}
while i < len(args):
    if args[i] not in params.keys():
        print("Incorrect parameter: " + args[i])
        exit(1)
    else:
        if args[i] == MODE_ARG:
            params[args[i]] = True
            i += 1
            continue

        if args[i] == NUM_TICKETS_ARG or args[i] == PARAMETER_ARG:
            arg_int_value = int(args[i + 1])
            if arg_int_value < 1:
                print("Incorrect parameter: " + args[i])
                exit(1)
            params[args[i]] = int(args[i + 1])
        else:
            params[args[i]] = args[i + 1]
        i += 2

names = []
with open(params[FILE_ARG], 'r', encoding='UTF-8') as file:
    while line := file.readline().rstrip():
        names.append(line)

#
# Создаем массив билетов. В случае если количество студентов <= количества билетов, то у меня просто создается массив
# билетов [1..numbilets]. Если же студентов больше, чем билетов, данный массив билетов дублируется
# PERSONS_COUNT div TICKETS_COUNT раз.
# При наличии флага -mode мы будем удалять сгенерированный номер билета из этого массива, предоставляя следующим
# студентам меньший выбор билета. Таким образом при равном количестве билетов и студентов каждый студент получит
# уникальный номер билета
#
persons_count = len(names)
tickets_repeat_counts = persons_count // params[NUM_TICKETS_ARG]
if persons_count % params[NUM_TICKETS_ARG] != 0:
    tickets_repeat_counts += 1
tickets = [i for i in range(1, params[NUM_TICKETS_ARG] + 1)] * tickets_repeat_counts


#
# Функция по получению номера билета по имени студента (и другим параметрам, полученным ранее).
# При необходимости удаляем полученный билет из списка билетов.
#
def getTicketNumber(ticketName):
    ord_sum = int.from_bytes(hashlib.sha1(ticketName.encode('utf-8')).digest(), 'big') % (10 ** 8)
    ticket_index = (ord_sum ^ params[PARAMETER_ARG]) % len(tickets)
    ticket_number = tickets[ticket_index]

    if params[MODE_ARG]:
        del tickets[ticket_index]

    return ticket_number


for name in names:
    print(name + ": " + str(getTicketNumber(name)))
