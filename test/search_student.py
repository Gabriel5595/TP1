from tabulate import tabulate

def search_student(database):
    while True:
            print("Would you like to search by student ID or Full Name?")
            option = int(input("1) student ID.\n2) Full Name.\n"))
            
            if option == 1:
                student_id = int(input("\nPlease, enter the student's ID: "))
                student_id -= 1
                
                if database[student_id] == None:
                    print("student not found.\n")
                    return None
                else:
                    print(tabulate([database[student_id]], headers="keys", tablefmt="grid"))
                    return database[student_id]
                    # print(f"The selected student is {database[student_id]}")
                    # new_grade_1 = round(float(input("Please enter the student's new first grade: ")), 2)
                    # new_grade_2 = round(float(input("Please enter the student's new second grade: ")), 2)
                    # new_grade_3 = round(float(input("Please enter the student's new third grade: ")), 2)
                    # new_average = round(float((new_grade_1 + new_grade_2 + new_grade_3) / 3))
                    
                    # database[student_id]["Nota 1"] = new_grade_1
                    # database[student_id]["Nota 2"] = new_grade_2
                    # database[student_id]["Nota 3"] = new_grade_3
                    # database[student_id]["Média"] = new_average
                    
                    # print("student's new info:")
                    # print(tabulate([database[student_id]], headers="keys", tablefmt="grid"))
                    
                    # return database
            
            elif option == 2:
                student_name = input("Please, enter the student's full name: ")
                
                for data in database:
                    if data["Nome Completo"] == student_name:
                        print(tabulate([data], headers="keys", tablefmt="grid"))
                        return data
                        # print(f"The selected student is {data}")
                        
                        # new_grade_1 = round(float(input("Please enter the student's new first grade: ")), 2)
                        # new_grade_2 = round(float(input("Please enter the student's new second grade: ")), 2)
                        # new_grade_3 = round(float(input("Please enter the student's new third grade: ")), 2)
                        # new_average = round(float((new_grade_1 + new_grade_2 + new_grade_3) / 3))
                        
                        # data["Nota 1"] = new_grade_1
                        # data["Nota 2"] = new_grade_2
                        # data["Nota 3"] = new_grade_3
                        # data["Média"] = new_average
                        
                        # print("student's new info:")
                        # print(tabulate([data], headers="keys", tablefmt="grid"))
                        
                        # return database
                
                print("student not found.\n")
                return None
            
            else:
                print("The entered option is not valid.\n")

def main():
    database = [
    {"Nome Completo": "João da Silva", "Nota 1": 7.25, "Nota 2": 8.50, "Nota 3": 9.75, "Média": 8.50},
    {"Nome Completo": "Maria Oliveira", "Nota 1": 6.00, "Nota 2": 5.25, "Nota 3": 7.75, "Média": 6.33},
    {"Nome Completo": "Pedro Santos", "Nota 1": 9.00, "Nota 2": 8.25, "Nota 3": 10.00, "Média": 9.08},
    {"Nome Completo": "Ana Pereira", "Nota 1": 8.50, "Nota 2": 7.75, "Nota 3": 6.25, "Média": 7.50},
    {"Nome Completo": "Carlos Costa", "Nota 1": 5.75, "Nota 2": 6.25, "Nota 3": 7.50, "Média": 6.50},
    {"Nome Completo": "Mariana Rodrigues", "Nota 1": 9.25, "Nota 2": 9.50, "Nota 3": 8.75, "Média": 9.17},
    {"Nome Completo": "José Martins", "Nota 1": 7.25, "Nota 2": 8.00, "Nota 3": 7.00, "Média": 7.42},
    {"Nome Completo": "Sandra Ferreira", "Nota 1": 6.00, "Nota 2": 5.25, "Nota 3": 6.00, "Média": 5.75},
    {"Nome Completo": "Rui Sousa", "Nota 1": 8.25, "Nota 2": 7.75, "Nota 3": 9.00, "Média": 8.00},
    {"Nome Completo": "Carla Almeida", "Nota 1": 7.00, "Nota 2": 6.25, "Nota 3": 5.00, "Média": 6.08},
    {"Nome Completo": "Manuel Lima", "Nota 1": 9.50, "Nota 2": 8.25, "Nota 3": 9.25, "Média": 8.83},
    {"Nome Completo": "Patrícia Carvalho", "Nota 1": 6.25, "Nota 2": 7.00, "Nota 3": 8.00, "Média": 7.08},
    {"Nome Completo": "Jorge Pereira", "Nota 1": 7.00, "Nota 2": 6.25, "Nota 3": 5.00, "Média": 6.08},
    {"Nome Completo": "Catarina Silva", "Nota 1": 8.25, "Nota 2": 9.25, "Nota 3": 8.50, "Média": 8.67},
    {"Nome Completo": "Paulo Santos", "Nota 1": 5.75, "Nota 2": 6.25, "Nota 3": 7.50, "Média": 6.50},
    {"Nome Completo": "Andreia Costa", "Nota 1": 9.25, "Nota 2": 8.00, "Nota 3": 7.00, "Média": 8.08},
    {"Nome Completo": "Miguel Oliveira", "Nota 1": 7.25, "Nota 2": 8.00, "Nota 3": 9.25, "Média": 8.17},
    {"Nome Completo": "Filipa Rodrigues", "Nota 1": 6.25, "Nota 2": 7.00, "Nota 3": 8.00, "Média": 7.08},
    {"Nome Completo": "Ricardo Martins", "Nota 1": 8.00, "Nota 2": 9.00, "Nota 3": 8.50, "Média": 8.50},
    {"Nome Completo": "Inês Ferreira", "Nota 1": 5.75, "Nota 2": 6.25, "Nota 3": 7.50, "Média": 6.50}
]
    
    database = search_student(database)
    

main()