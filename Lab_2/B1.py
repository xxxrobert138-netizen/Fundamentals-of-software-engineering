import os

input_filename = input("Введите полное имя входного файла: ")

if not os.path.exists(input_filename):
    print(f"Ошибка: Файл {input_filename} не найден в папке с программой!")
else:
    with open(input_filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    first_line_data = lines[0].split()
    num_locations = int(first_line_data[0])
    scale = float(first_line_data[1])

    legs_miles = []
    total_distance = 0.0

    for line in lines[1:]:
        line = line.strip()
        if line:
            legs_miles.append(float(line))
            total_distance += round(float(line) * scale, 1)

    print("Pyrski Robert")
    print("Simple Map Distance Computations")
    print(f"Map Scale Factor: {scale:.2f} miles per inch")
    print("     Map     Mileage")
    print("     Measure Distance")
    print("=========================================================================")
    leg_number = 1
    for miles in legs_miles:
        print(f"# {leg_number}: {miles:.1f}   {miles * scale:.1f}")
        leg_number += 1
    print("=========================================================================")
    print(f"Total Distance: {total_distance:.1f}")