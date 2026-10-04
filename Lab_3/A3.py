prev_reading = int(input())
curr_reading = int(input())

if curr_reading >= prev_reading:
    used_gas = curr_reading - prev_reading
else:
    used_gas = (10000 - prev_reading) + curr_reading

bill = 0.0

if used_gas <= 300:
    bill = 21.0
else:
    bill += 21.0
    gas_in_range_2 = min(used_gas - 300, 300)
    bill += gas_in_range_2 * 0.06

    if used_gas > 600:
        gas_in_range_3 = min(used_gas - 600, 200)
        bill += gas_in_range_3 * 0.04

        if used_gas > 800:
            gas_in_range_4 = used_gas - 800
            bill += gas_in_range_4 * 0.025

avg_price = bill / used_gas if used_gas > 0 else 0.0

print("Предыдущее Текущее Использовано К оплате Ср. цена m^3")
print(f"{prev_reading:<11} {curr_reading:<7} {used_gas:<12} {bill:<8.2f} {avg_price:.2f}")
