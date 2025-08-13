class Student:
    def __init__(self,name, last_name, age, av_score):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.av_score = av_score

    def set_score(self,new_score):
        self.av_score = new_score

st_as = Student(name='Anna', last_name='Smith', age='29', av_score='93')
st_ma = Student(name='Maria', last_name='Adams', age='23', av_score='87')
st_sr = Student(name='Sofia', last_name='Rob', age='27', av_score='78')

st_as.set_score('100')
print(f'Середній бал Анни Сміт - {st_as.av_score}')