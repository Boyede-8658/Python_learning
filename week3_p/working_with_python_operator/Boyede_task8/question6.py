age = int(input('Enter your age: '))
utme_score = int(input('Enter your utme score: '))
olevel = input('Do you have 5 credits in olevel: ')
postutme = input('Did you paticipate in post utme?(True or False) ')
dept_cut_off = float(input('Enter departmental cut off here: '))

final_admission = (age >= 17) and (utme_score >= 199) and (olevel.lower() == 'true') and (postutme.lower() == 'true') and (dept_cut_off >= 200)
print(f'Admitted: {final_admission}')