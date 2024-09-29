# Absolute Supreme

## Условие

На вход подаются тройки чисел через запятую, последняя строка ввода — пустая. Между тройками введён частичный порядок: $(x_{0}, x_{1}, x_{2}) \ll (y_{0}, y_{1}, y_{2})$, если $\exist i, j, k: (x_{0}, x_{1}, x_{2}) \neq (y_{i}, y_{j}, y_{k})$ и $x_{0} \leq y_{i}, x_{1} \leq y_{j}, x_{2} \leq y_{k}, i \neq j \neq k$. Отсортировать последовательность по убыванию, по возможности не меняя следования элементов: каждая тройка должна быть «не меньше» (т. е. утверждение $A \ll B$ неверно) следующих за ней. Разрешается использовать устойчивый «тяжёлый» алгоритм
сортировки с квадратичной сложностью (например, сортировку выбором).

> В формулировке присутствует неоднозначность, так что в этом семестре в качестве решения необходимо реализовать описанный ниже неэффективный алгоритм (чуть ли не кубической сложности):
> 1. Найти первую тройку, которая не меньше всех остальных
> 2. Удалить её из списка и вставить в его начало
> 3. Повторить п. п. (1) - (3) над оставшимся фрагментом списка (без вставленного элемента)

### Input
```
7,5,2
1,7,1
1,2,3
12,11,0
2,3,4
6,7,8
```

**Пояснение**:

Согласно алгоритму:

1. (12,11,0), потому что:
    - (7,5,2) ≪ (6,7,8)
    - (1,7,1) ≪ (7,5,2)
    - (1,2,3) ≪ (7,5,2)
    - (12,11,0) → первая тройка, которая не меньше всех остальных

2. (6,7,8):
    - (7,5,2) ≪ (6,7,8)
    - (1,7,1) ≪ (7,5,2)
    - (1,2,3) ≪ (7,5,2)
    - (2,3,4) ≪ (7,5,2)
    - (6,7,8) → первая тройка, которая не меньше всех остальных, кроме  - (12,11,0) (её она тоже не меньше, но это не имеет значения)

3. (7,5,2)

4. (1,7,1)

5. (2,3,4):
    - (1,2,3) ≪ (2,3,4)
    - (2,3,4) →

6. (1,2,3)

### Output
```
12, 11, 0
6, 7, 8
7, 5, 2
1, 7, 1
2, 3, 4
1, 2, 3
```