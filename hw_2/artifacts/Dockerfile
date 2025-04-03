# Базовый образ с Python
FROM python:3.9-slim

# Установим LaTeX и необходимые утилиты
RUN apt-get update && apt-get install -y \
    texlive-latex-base \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    texlive-latex-extra \
    texlive-xetex \
    texlive-bibtex-extra \
    texlive-lang-cyrillic \
    ghostscript \
    && rm -rf /var/lib/apt/lists/*

# Создаем директорию приложения
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Генерируем .tex файлы и pdf
CMD python main.py && \
    pdflatex table.tex && \
    pdflatex pic.tex
