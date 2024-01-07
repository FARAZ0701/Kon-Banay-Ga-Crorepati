_questions_ = [
    ["What is the capital of France?", "1: Berlin", "2: Madrid", "3: Paris", "4: Rome", 3],
    ["Which planet is known as the Red Planet?", "1: Venus", "2: Mars", "3: Jupiter", "4: Saturn", 2],
    ["Who wrote 'Romeo and Juliet'?", "1: Charles Dickens", "2: William Shakespeare", "3: Jane Austen", "4: Mark Twain", 2],
    ["What is the largest mammal on Earth?", "1: Elephant", "2: Blue Whale", "3: Giraffe", "4: Hippopotamus", 2],
    ["What is the chemical symbol for gold?", "1: Au", "2: Ag", "3: Fe", "4: Cu", 1],
    ["What is the capital of Japan?", "1: Beijing", "2: Tokyo", "3: Seoul", "4: Bangkok", 2],
    ["Which programming language is often used for web development?", "1: Java", "2: Python", "3: HTML", "4: JavaScript", 4],
    ["Who is the author of 'To Kill a Mockingbird'?", "1: J.K. Rowling", "2: Ernest Hemingway", "3: Harper Lee", "4: F. Scott Fitzgerald", 3],
    ["What is the largest ocean on Earth?", "1: Indian Ocean", "2: Atlantic Ocean", "3: Southern Ocean", "4: Pacific Ocean", 4],
    ["In which year did the first moon landing occur?", "1: 1969", "2: 1975", "3: 1981", "4: 1992", 1],
    ["What is the capital of Brazil?", "1: Buenos Aires", "2: Rio de Janeiro", "3: Brasília", "4: São Paulo", 3],
    ["Who painted the Mona Lisa?", "1: Vincent van Gogh", "2: Pablo Picasso", "3: Leonardo da Vinci", "4: Michelangelo", 3],
    ["What is the chemical symbol for water?", "1: H2O", "2: CO2", "3: O2", "4: NaCl", 1],
    ["Which country is known as the 'Land of the Rising Sun'?", "1: China", "2: Japan", "3: South Korea", "4: Vietnam", 2],
    ["Who wrote 'The Great Gatsby'?", "1: Charles Dickens", "2: F. Scott Fitzgerald", "3: Jane Austen", "4: Mark Twain", 2],
]
Money = 0
Trys = 0
levelsOfMoney = [1000,2000,6000,12000,22000,50000,100000,150000,2000000,250000000,2500000000,2500000000000,3000000000000,3000000000000,40000000000000000,50000000000000000000000]
for i in range(len(_questions_)):
    question = _questions_[i]
    
    if Trys <= 4:
        print(i,"   ",question[0])
        print(question[1],"   ",question[2])
        print(question[3],"   ",question[4])
        try:
            reply = int(input("Enter number of right answer : "))
        except:
            print("The number you have entered in not a integer")
            continue
        if reply == question[5]:
            Money = levelsOfMoney[i]
            print("Right answer  ",Money)
        else:
            Trys += 1
            print(f"wrong answer{question[5]}  ,  Money = {Money} Rs")
    else:
        print("TOO many try, You are ILLITERATE!!!!")

        
if Trys == 0:
    print("You are amazing, all answers are right and you have got ",Money," Rs")
else:
    print("you won in ",Trys," trys and you have got ",Money," Rs")

            