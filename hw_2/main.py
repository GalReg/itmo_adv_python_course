from latex_generator_module.latex_generator import generate_latex_table, generate_latex_image

# Таблица:

data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]
latex_code = generate_latex_table(data)

with open("table.tex", "w", encoding="utf-8") as file:
    file.write(latex_code)

# Картинка:

latex_image_code = generate_latex_image('cat_pic.jpg')

with open("pic.tex", "w", encoding="utf-8") as file:
    file.write(latex_image_code)