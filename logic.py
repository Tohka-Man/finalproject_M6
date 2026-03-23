import sqlite3
import os
import sys
import datetime
from typing import List, Tuple, Optional, Any

# Функция для создания базы данных и всех таблиц
def create_database():
    
    # Подключаемся к базе данных (файл database.db будет создан автоматически)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Таблица категорий
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    # Таблица производителей
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS manufacturers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    # Таблица товаров
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            manufacturer_id INTEGER,
            category_id INTEGER,
            FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(id),
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )
    ''')

    # Таблица размеров
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sizes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            size TEXT NOT NULL
        )
    ''')

    # Таблица наличия (связь товаров и размеров)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS availability (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            size_id INTEGER NOT NULL,
            is_available BOOLEAN DEFAULT 0,
            quantity INTEGER DEFAULT 0,
            FOREIGN KEY (product_id) REFERENCES products(id),
            FOREIGN KEY (size_id) REFERENCES sizes(id)
        )
    ''')

    # Сохраняем изменения и закрываем соединение
    conn.commit()
    conn.close()
    print("База данных 'database.db' успешно создана!")

if __name__ == '__main__':
    create_database()
