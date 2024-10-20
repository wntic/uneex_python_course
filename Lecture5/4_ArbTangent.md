# Arb Tangent

## Условие

Ввести числа: рациональное $A$ (целое или десятичная дробь) — угол из диапазона от $1$ до $99$ градов (метрических градусов), и натуральное $4 \leq E \leq 1000$ — точность вычисления (в терминах контекста вычислений модуля Decimal — поле perc). Вычислить значение тангенса с указанной точностью. Число Пи (если оно вам понадобится) тоже надо вычислять!

### Input

```
50
7
```

### Output

```
1.000000
```

Совет: обратите внимание на то, что точность задаётся только для вычислений, само представление числа может содержать больше знаков.

Для крайних значений с той же точностью: $tg(99^g)[7] = 63.65674$, $tg(1^g)[7] = 0.01570926$

Подсказка: всё это вычисляется с помощью рядов
Подсказка: не экономьте на точности! если ряд хорошо сходится, $1000$ знаков вычислить очень просто

Спойлер: Пи я вычислял по алгоритму Чудновских (но можно и по формуле Бэйли — Боруэйна — Плаффа), синус и косинус — простыми степенными рядами (тангенс уж больно замороченный), точность брал $2000$ и всё равно времени хватило