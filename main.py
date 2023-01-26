# модуль это питоновский файл
# папка с питоновскими модулями это пакет
# библиотека модули и пакеты,содержится структурированная информация


# file = open('test1.txt', 'r' )    #читать текст по умолчанию
# # file.write('Hello\n')
# # file.writelines("['Hello']")
# # file.write('World')
# # file.write('Hello')
# # f = file.read(2)
# # print(file.readline())   # hello
# # print(file.readline())   # hello    John
# print(file.readlines())    #['hello\n', 'John']

# file.close()



# with open('test1.txt') as file:
#     print(file.read())
# print(file.read())




"""
json - текстовый формат для обмена данными 
сериализация(с пайтон в json) -> dump, dumps
десериализация(с json в pyhton) -> load, loads
"""
# import json
# d ={'hello': True, 'age': 2, 'name': None}
# # print(json.dumps(d))  #{"hello": true, "age": 2, "name": null} 

# json_obj = json.dumps(d)
# print(json_obj)   #{"hello": true, "age": 2, "name": null}
# print(type(json_obj))   #<class 'str'>

# python_obj = json.loads(json_obj)
# print(python_obj)    #{'hello': True, 'age': 2, 'name': None}


# import json
# with open('data.json', 'r') as file:
#     python_obj = json.loads(file.read())
#     print(python_obj)  #{'name': None}


# import json
# with open('data.json', 'r') as file:
#     python_obj = json.load(file)
#     print(python_obj) 


"""
oop, git, postgresql, (http, orm)
"""

# postgres - 
"""

связь один к одному  - unique - должен быть уникальным
postgres=# create table passport(
id serial primary key,
person_id int unique,
foreign key (person_id) references person(id));

person 
John 1
Sam 2
person(id, person_id)
# pas1 1
# pas2 1 - ошибка




# связь один ко многим
?

person 
John 1
Sam 2
person(id, person_id)
# pas1 1
# pas2 1
# pas3 1




# связь многое ко многим
student
id pk

student_teacher
id pk
t_id fk teacher(id)
s_id fk student(id)

1. 1t - 2s
2. 1t - 3s
3. 1t - 1s
"""


# способ написания кода - парадигма
"""
class - описывает поведение всех объектов
атрибут экземпляра класа - создаются внутри метода класса, через объект можно тоже obj.color = 'red'
атрбут класса
self - ccылка на объект, ссылка котрую вызываем у объекта 
setatr - назначает новый объект


магические - рработают сами в определенный момент времени 
__new__ - создает объект
__init__ - инициализирует, задает свойства объекту
__str__ - человекочитабельный
__repr__ - машинный код
__del__ - удаялет
__dict__

"""
# class A:
#     amount = 0

#     def info(self):
#         pass

#     classmethod    #
#     def info2(cls):
#         pass

#     @staticmethod   #нужен для связи без связи  к объекту и к классу 
#     def info3():
#         pass

# obj = A()
# obj.color = 'red'


""""""
# одиночное наследование
# class A:
#     a = 2

# class B(A):
#     pass

# f = B()
# f.a

# mro
# class A:
#     a = 2

# class B(A):
#     a = 3

# f = B()
# print(B.__mro__)   #(<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)


""" поиск в глубину обычно - но через мро в ширину - с лева на право"""
# class A:
#     a = 2

# class B(A):
#     a = 3

# class C(A):
#     a = 4

# class D(B, C):
#     a = 5
# f = B()
# print(B.__mro__)


"""
инкапсуляция
"""
# class A:
#     a = 2
#     _protected = 3  
#     __private = 4   #только в классе - на уровне соглашения
# print(A._A__private)  #обходной путь лучше использовать getter setter


"""
абстракция - выделение определенных действий 
все классы котрые создаются должны переопределится от класса
"""

# from abc import ABC, abstractmethod

# class A(ABC):

#     @abstractmethod
#     def f():
#         pass

"""
ассоциация - межклассовое взаимодействие как наследование

агрегация - 
компазиция - 
"""


"""
Миксины - классы примеси
расширители классов 
нельзя делать от них объекты
одну логику
не наследуется
"""


# orm - технология связывающая 
"""
host : localhost  - 127.0.1 - 
"""

# протоколы http , https - набор правил как программам общаться друг с другом


"""
github - 
"""