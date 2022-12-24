# Приложение определяет тип именованного объекта в тексте (город, человек, организация).

Практическое задание модуля 3 по дисциплине программная инженерия магистратуры "Инжернения машинного обучения".

## Описание используемой модели dslim/bert-base-NER.

Модель расположена в комьюнити Hugging Face по адресу:
https://huggingface.co/dslim/bert-base-NER

bert-base-NER — это точно настроенная модель BERT, готовая к использованию для распознавания именованных объектов и обеспечивающая самую современную производительность для задачи NER. Она обучена распознавать четыре типа объектов: местонахождение (LOC), организации (ORG), лица (PER) и разные (MISC).

Abbreviation	Description
O	    		Outside of a named entity
B-MIS			Beginning of a miscellaneous entity right after another miscellaneous entity
I-MIS			Miscellaneous entity
B-PER			Beginning of a person’s name right after another person’s name
I-PER			Person’s name
B-ORG			Beginning of an organization right after another organization
I-ORG			organization
B-LOC			Beginning of a location right after another location
I-LOC			Location


## Пример текста для преобразования

My name is Clara and I live in Berkeley, California.

## Примеры ответа

Возвращает строку, которая содержит список словарей с указанием 
- типа объекта - 'entity', 
- вероятности определения этого объекта - 'score', 
- порядкого номера слова в тексте - 'index',
- самого слова - 'word',
- начальной и конечной позиции символов слова в тексте - 'start', 'end'

[{'entity': 'B-PER', 'score': 0.99641764, 'index': 4, 'word': 'Clara', 'start': 11, 'end': 16}, 
{'entity': 'B-LOC', 'score': 0.996198, 'index': 9, 'word': 'Berkeley', 'start': 31, 'end': 39}, 
{'entity': 'B-LOC', 'score': 0.9990196, 'index': 11, 'word': 'California', 'start': 41, 'end': 51}]


## Запуск приложения:

**Windows
curl -X POST  http://127.0.0.1:8000/recognition/ -H "Content-Type: application/json" -d "{\"text\":\"My name is Clara and I live in Berkeley, California.\"}"

**Linux
curl -X 'POST' \
  'http://127.0.0.1:8000/recognition/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "My name is Clara and I live in Berkeley, California."
}'
