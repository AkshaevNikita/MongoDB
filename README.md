# MongoDB

Будем изучать Mongo используя docker.

1. Для начала предоставим права обычному пользователю.

![alt text](https://github.com/AkshaevNikita/MongoDB/blob/main/pic1.jpg?raw=true)

2. Далее создаем и запускаем контейнер mongodb.

![alt text](https://github.com/AkshaevNikita/MongoDB/blob/main/pic2.jpg?raw=true)

3. Теперь нужно загрузить данные, для этого нужно узнать IP-адрес хоста.

![alt text](https://github.com/AkshaevNikita/MongoDB/blob/main/pic4.jpg?raw=true)

![alt text](https://github.com/AkshaevNikita/MongoDB/blob/main/pic5.jpg?raw=true)

4. Импортируем данные из файла, используя команду mongoimport. В даной базе данных есть поля Customer_ID, Genre, Age, Annual Income (k$), Spending Score (1 - 100).
