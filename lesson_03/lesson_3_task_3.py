from address import Address
from mailing import Mailing
toAddress = Address("1569", "SPB", "uliza Pergo", "dom 47", "kv. 56")
fromAddress = Address("1569", "SPB", "uliza Pergo", "dom 47", "kv. 56")
Mail = Mailing( toAddress, fromAddress, 4800, "fgd235")

print(Mail)