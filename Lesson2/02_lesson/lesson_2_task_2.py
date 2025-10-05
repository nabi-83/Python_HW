def is_year_leap (year):
   if year % 4 == 0:
        return(True)
   else:
        return(False)
year = int(input("Введите номер года: "))
print(f"год {year}: {is_year_leap (year)}")