total_tickets = int(input('Укажите какое кол-во билетов вы хотите зарезервировать : '))
ticket = 1
midl_ticket = 0
elder_ticket = 0
while ticket <= total_tickets:
    ticket_x = int(input('Укажите возраст владельца билета : '))
    if ticket_x > 0:
        if 18 <= ticket_x < 25:
            midl_ticket += 1
        elif ticket_x >= +25:
            elder_ticket += 1
        ticket += 1
    else:
        print('Возраст указан неверно!')
sum_ = midl_ticket * 990 + elder_ticket * 1390
if total_tickets > 3:
    sum_ = sum_ / 100 * 90
print('Общая стоимость билетов : ', int(sum_))