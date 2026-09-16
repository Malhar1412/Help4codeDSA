class College:
    college_name = "Sandip University"

obj1 = College()
obj2 = College()
obj3 = College()
print(obj1.college_name)
print(obj2.college_name)
print(obj3.college_name)
College.college_name = "Modern College"    
print(obj1.college_name)
print(obj2.college_name)
print(obj3.college_name)