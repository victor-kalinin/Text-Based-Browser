# write your code here
with open('salary.txt', 'r') as m_salary, open('salary_year.txt', 'w') as y_salary:
    for line in m_salary:
        y_salary.write(str(int(line.strip()) * 12) + '\n')
