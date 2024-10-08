# Half Transpose

## Условие

Ввели $N$ строк по $N$ целых чисел (для удобства представлены тут цифрами). Полученную матрицу

```
1234
5678
9012
3456
```

попытались «транспонировать на $45 \degree$ по часовой стрелке» — получилось примерно так:

```
   1
  5 2
 9 6 3
3 0 7 4
 4 1 8
  5 2
   6
```

При этом способе поворота между числами образовались «пустые места» каждое размеров в одно число, размер матрицы увеличился до $2N-1$ $\times$ $2N-1$. Затем все числа «упали на свободные места под ними» — переместились до ближайшей незанятой ячейки:

```
   1
  562
 90173
3456284
```

Ввести построчно через запятую элементы исходной квадратной матрицы. Вывести построчно через запятую элементы получившейся матрицы (без учёта свободных ячеек)

### Input

```
1,2,3,4
5,6,7,8
9,0,1,2
3,4,5,6
```

### Output

```
1
5,6,2
9,0,1,7,3
3,4,5,6,2,8,4
```
