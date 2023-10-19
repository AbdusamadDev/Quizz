from django.test import TestCase

context = [
    {
        "id": 21,
        "answers": {"a": "10", "b": "2", "c": "5", "correct_answer": "a"},
        "text": "print(5 * 2) natijasi nima?",
    },
    {
        "id": 22,
        "answers": {"a": "and", "b": "or", "c": "not", "correct_answer": "c"},
        "text": "Quyidagilardan qaysi mantiqiy operator emas?",
    },
    {
        "id": 23,
        "answers": {"a": "3", "b": "2", "c": "1", "correct_answer": "b"},
        "text": "print(4 // 2) natijasi nima?",
    },
    {
        "id": 24,
        "answers": {"a": "0", "b": "-1", "c": "1", "correct_answer": "b"},
        "text": "List `my_list`ning oxirgi elementini qanday olish mumkin?",
    },
    {
        "id": 25,
        "answers": {"a": "False", "b": "True", "c": "None", "correct_answer": "a"},
        "text": "print(5 < 3) natijasi nima?",
    },
    {
        "id": 26,
        "answers": {"a": "5", "b": "10", "c": "15", "correct_answer": "a"},
        "text": "print(10 // 2) natijasi nima?",
    },
    {
        "id": 27,
        "answers": {
            "a": "list.append(x)",
            "b": "list.add(x)",
            "c": "list.insert(x)",
            "correct_answer": "a",
        },
        "text": "Listga yangi element qo'shish uchun qaysi metod ishlatiladi?",
    },
    {
        "id": 28,
        "answers": {
            "a": "List",
            "b": "String",
            "c": "Dictionary",
            "correct_answer": "b",
        },
        "text": "index() metodi qaysi turdagi o'zgaruvchilarda ishlatiladi?",
    },
    {
        "id": 29,
        "answers": {"a": "3", "b": "2", "c": "1", "correct_answer": "a"},
        "text": "len('abc') natijasi nima?",
    },
    {
        "id": 30,
        "answers": {"a": "+", "b": "-", "c": "*", "correct_answer": "b"},
        "text": "Ayirish amalini bajaruvchi operator qaysi?",
    },
]


import requests

# Loop through your questions and answers
for i in context:
    response = requests.post("http://127.0.0.1:8000/api/questions/", json=i)

    # Check if the request was successful
    if response.status_code == 200 or response.status_code == 201:
        print(f"Successfully posted question with id {i['id']}")
    else:
        print(
            f"Failed to post question with id {i['id']}. Status code: {response.status_code}"
        )
