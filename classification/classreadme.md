# Классификация
### Входные данные
Использовался датасет с 8 признаками грибов(цвет, поверхность, форма шапочки, пятна, запах и т.д), 180 объектов, классы генерируются случайно
### Задача
Построить классификатор на основе датасета
### Решение
Использована библиотека sklearn, пока она не поддерживает категорические признаки, поэтому их пришлось сделать бинарными (например: гриб красный и незеленый и несиний). 
### Результат
![](https://github.com/oreshkichikaladnie/machine_learning/blob/main/Figure_2.png)
![](https://github.com/oreshkichikaladnie/machine_learning/blob/main/Screenshot%20from%202021-01-09%2018-44-08.png)
![](https://github.com/oreshkichikaladnie/machine_learning/blob/main/Screenshot%20from%202021-01-09%2018-44-24.png)
### Вывод
На примерах в разы меньше ветвей, чем если бы решение было переборным(переборное - это 10^5 ветвей), поэтому построен эффективный и оптимизированный классификатор
