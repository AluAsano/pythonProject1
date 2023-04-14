a = 100
tkb = 5.6
skb = 5.9
vtb = 4.28
sber = 4.0
sum_str = input("Укажите сумму, которую хотите внести : ")
sum = int(sum_str)
tkb_dp = sum / a * tkb
skb_dp = sum / a * skb
vtb_dp = sum / a * vtb
sber_dp = sum / a * sber
tkb_dp = int(tkb_dp)
skb_dp = int(skb_dp)
vtb_dp = int(vtb_dp)
sber_dp = int(sber_dp)
print("Депозит в банке 'ТКБ' составит: ", tkb_dp)
print("Депозит в банке 'СКБ' составит: ", skb_dp)
print("Депозит в банке 'ВТБ' составит: ", vtb_dp)
print("Депозит в банке 'СБЕР' составит: ", sber_dp)
all_dp = [tkb_dp, skb_dp, vtb_dp, sber_dp]
max_dp = max(all_dp)
print("Наибольший депозит составит: ", max_dp)