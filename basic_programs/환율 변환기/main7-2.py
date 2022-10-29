#1달러 환율
from currency_converter import CurrencyConverter

cc = CurrencyConverter("https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip")
print(cc.convert(1,"USD","KRW"))

