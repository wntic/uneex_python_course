# Virtual Turtle

## Условие

Написать параметрическую генератор-функцию `turtle(coord, direction)`, описывающую движение «черепахи» по координатной плоскости. `coord` — это кортеж из двух целочисленных начальных координат, `direction` описывает первоначальное направление (0 — восток, 1 — север, 2 — запад, 3 — юг). Координаты увеличиваются на северо-восток. Генератор принимает три команды — `"f"` (переход на 1 шаг вперёд), `"l"` (поворот против часовой стрелки на $90 \degree$) и `"r"` (поворот по часовой стрелке на $90 \degree$) и возвращает текущие координаты черепахи.

### Input

```python
robo = turtle((0, 0), 0)
start = next(robo)
for c in "flfrffrffr":
    print(*robo.send(c))
```

### Output

```
1 0
1 0
1 1
1 1
2 1
3 1
3 1
3 0
3 -1
3 -1
```
