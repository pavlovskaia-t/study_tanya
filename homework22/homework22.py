from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship


DATABASE_URL = "postgresql://postgres:unitytest@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

student_courses = Table(
    'student_courses', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)
    courses = relationship("Courses", secondary=student_courses, back_populates="students")

class Courses(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    students = relationship("Student", secondary=student_courses, back_populates="courses")

Base.metadata.create_all(engine)

course_names = ["Math", "Physics", "Chemistry", "History", "English"]
courses = [Courses(name=name) for name in course_names]
session.add_all(courses)
session.commit()

# додавання людей в таблицю
students = [
    Student(name="Alice", age=20, courses=[courses[0], courses[1]]),  # Math, Physics
    Student(name="Bob", age=21, courses=[courses[1]]),                 # Physics
    Student(name="Charlie", age=22, courses=[courses[0], courses[2]]), # Math, Chemistry
    Student(name="Diana", age=20, courses=[courses[2], courses[3]]),  # Chemistry, History
    Student(name="Ethan", age=23, courses=[courses[4]]),               # English
    Student(name="Fiona", age=21, courses=[courses[0], courses[4]]),   # Math, English
    Student(name="George", age=22, courses=[courses[1], courses[3]]),  # Physics, History
    Student(name="Hannah", age=20, courses=[courses[2]]),              # Chemistry
    Student(name="Ian", age=23, courses=[courses[3], courses[4]]),     # History, English
    Student(name="Julia", age=21, courses=[courses[0], courses[1], courses[2]])  # Math, Physics, Chemistry
]

session.add_all(students)
session.commit()


print([s.name for s in session.query(Courses).filter_by(name="Math").first().students]) # тут пошук за назвою курса, але він чогось не працює
print([c.name for c in session.query(Student).filter_by(name="Alice").first().courses]) # тут пошук за іменем

student = session.query(Student).filter_by(name="Bob").first() # тут видалення студента
session.delete(student)
session.commit()







