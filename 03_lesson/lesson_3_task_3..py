from adress import Adress
from mailing import Mailing

to_address = Adress("456800", "Саратов", "Ленина", "21", "39")
from_address = Adress("351624", "Москва", "Тверская", "52", "42")

mailing = Mailing(to_address, from_address, 1500, "001")

print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.flat} в "
    f"{mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
    f"{mailing.to_address.house} - {mailing.to_address.flat}. "
    f"Стоимость {mailing.cost} рублей."
)