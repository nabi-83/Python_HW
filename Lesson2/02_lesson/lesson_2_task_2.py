def is_year_leap (год):
   if год % 4 == 0:
        return(True)
   else:
        return(False)
год = int(input("Введите номер года: "))
print(f"год {год}: {is_year_leap (год)}")