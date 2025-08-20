from address import Address
from mailing import Mailing
toAddress = Address("1569", "SPB", "uliza Pergo", "dom 47", "kv. 56")
fromAddress = Address("1234", "SPB", "uliza Horb", "dom 15", "kv. 23")
Mail = Mailing( toAddress, fromAddress, 4800, "fgd235")

print(f"{Mail}")