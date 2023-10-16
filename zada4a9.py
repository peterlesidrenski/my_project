length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent_full = float(input())
volume_dm3 = (length_cm * width_cm * height_cm) / 1000
liters_needed = volume_dm3 * (1 - percent_full / 100)
print(f"{liters_needed:.2f}")

