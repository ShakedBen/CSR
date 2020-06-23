
from math import gcd
def bind_method(value, instance):
    """Return a bound method if value is callable, or value otherwise."""
    if callable(value):
        def method(*args):
            return value(instance, *args)

        return method
    else:
        return value
def make_instance(cls):
    """Return a new object instance, which is a dispatch dictionary."""
    attributes = {}
    def get_value(name):
        if name in attributes:
            return attributes[name]
        else:
            value = cls['get'](name)
            return bind_method(value, instance)

    def set_value(name, value):
        attributes[name] = value

    instance = {'get': get_value, 'set': set_value}
    return instance
def init_instance(cls, *args):
    """Return a new object with type cls, initialized with args."""
    instance = make_instance(cls)
    init = cls['get']('__init__')
    if init:
        init(instance, *args)
    return instance
def make_class(attributes, *base_classes):
    """Return a new class, which is a dispatch dictionary."""

    def get_value(name):
        if name in attributes:
            return attributes[name]
        elif base_classes is not None:
            for base_class in base_classes:
                value = base_class['get'](name)
                if value:
                    return value

    def set_value(name, value):
        attributes[name] = value

    def new(*args):
        return init_instance(cls, *args)

    cls = {'get': get_value, 'set': set_value, 'new': new}
    return cls
def make_myDate_class():
    def __init__(self,day,month,year='2020'):
        if int(year) > 1900 and int(year) < 2100:
            self['set']('year',year)
        if int(month) > 0 and int(month) <= 12:
            self['set']('month',month)
        if int(day)> 0 and int(day)<= 30:
            self['set']('day',day)

    def __repr__(self):
        return "Date['new']({},{},{})".format(self['get']('day'),self['get']('month'),self['get']('year'))

    def __str__(self):
        string="birth day: "+ str(self['get']('day'))+'.'+str(self['get']('month'))+'.'+str(self['get']('year'))
        return string


    def getDay(self):
        return self['get']('day')
    def getMonth(self):
        return self['get']('month')
    def getYear(self):
        return self['get']('year')

    def setDay (self,day):
        if int(day)>0 and int(day)<30:
            self['set']('day',day)

    def setMonth(self,month):
        if int(month)>0 and int(month)<12:
            self['set']('month',month)
    def setYear(self,year):
        if year>int(1900) and int(year)<2100:
            self['set']('year',year)

    return make_class(locals())
Date=make_myDate_class()
n_Date=Date['new']('1','26','1997')
n_Date['get']('setMonth')('5')
print(n_Date['get']('__str__')())
print(n_Date['get']('getYear')())
print(n_Date['get']('__repr__')())
def make_person_class():
    def __init__(self, firstName, lastName, birthDate, Id):
        self['set']('firstName', firstName)
        self['set']('lastName', lastName)
        self['set']('birthDate', birthDate)
        if Id.isnumeric() and int(Id) > 0:
            self['set']('Id', Id)

    def __repr__(self):
        return "person['new']({},{},{},{})".format(self['get']('firstName'), self['get']('lastName'), self['get']('birthDate')['get']('__repr__')(), self['get']('Id'))
    def __str__(self):
        string_p ="name: "+str(self['get']('firstName'))+" "+str(self['get']('lastName'))+"\n"+str(self['get']('birthDate')['get']('__str__')())+"\nid: "+str(self['get']('Id'))+'\n'
        return string_p


    def getId(self):
        return self['get']('Id')
    def getBirthDate(self):
        return self['get']('birthDate')
    def getFirstName(self):
        return self['get']('firstName')
    def getLastName(self):
        return self['get']('lastName')
    def setId(self, Id):
        self['set']('Id',Id)
    def setBirthDate(self, BirthDate):
        self['set']('BirthDate',BirthDate)
    def setFirstName(self, firstName):
        self['set']('firstName',firstName)
    def setLastName(self, lastName):
        self['set']('lastName',lastName)



    return make_class(locals())
