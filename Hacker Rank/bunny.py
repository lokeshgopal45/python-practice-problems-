class teacher:
    def __init__(self,qualification,salury):
        self.qualification=qualification
        self.salury=salury

t=teacher("phd",85000)
print(t.salury)
print(t.qualification)

t=teacher("m-tech",75000)
print(t.salury)
print(t.qualification)

t=teacher("b-tech",60000)
print(t.salury)
print(t.qualification)

t=teacher("diploma",50000)
print(t.salury)
print(t.qualification)