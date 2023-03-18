from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # Дата сьогодні
    today = datetime.today()
    # Наступний понеділок - поточна дата плюс кількість днів до наступного понеділка
    next_monday = today + timedelta(days=(7 - today.weekday()))
    for i in range(7):
        # Дата наступного понеділка + кількість днів від цього понеділка
        current_day = next_monday + timedelta(days=i)
        # День тижня (текст)
        current_day_name = current_day.strftime("%A")
        current_day_users = []

        # Перевірка чи день народження у суботу або неділю
        if current_day.weekday() == 5 or current_day.weekday() == 6:
            for user in users:
                # Дата народження людини
                user_birthday = datetime.strptime(user["birthday"], "%d-%m-%Y")
                # Якщо співпадає з поточним днем
                if user_birthday.day == current_day.day and user_birthday.month == current_day.month:
                    current_day_users.append(user["name"])
            if current_day_users:
                users_string = ", ".join(current_day_users)
                # Виведення списку користувачів, яких потрібно привітати наступного понеділка, тому що дн у вихідний день
                print(f"Monday, after next week: {users_string}")
        else:
            for user in users:
                # Витягуємо дату і перетворюємо з рядка на об'єкт
                user_birthday = datetime.strptime(user["birthday"], "%d-%m-%Y")
                # Перевіряємо чи збігається дата з поточним днем
                if user_birthday.day == current_day.day and user_birthday.month == current_day.month:
                    current_day_users.append(user["name"])
            if current_day_users:
                users_string = ", ".join(current_day_users)
                print(f"{current_day_name}: {users_string}")


if __name__ == '__main__':
    
    users = [{'name': 'Oleh', 'birthday': '23-03-1996'},
             {'name': 'Maryanna', 'birthday': '20-03-1997'},
             {'name': 'Ivan', 'birthday': '21-03-1478'},
             {'name': 'Ser Gay', 'birthday': '22-03-1456'},
             {'name': 'Vitalik', 'birthday': '22-03-1236'},
             {'name': 'Artem', 'birthday': '24-03-1564'},
             {'name': 'Orest', 'birthday': '25-03-1879'}]
    
    get_birthdays_per_week(users)