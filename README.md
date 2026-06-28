# GoldenRatio

Python-библиотека для точной арифметики в фи-еричной системе счисления (phinary).  
Основание системы — золотое сечение φ = (1+√5)/2 ≈ 1.618...

В отличие от float, все вычисления абсолютно точные — числа хранятся в виде `a + b·√5` через `Fraction`.

**Возможности:**
- Точная арифметика без потери точности (сложение, вычитание, умножение)
- Перевод целых чисел в фи-еричную систему счисления
- Вычисление степеней золотого сечения φⁿ для любого n
- Обратный перевод из фи-записи в целое число
- Сравнение чисел (`<`, `<=`, `==`)

---

## Установка

```bash
pip install golden-ratio
# или
uv add golden-ratio
```

---

## Быстрый старт

```python
import goldenratio as gr

a = gr.GoldenNumber(11, 0)
b = gr.GoldenNumber(4, 0)

result = a + b
print(result)          # 15 + 0·√5
print(int(result))     # 15
print(gr.fi_degree(5)) # φ⁵ = 5/2 + 5/2·√5
```

---

## API

| Функция | Описание | Пример |
|---|---|---|
| `GoldenNumber(a, b)` | Число вида `a + b·√5` | `GoldenNumber(3, 0)` |
| `normalize(value)` | Перевод в фи-запись | `normalize(a)` |
| `fi_degree(n)` | Вычислить φⁿ | `fi_degree(5)` |

### Арифметика

| Операция | Пример |
|---|---|
| Сложение | `a + b` |
| Вычитание | `a - b` |
| Умножение | `a * b` |
| Сравнение | `a < b`, `a <= b`, `a == b` |

---

## Авторы

Яна — anaermakova948@gmail.com  https://github.com/Yana5193

Дима — babygreenyoda@yandex.ru  https://github.com/DemiusHTTV