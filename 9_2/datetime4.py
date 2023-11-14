from datetime import datetime, timedelta

a = datetime.now() + timedelta(days=3)

# Понедельник = 0, Вторник = 1, ..., Воскресенье = 6
print(a.weekday())

