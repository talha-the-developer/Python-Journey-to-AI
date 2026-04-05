names = ["Saeed", "Talha", "Tabish", "Farhan", "Adil", "Zain"]
marks = [85, 92, 45, 78, 60, 30]

def grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"

def result(grade):
    if grade == "F":
        return "Fail"
    else:
        return "Pass"
    

for n, m in zip(names, marks):
    grd = grade(m)
    st = result(grd)
    print(f"STUDENT : {n} | MARKS : {m} | GRADE : {grd} | STATUS : {st}")
    