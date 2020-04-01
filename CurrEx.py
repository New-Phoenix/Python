import json; import requests
class Crypto:
        def __init__(self, value):
                self.value = value
        def translate(self, crypto, newcrypto):
                self.crypto = crypto
                self.newcrypto = newcrypto
                a = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={self.crypto}&tsyms={self.newcrypto}')
                c = a.text
                b = json.loads(c)
                d = b[self.newcrypto]
                return d * self.value
money1cur = input('Currency?: ')
money1val = int(input('Amount?: '))
money1to = input('Exchange to?: ')
themoney = Crypto(money1val)
print(money1to + ' ' + str(themoney.translate(money1cur, money1to)))
input()
