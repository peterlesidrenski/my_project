
annual_fee = float(input())


basketball_shoes_price = 0.4 * annual_fee
basketball_outfit_price = 0.8 * basketball_shoes_price
basketball_ball_price = basketball_outfit_price / 4
basketball_accessories_price = basketball_ball_price / 5
total_cost = annual_fee + basketball_shoes_price + basketball_outfit_price + basketball_ball_price + basketball_accessories_price
print(f"Pesho has need {total_cost:.2f} leva for training!")