Person=make_person_class()
n_person=Person['new']('einav','bitton',n_Date,'8')
print(n_person['get']('__str__')())
n_person['get']('birthDate')['get']('setDay')('6')
print(n_person['get']('__str__')())
print(n_person['get']('__repr__')())
def make_student_class():

    def __init__(self,firstName, lastName, birthDate, Id,Learning,Avg,seniority_student):
        Person['get']('__init__')(self,firstName, lastName, birthDate, Id)
        self['set']('Learning',Learning)
        if Avg.isnumeric() and float(Avg) > 0:
            self['set']('Avg',float(Avg))
        if seniority_student.isnumeric() and int(seniority_student) > 0:
            self['set']('seniority_student',int(seniority_student))


    def __repr__(self):
        return "student['new']({},{},{},{},{},{},{})".format(self['get']('firstName'), self['get']('lastName'), self['get']('birthDate')['get']('__repr__')(), self['get']('Id'), self['get']('Learning'), self['get']('Avg'), self['get']('seniority_student'))

    def __str__(self):
        str_s=str(Person['get']('__str__')(self))+"Learning: " + str(self['get']('Learning'))+"\n"+"Avg: " + str(self['get']('Avg'))+"\n"+"seniority student: " + str(self['get']('seniority_student'))
        return str_s


    def getLearning(self):
        return self['get']('Learning')
    def getAve(self):
        return self['get']('Avg')
    def getSeniority(self):
        return self['get']('seniority_student')

    def setLearning(self,Learning):
        self['set']('Learning',Learning)
    def setAve(self,Avg):
        if Avg.isnumeric() and float(Avg) > 0:
            self['set']('Avg',float(Avg))
    def setSeniority(self,Seniority):
        if Seniority.isnumeric() and int(Seniority) > 0:
            self['set']('seniority_student',int(Seniority))

    def getId(self):
        return self['get']('Id')
    def getBirthDate(self):
        return self['get']('birthDate')
    def getFirstName(self):
        return self['get']('firstName')
    def getLastName(self):
        return self['get']('lastName')
    def setId(self, Id):
        self['set']('Id',Id)
    def setBirthDate(self, BirthDate):
        self['set']('BirthDate',BirthDate)
    def setFirstName(self, firstName):
        self['set']('firstName',firstName)
    def setLastName(self, lastName):
        self['set']('lastName',lastName)



    return make_class(locals(),Person)
student=make_student_class()
new_student=student['new']('einav','bitton',Date['new']('26','6','1997'),'318231750','787','89','87')
print(new_student['get']('__repr__')())
print(new_student['get']('__str__')())

def make_Faculty_class():

    def __init__(self, firstName, lastName, birthDate, Id, Teaching, Salary, seniority_faculty):
        Person['get']('__init__')(self, firstName, lastName, birthDate, Id)
        self['set']('Teaching', Teaching)
        self['set']('Salary', Salary)
        self['set']('seniority_faculty', seniority_faculty)

    def __repr__(self):
        return "faculty['new']({},{},{},{},{},{},{})".format(self['get']('firstName'), self['get']('lastName'),
                                                             self['get']('birthDate')['get']('__repr__')(), self['get']('Id'),
                                                             self['get']('Teaching'), self['get']('Salary'),
                                                             self['get']('seniority_faculty'))

    def __str__(self):
        string=Person['get']('__str__')(self)+"Teaching: " + str(self['get']('Teaching'))+'\n'+"Salary: " + str(self['get']('Salary'))+'\n'+"seniority faculty: " + str(self['get']('seniority_faculty'))
        return string

    def getTeaching(self):
        return self['get']('Teaching')
    def getSalary(self):
        return self['get']('Salary')
    def getSeniority(self):
        return self['get']('seniority_faculty')

    def setSeniority(self, Seniority):
        if Seniority.isnumeric() and int(Seniority) > 0:
            self['set']('seniority_faculty',int(Seniority))
    def setSalary(self, Salary):
        if Salary.isnumeric() and float(Salary) > 0:
            self['set']('Salary',float(Salary))
    def setTeaching(self, Teaching):
        self['set']('Teaching',Teaching)


    def getId(self):
        return self['get']('Id')
    def getBirthDate(self):
        return self['get']('birthDate')
    def getFirstName(self):
        return self['get']('firstName')
    def getLastName(self):
        return self['get']('lastName')
    def setId(self, Id):
        self['set']('Id',Id)
    def setBirthDate(self, BirthDate):
        self['set']('BirthDate',BirthDate)
    def setFirstName(self, firstName):
        self['set']('firstName',firstName)
    def setLastName(self, lastName):
        self['set']('lastName',lastName)



    return make_class(locals(),Person)
faculty=make_Faculty_class()
new_faculty=faculty['new']("shaked","hamo", Date['new']('28','5','2016'),"318231750","Teaching","54","764")
print(new_faculty['get']('__str__')())
print(new_faculty['get']('__repr__')())

def make_TA_class():
    def __init__(self,firstName, lastName, birthDate, Id,Learning,Avg,Teaching, Salary, seniority_student,seniority_faculty):
        student['get']('__init__')(self,firstName, lastName, birthDate, Id,Learning,Avg,seniority_student)
        faculty['get']('__init__')(self, firstName, lastName, birthDate, Id, Teaching, Salary, seniority_faculty)

    def __repr__(self):
        return "TA['new']({},{},{},{},{},{},{},{},{},{})".format(self['get']('firstName'), self['get']('lastName'),
                                                             self['get']('birthDate')['get']('__repr__')(), self['get']('Id'),
                                                             self['get']('Learning'), self['get']('Avg'),
                                                             self['get']('Teaching'),self['get']('Salary'),self['get']('seniority_student'),self['get']('seniority_faculty'))
    def changebyfather(s):
        newlist=[]
        [newlist.append(x) for x in s if x not in newlist]
        return newlist
    def __str__(self):
        string_TA=student['get']('__str__')(self)+'\n'+faculty['get']('__str__')(self)
        return '\n'.join(changebyfather(string_TA.split('\n')))

    return make_class(locals(),student,faculty)
