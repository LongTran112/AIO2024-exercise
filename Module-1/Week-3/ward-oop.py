from abc import ABC, abstractmethod
from typing import List
from datetime import date

class Person(ABC):
    def __init__(self, name, yob) -> None:
        self._name = name
        self._yob = yob
    
    @abstractmethod
    def __str__(self) -> str:
        pass

class Student(Person):
    def __init__(self, name, yob, grade) -> None:
        super().__init__(name, yob)
        self.__grade = grade
    
    def __str__(self) -> str:
        return f"{self._name} {self._yob} {self.__grade}"

class Teacher(Person):
    def __init__(self, name, yob, subject) -> None:
        super().__init__(name, yob)
        self.__subject = subject

    def __str__(self) -> str:
        return f"{self._name} {self._yob} {self.__subject}"
    
class Doctor(Person):
    def __init__(self, name, yob, specialist) -> None:
        super().__init__(name, yob)
        self.__specialist = specialist

    def __str__(self) -> str:
        return f"{self._name} {self._yob} {self.__specialist}"

class Ward():
    def __init__(self, name, person_list: List[Person] = None) -> None:
        self.__name = name
        self.__person_list = person_list if person_list is not None else []

    def __str__(self) -> str:
        return f"{self.__name} {self.__person_list}"
    
    def add_person(self, person: Person) -> None:
        self.__person_list.append(person)

    def count_doctor(self) -> int:
        count = 0
        for person in self.__person_list:
            if(type(person) == Doctor):
                count += 1
        return count

    def sort_age(self) -> List[Person]:
        return sorted(self.__person_list, key=lambda p: p._yob)

    def compute_average(self) -> float:
        total_year = sum(person._yob.year for person in self.__person_list)
        return total_year/len(self.__person_list)

person1 = Student("Long", date(2000, 10 , 4), 10)
person2 = Teacher("Tin", date(1990, 5 ,5), "Math")
person3 = Doctor("Ha", date(1980, 6, 6), "Heart")
person4 = Doctor("Minh", date(1970, 9, 9), "Skin") 

persons = [person1, person2, person3, person4]

ward = Ward("Go Vap", persons)
ward.add_person(Doctor("Phuoc", date(2001, 10, 10), "Eye"))

print(ward.count_doctor())

persons_sorted_by_yob = ward.sort_age()

[print(person) for person in persons_sorted_by_yob]

print(ward.compute_average())