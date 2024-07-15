import json 
import re
from print_color.print_color import print
from datetime import datetime

p =int(input("Which set pratice .. : "))

start = datetime.now()

pratice = []
# Le pattern regex pour capturer les questions, réponses et explications
pattern = re.compile(
    r'(?P<question>\d+\. Question[\s\S]*?Answer:\s*(?P<answer>[\d,]+)\s*Explanation:\s*(?P<explanation>[\s\S]*?))\s*(?=(\d+\. Question|\Z))'
)

with open(f'training/pratice{p}.txt' , 'r') as pr : 
    matches = re.findall( pattern, pr.read())

    for  i , match in enumerate (matches):
        question = (match[0].strip()).split("Answer: ")[0]
        answer = match[1].strip()
        explanation = match[2].strip()

        pratice.append(
            {
                'question': question,
                'answer': [int(a) for a in re.split(r'[,.]', answer)],
                'explanation': explanation
            }
        )

with open(f"training/pratice{p}.json" , 'w') as js : 
    js.write(json.dumps(pratice,indent=4))
    

score = 0
missed = []
i= 0
for questions in pratice : 
    i+=1 
    if i <=25 : continue
    question = questions['question']
    answer = questions['answer']
    explanation = questions['explanation']

    print("\033[1;34mQuestion:")
    print(question) 

    while True : 
        try : 
            my_answer = input("Answers here .. : ")
            
            if my_answer == 'stop': 
                print("You have stoped the pratice" , color='red')
                print("time : " , start - datetime.now() )
                raise "Stopped"

            my_answer = my_answer.split("-")
            my_answer = [int(num.strip()) for num in my_answer]
            
        

            break
            
        except Exception as e :
            print(e , color="red")

    if sorted(answer) == sorted(my_answer) : 
        print("\n[Correct answer] ", color='green')
        score+=1
    else:
        miss = question.split(".")[0]
        missed.append(miss)
        print("\n[Wrong answer] " , miss, color='red')
        print(f"Correct answer : {answer}")
        print(f"Your answer : {my_answer}")
    print(f"Explanation : {explanation}\n\n")
    print(200*"=")

end = datetime.now()

print("Votre score est : ", score , " --- = %" , int((score/65 )*100) )
print(f"Vous avez raté : {len(missed)} questions")
print("You have do this in :" , (end - start) )


