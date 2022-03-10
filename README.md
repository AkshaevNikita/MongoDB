# Отчет по MongoDB

Будем изучать Mongo используя docker.

1. Для начала предоставим права обычному пользователю.

![alt text](https://github.com/AkshaevNikita/MongoDB/blob/main/pic1.jpg?raw=true)

2. Далее создаем и запускаем контейнер mongodb.

![alt text](https://github.com/AkshaevNikita/MongoDB/blob/main/pic2.jpg?raw=true)

3. Теперь нужно загрузить данные, для этого нужно узнать IP-адрес хоста.

![alt text](https://github.com/AkshaevNikita/MongoDB/blob/main/pic4.jpg?raw=true)

![alt text](https://github.com/AkshaevNikita/MongoDB/blob/main/pic5.jpg?raw=true)

4. Импортируем данные из файла, используя команду mongoimport. В даной базе данных есть поля Customer_ID, Genre, Age, Annual Income (k$), Spending Score (1 - 100).

![alt text](https://github.com/AkshaevNikita/MongoDB/blob/main/pic6.jpg?raw=true)

5. Видим, что появилась новая база данных mydb.

![alt text](https://github.com/AkshaevNikita/MongoDB/blob/main/pic7.jpg?raw=true)

6. Сделаем несколько запросов на выборку.

![alt text](https://github.com/AkshaevNikita/MongoDB/blob/main/pic8.jpg?raw=true)

![alt text](https://github.com/AkshaevNikita/MongoDB/blob/main/pic9.jpg?raw=true)

7. Сделаем update() и updateMany().

![alt text](https://github.com/AkshaevNikita/MongoDB/blob/main/pic10.jpg?raw=true)

![alt text](https://github.com/AkshaevNikita/MongoDB/blob/main/pic11.jpg?raw=true)

8. Для того, чтобы исследовать производительность индексов, нам нужна база данных побольше (В mydb 200 записей). Cгенерируем базу даных с 1 000 000 записями и импортируем аналогичным образом в Mongo. (Данные сгенериррованы с помощью python https://github.com/AkshaevNikita/MongoDB/blob/main/generate_data.py)

![alt text](https://github.com/AkshaevNikita/MongoDB/blob/main/pic12.jpg?raw=true)

9.Убедимся, что новая база данных db_research появилась, обратим внимание на размер базы данных 0.145 GB.

![alt text](https://github.com/AkshaevNikita/MongoDB/blob/main/pic13.jpg?raw=true)

10. В нашей коллекции users есть поля: age - сколько лет пользователю, full_name - полное имя юзера, text - набор символов, сгенерированный рандомно для каждого пользователя 

11. Начнем работу с индексами. Для начала воспользуемся меодом getIndexes(), чтобы убедиться, что пока у нас есть только индекс по умолчанию

![alt text](https://github.com/AkshaevNikita/MongoDB/blob/main/pic14.jpg?raw=true)

12. Произведем запрос find(), который ищет документы, в которых поле text начинается на "abc", и с помощью метода explain() произведем анализ запроса.

![alt text](https://github.com/AkshaevNikita/MongoDB/blob/main/pic18.jpg?raw=true)

![alt text](https://github.com/AkshaevNikita/MongoDB/blob/main/pic15.jpg?raw=true)

Видим, что под наш запрос подходит 56 документов, проверено было 1 000 000 документов, то есть была проверена вся коллекция (об этом говорит поле "COLLSCAN"). И самое главное, на что стоит обратить внимание, это затраченное время - 1043 ms.

13. Теперь создадим индекс на поле "text" и также исследуем предыдущий запрос с помощью метода explain().

![alt text](https://github.com/AkshaevNikita/MongoDB/blob/main/pic16.jpg?raw=true)

![alt text](https://github.com/AkshaevNikita/MongoDB/blob/main/pic17.jpg?raw=true)

Всё также подходят 56 документов, но теперь проверена не вся коллекция из 1 000 000 документов, а ровно 56. С помощью индексов мы добились времени -- 6 ms, что в сотни раз меньше, чем запрос без инексов.
