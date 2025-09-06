
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department
class Developer(Employee):
    def __init__(self,name,salary,programming_language):
        super().__init__(name,salary)
        self.programming_language = programming_language

class TeamLead(Manager,Developer):
    def __init__(self,name,salary,department,team_size):
        Employee.__init__(self,name, salary)
        self.department = department
        self.team_size = team_size

def test_teamlead():
    teamlead = TeamLead('Mark', '1000', 'AQA','8')
    assert hasattr(teamlead, 'name')
    assert hasattr(teamlead, 'salary')
    assert hasattr(teamlead, 'department')
    assert hasattr(teamlead, 'team_size')

test_teamlead()