import json
import random
#this allows the user to input the type of question they want to study
user_input= input('Welcome to SAT prep. What would you like to study?'
                  '\n'
                  '\nPlease select a number to begin!'
                  '\n'
                  '\n1- For Math'
                  '\n2- For Reading'
                  '\n3- For Both?\t')
print()
print('***Must remember to answer in a capital letter choice.***'
                  '\nType “quit” in lowercase to exit test and view score.'
                  '\nGood luck!')
print()
if user_input =='1':
    test_type=['math']
elif user_input=='2':
    test_type=['reading']
elif user_input=='3':
    test_type=['math','reading']
else:
    user_input= input('Invalid Entry.Enter 1 for math, 2 for reading, or 3 for both? ')#
# makes the question varible and correct answers varible of question numbers to 0
total_questions=0
total_correct=0

totalScore=0

with open ("SATprep.txt",encoding='utf16') as handle: #opens the json file that we made
    contents=json.load(handle) #this looks at all the questions in the files we need
    random.shuffle(contents)#outputs the questions randomly to the user
    for dic in contents:
        if user_input=='quit':#gives the user the option to enter "quit" anytime which will stop the interactive portion
            break
        elif (dic['type']) not in test_type: #if the user inputs the type of question then the loop for the questions will continue
            continue
        else:
            print(dic['question'])#outputs the question key used in the json file
            print(dic['choices'])##outputs the answer choices key used in the json file
            user_answer=input('Your Answer: ')
            if user_answer== (dic['answer']):#after the user enters in their answer choices it would loop through all the correct answers and questions keys in the file
                total_correct +=1
                total_questions +=1
                print('Correct! \n')
            elif user_answer== 'quit':
                break
            else:
                total_questions +=1
                print()
                print('Incorrect.\n')
            if total_questions > 0: #after each question answered, it would loop through the amount of correct answer over the amount of question they answered
                grade = ((total_correct / total_questions) * 100)#percentage of correct answers
                print()
                print("You got %d out of %d correct, which means you got %.2f percent." % (total_correct, total_questions, grade))#gives the score precentage based on how many questions they have answered so far
            else:
                total_questions = 0 # when user input is incorrect
                print()
                print("You got 0/0 correct.")

if total_questions==0:
    totalScoreS=str(totalScore)
    print()
    print('You have completed this session. You have scored a ' +totalScoreS + '%') #gives the total score after user has finished
    print('Explore https://collegereadiness.collegeboard.org/sample-questions for practice and tutorials')#provides them with useful resources to study from after they finish

else:
    totalScore=(total_correct/total_questions*100)
    totalScoreS=str(totalScore)
    print('You have completed this session. You have scored a ' +totalScoreS + '%')
    if totalScore <=70:
        if user_input==1:
            print('https://collegereadiness.collegeboard.org/sample-questions/math for practice and tutorials')
        elif user_input==2:
            print('https://collegereadiness.collegeboard.org/sample-questions/reading for practice and tutorials')
        elif user_input==3:
            print('Explore https://collegereadiness.collegeboard.org/sample-questions for practice and tutorials')
        else:
            print('Explore https://collegereadiness.collegeboard.org/sample-questions for practice and tutorials')