TA=make_TA_class()
obj_TA=TA['new']('einav', 'bitton', Date['new']('28','5','2016'), '8','Software Engineering', '5000', 'fsf','3888','95', ' 3324')
print(obj_TA['get']('__str__')())
print(obj_TA['get']('__repr__')())
###########################################################################################################ex2###################
class Rational(object):
    def __init__(self, numer, denom):
        g = gcd(numer, denom)
        self.numer = numer // g
        self.denom = denom // g

    def __repr__(self):
        return 'Rational({0}, {1})'.format(self.numer, self.denom)

class Rlist(object):
    """A recursive list consisting of a first element and the rest."""
    class EmptyList(object):
        def __len__(self):
            return 0

    empty = EmptyList()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __repr__(self):
        args = repr(self.first)
        if self.rest is not Rlist.empty:
            args += ', {0}'.format(repr(self.rest))
        return 'Rlist({0})'.format(args)

    def __len__(self):
        return 1 + len(self.rest)

    def __getitem__(self, i):
        if i == 0:
            return self.first
        return self.rest[i - 1]



def extendRlist(rlist, p):
    if rlist is Rlist.empty:
        return p
    return Rlist(rlist.first, extendRlist(rlist.rest, p))
def Add_Rational_To_Rlist(rlist,rational):
    return extendRlist(rlist,Rlist(rational))
def Add_Rlist_To_Rlist(rlist1,rlist2):
    return extendRlist(rlist1,rlist2)
def Add_Rational_To_Rational(rational1,rational2):
    return ((rational1.numer/rational1.denom)+(rational2.numer/rational2.denom))
def Add_Int_To_Int(int1,int2):
    return (int1+int2)
def Add_Rational_To_Int(rational,int):
    return Rational((rational.numer+int*rational.denom),(rational.denom))
def Mul_Int_And_Rlist(int,rlist):
    if int==1:
        return rlist
    if int==0:
        return None
    new = extendRlist(rlist, rlist)
    for i in range(2,int):
        new=extendRlist(new,rlist)
    return new
def Mul_Rational_And_Rational(rational1,rational2):
    return ((rational1.numer*rational2.numer)/(rational1.denom*rational2.denom))
def Mul_Int_And_Int(int1,int2):
    return (int1*int2)
def Mul_Rational_And_Int(rational,int):
    return Rational((rational.numer*int),rational.denom)

apply_dict={('mul',('Rational','Int')):Mul_Rational_And_Int,("mul",('Int','Int')):Mul_Int_And_Int,("mul",('Rational','Rational')):Mul_Rational_And_Rational,
("mul",('Int','Rlist')):Mul_Int_And_Rlist,("add",('Rational','Int')):Add_Rational_To_Int,("add",('Int','Int')):Add_Int_To_Int,
("add",('Rational','Rational')):Add_Rational_To_Rational,("add",('Rlist','Rlist')):Add_Rlist_To_Rlist,
('add',('Rlist','Rational')):Add_Rational_To_Rlist}
def type_Rational(tmp):
    if type(tmp)==Rational:
        return "Rational"
def type_Int(tmp):
    if type(tmp)==int:
        return "Int"
def type_Rlist(tmp):
    if type(tmp)==Rlist:
        return "Rlist"
def apply(argument1,argument2,operator):
    if operator=="add" or operator=="+":
        op="add"
    elif operator=="mul" or operator=="*":
        op="mul"
    else:
        print("wrong operator")
        return
    a1=type_Int(argument1)
    if a1 is None:
        a1=type_Rational(argument1)
        if a1 is None:
            a1=type_Rlist(argument1)
            if a1==None:
                print("wrong input")
                return
    a2=type_Int(argument2)
    if a2 is None:
        a2=type_Rational(argument2)
        if a2 is None:
            a2=type_Rlist(argument2)
            if a2==None:
                print("wrong input")
                return

    if (op,(a1,a2)) in apply_dict.keys():
        return apply_dict.get((op,(a1,a2)))(argument1,argument2)
    if (op,(a2,a1)) in apply_dict.keys():
        return apply_dict.get((op,(a2,a1)))(argument2,argument1)
    print("no combination")
    return




x=Rational(1,8)
c=Rational(7,9)
y=Rlist(3,Rlist(6))
z=Rlist(4)
print(apply(x,y,"add"))
print(apply(y,z,"+"))
print(apply(x,c,"add"))
print(apply(5,3,"+"))
print(apply(5,x,"add"))
print(apply(5,y,"*"))
print(apply(c,x,'*'))
print(apply(6,2,"mul"))
print(apply(2,x,"mul"))

