#Give input seperated by spaces like first_name last_name age class
info=[]
first_name=[]
last_name=[]
age=[]
stud1=input("Enter student full name,age,class: \n")
info.append(stud1)
stud2=input("Enter student full name,age,class: \n")
info.append(stud2)
stud3=input("Enter student full name,age,class: \n")
info.append(stud3)
stud4=input("Enter student full name,age,class: \n")
info.append(stud4)
stud5=input("Enter student full name,age,class: \n")
info.append(stud5)
no=len(info)
print('Total students : ')
print(no)
split_name=info[0].split()
first_name.append(split_name[0])
split_name=info[1].split()
first_name.append(split_name[0])
split_name=info[2].split()
first_name.append(split_name[0])
split_name=info[3].split()
first_name.append(split_name[0])
split_name=info[4].split()
first_name.append(split_name[0])
first_name.sort()
print(first_name)
split_name=info[0].split()
last_name1=split_name[1][::-1]
last_name.append(last_name1)
split_name=info[1].split()
last_name1=split_name[1][::-1]
last_name.append(last_name1)
split_name=info[2].split()
last_name1=split_name[1][::-1]
last_name.append(last_name1)
split_name=info[3].split()
last_name1=split_name[1][::-1]
last_name.append(last_name1)
split_name=info[4].split()
last_name1=split_name[1][::-1]
last_name.append(last_name1)
print(last_name)
cal_age=info[0].split()
age1=int(cal_age[2])
age.append(age1)
cal_age=info[1].split()
age2=int(cal_age[2])
age.append(age2)
cal_age=info[2].split()
age3=int(cal_age[2])
age.append(age3)
cal_age=info[3].split()
age4=int(cal_age[2])
age.append(age4)
cal_age=info[4].split()
age5=int(cal_age[2])
age.append(age5)
print('Sum of age of Total students')
print(age1+age2+age3+age4+age5)


