#Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

Weekday = int(input('Введите номер дня недели '))

if Weekday >= 6 and Weekday < 8:
    print('Это выходной!')
    
elif Weekday <6 and Weekday > 1:
    print('Это будний день')
else:
    print('Введите число в соответствии с днем недели (от 1 до 7)')
