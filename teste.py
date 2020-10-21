from models.cliente import Cliente
from models.conta import Conta

felicity: Cliente = Cliente('Felicity Jones', 'felicity@gmail.com', '123.123.123.32', '02/09/1987')
angelina: Cliente = Cliente('Angelina Jolie', 'angelina@gmail.com', '123.123.123.42', '08/07/1912')

# print(angelina)
# print(felicity)

contaf: Conta = Conta(felicity)
contaa: Conta = Conta(angelina)

#print(contaf)
#print(contaa)

