number_of_packet_with_pens = int(input("enter a number: "))
number_of_packet_with_markers = int(input("enter a number: "))
liquid = int(input("enter a number: "))
procent= int(input("enter a number: "))
price_pens = 5.80 * number_of_packet_with_pens
price_markers= 7.20 * number_of_packet_with_markers
price_liquid = 1.20 * liquid
prise = price_liquid + price_pens + price_markers
percent = (procent / 100) * prise
full_price = prise - percent
print(full_price)



