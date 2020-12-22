import json as jn

import requests as rq

api_url = 'https://api.exchangeratesapi.io/latest?base='
# latest?base= değerini değişken olması için boş bıraktık(hangi döviz türü bazlı olduğunu belirtir)

bozdurulacak_döviz = input("bozdurulacak döviz türü?: ")
alınacak_döviz = input("alınacak döviz türü?: ")

miktar = int(input(f"ne kadar {bozdurulacak_döviz} bozdurmak istiyorsunuz?: "))

talep = rq.get(api_url+bozdurulacak_döviz)
# bilgiye ulaşmak için adrese bir talep yolladık + dan sonra kullanıcıdan alınacak döviz türü bilgisine ulaşmak için adresin sonuna ekledik
jon = jn.loads(talep.text)
# adresteki bilgiye text ile ulaştık ve kullanabilmek için loads metodunu kullandık

print("1 {0} = {1} {2}".format(bozdurulacak_döviz,jon["rates"][alınacak_döviz],alınacak_döviz))
print("{0} {1} = {2} {3}".format(miktar,bozdurulacak_döviz,miktar*jon["rates"][alınacak_döviz],alınacak_döviz))
