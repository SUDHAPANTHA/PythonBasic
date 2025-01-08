#pythonic way.
us_price = {'milk': 2.05, 'bread': 2.60 ,'butter': 2.8}
exchange_rate = 135
nep_price = {item: price * exchange_rate for item, price in us_price.items()}
print("Nepali Prices:", nep_price)
#Non-pythonic way
# Define US prices
us_price = {'milk': 2.05, 'bread': 2.60, 'butter': 2.8}
er = 135
np = {}
mip = us_price['milk'] * er
bp = us_price['bread'] * er
bpy = us_price['butter'] * er
np['milk'] = mip
np['bread'] = bp
np['butter'] = bpy
print("Nepali Prices:", np)

