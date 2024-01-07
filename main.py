
_planet_questions_ = [
    ["Which planet is known as the 'Red Planet'?", "1: Venus", "2: Mars", "3: Jupiter", "4: Saturn", 2],
    ["Which planet is closest to the Sun?", "1: Earth", "2: Venus", "3: Mercury", "4: Mars", 3],
    ["Which planet is known for its prominent ring system?", "1: Jupiter", "2: Saturn", "3: Neptune", "4: Uranus", 2],
    ["Which planet is referred to as the 'Blue Planet'?", "1: Mars", "2: Earth", "3: Neptune", "4: Uranus", 2],
    ["What is the largest planet in our solar system?", "1: Earth", "2: Jupiter", "3: Saturn", "4: Neptune", 2],
    ["Which planet is known for its extreme temperatures and thick atmosphere?", "1: Venus", "2: Mars", "3: Jupiter", "4: Saturn", 1],
    ["Which planet is often called the 'Evening Star' or 'Morning Star'?", "1: Mercury", "2: Venus", "3: Mars", "4: Jupiter", 2],
    ["Which dwarf planet was formerly considered the ninth planet in our solar system?", "1: Pluto", "2: Eris", "3: Haumea", "4: Ceres", 1],
]
_movie_questions_ = [
    ["Which movie won the Academy Award for Best Picture in 2021?", "\n1: Nomadland", "\n2: The Trial of the Chicago 7", "\n3: Minari", "\n4: Promising Young Woman", 1],
    ["Who won the Academy Award for Best Actor in a Leading Role in 2021?", "\n1: Anthony Hopkins", "\n2: Chadwick Boseman", "\n3: Riz Ahmed", "\n4: Gary Oldman", 1],
    ["In which film did Heath Ledger posthumously win an Oscar for Best Supporting Actor?", "\n1: The Dark Knight", "\n2: Brokeback Mountain", "\n3: 10 Things I Hate About You", "\n4: A Knight's Tale", 1],
    ["Which animated movie features a character named Simba?", "\n1: Shrek", "\n2: The Lion King", "\n3: Toy Story", "\n4: Finding Nemo", 2],
    ["Who directed the 1994 film 'Pulp Fiction'?", "\n1: Quentin Tarantino", "\n2: Martin Scorsese", "\n3: Steven Spielberg", "\n4: Christopher Nolan", 1],
    ["Which movie features a character named Jack Dawson and a famous line 'I'm king of the world!'?", "\n1: Titanic", "\n2: Inception", "\n3: The Revenant", "\n4: The Departed", 1],
    ["Who played the lead role in the 1990 film 'Pretty Woman'?", "\n1: Julia Roberts", "\n2: Sandra Bullock", "\n3: Nicole Kidman", "\n4: Meg Ryan", 1],
    ["Which movie is known for the quote 'May the Force be with you'?", "\n1: The Matrix", "\n2: Star Wars", "\n3: Blade Runner", "\n4: E.T. the Extra-Terrestrial", 2],
]
_python_programming_questions_ = [
    ["What is the difference between 'deep copy' and 'shallow copy' in Python?", "1: Deep copy creates a new object with a new reference, while shallow copy creates a new object with the same reference.", "2: Deep copy creates a new object with the same reference, while shallow copy creates a new object with a new reference.", "3: Deep copy is used for immutable objects, while shallow copy is used for mutable objects.", "4: Shallow copy is used for immutable objects, while deep copy is used for mutable objects.", 1],
    ["Explain the Global Interpreter Lock (GIL) in Python.", "1: The GIL is a mechanism to synchronize access to Python objects, preventing multiple threads from executing Python bytecode at once.", "2: The GIL ensures that only one process can execute Python code at a time, preventing race conditions.", "3: The GIL is used to lock the interpreter during garbage collection to prevent memory leaks.", "4: The GIL is a feature of Python's memory manager to optimize memory usage.", 1],
    ["What is the use of the 'yield' keyword in Python?", "1: It is used to return a value from a function.", "2: It is used to create a generator function, allowing the function to retain its state between calls.", "3: It is used to raise an exception.", "4: It is used to declare a variable with a specific data type.", 2],
    ["Explain the concept of a decorator in Python.", "1: A decorator is a design pattern used to create a class instance.", "2: A decorator is a function that takes another function and extends or modifies the behavior of the latter function.", "3: A decorator is a special type of variable in Python.", "4: A decorator is a keyword used for error handling.", 2],
    ["What is the purpose of the 'lambda' function in Python?", "1: It is used to declare anonymous functions.", "2: It is used for exception handling.", "3: It is used for file input/output operations.", "4: It is used to define a class in a single line.", 1],
    ["How does the 'map' function work in Python?", "1: It applies a function to each item in a sequence (e.g., a list) and returns a new sequence of the results.", "2: It is used to create a mapping of keys to values.", "3: It is used to filter elements from a sequence based on a given condition.", "4: It is used to merge two dictionaries.", 1],
    ["What is the purpose of the 'super()' function in Python?", "1: It is used to generate random numbers.", "2: It is used to call a method from the parent class.", "3: It is used to calculate the square root of a number.", "4: It is used to convert a string to uppercase.", 2],
    ["Explain the concept of a generator in Python.", "1: A generator is a function that returns an iterator, allowing you to iterate over a potentially large sequence of data.", "2: A generator is a built-in module for handling dates and times.", "3: A generator is a data structure used for sorting elements.", "4: A generator is a special type of list in Python.", 1],
    ["What is the purpose of the 'with' statement in Python?", "1: It is used for creating aliases for module imports.", "2: It is used for opening and managing files, ensuring proper resource cleanup.", "3: It is used for defining a block of code that will be executed in case an error occurs.", "4: It is used for creating conditional statements.", 2],
]

_data_engineering_questions_ = [
    ["What is ETL?", "1: Extract, Transform, Load", "2: Extract, Transfer, Load", "3: Extract, Transmit, Load", "4: Extract, Translate, Load", 1],
    ["What is the purpose of a data warehouse?", "1: Real-time data processing", "2: Long-term storage and analysis of historical data", "3: Data streaming", "4: Transactional processing", 2],
    ["Which programming language is commonly used for writing Apache Spark applications?", "1: Java", "2: Python", "3: Scala", "4: Ruby", 3],
    ["What is Apache Kafka used for in data engineering?", "1: Data warehousing", "2: Stream processing and messaging", "3: Data cleaning", "4: Data visualization", 2],
    ["What does the acronym 'SQL' stand for?", "1: Simple Query Language", "2: Structured Question Language", "3: Standardized Query Language", "4: Sequential Query Language", 3],
    ["What is the purpose of a schema in a database?", "1: To represent a collection of tables", "2: To define the structure and organization of data", "3: To perform complex calculations", "4: To generate random data", 2],
    ["Which database model is based on a tree-like structure?", "1: Relational", "2: NoSQL", "3: Hierarchical", "4: Network", 3],
    ["What is the primary goal of data normalization?", "1: Minimize redundancy and dependency", "2: Maximize redundancy and dependency", "3: Speed up data retrieval", "4: Increase data duplication", 1],
    ["What is a primary key in a relational database?", "1: A key used for encryption", "2: A unique identifier for a record in a table", "3: A key for sorting data", "4: A key for foreign relations", 2],
    ["In data engineering, what does the term 'data pipeline' refer to?", "1: A series of tubes for transmitting data", "2: A sequence of data processing stages", "3: A single point of failure in data processing", "4: A storage unit for data", 2],
]

_random_questions_ = [
    ["Which element is represented by the chemical symbol 'Na'?", "1: Sodium", "2: Nickel", "3: Nitrogen", "4: Neon", 1],
    ["In which year did the Titanic sink?", "1: 1905", "2: 1912", "3: 1923", "4: 1931", 2],
    ["Who wrote the play 'Romeo and Juliet'?", "1: William Shakespeare", "2: Jane Austen", "3: Charles Dickens", "4: Mark Twain", 1],
    ["Which country is known as the Land of the Rising Sun?", "1: China", "2: Japan", "3: South Korea", "4: Vietnam", 2],
    ["What is the capital city of Australia?", "1: Sydney", "2: Melbourne", "3: Canberra", "4: Brisbane", 3],
    ["Who painted the Mona Lisa?", "1: Vincent van Gogh", "2: Leonardo da Vinci", "3: Pablo Picasso", "4: Michelangelo", 2],
    ["What is the largest ocean on Earth?", "1: Atlantic Ocean", "2: Indian Ocean", "3: Southern Ocean", "4: Pacific Ocean", 4],
    ["Who is the author of 'To Kill a Mockingbird'?", "1: J.K. Rowling", "2: Harper Lee", "3: George Orwell", "4: Ernest Hemingway", 2],
    ["Which planet is known as the 'Red Planet'?", "1: Venus", "2: Mars", "3: Jupiter", "4: Saturn", 2],
    ["What is the capital of Canada?", "1: Toronto", "2: Ottawa", "3: Vancouver", "4: Montreal", 2],
    ["Who was the first woman to win a Nobel Prize?", "1: Marie Curie", "2: Rosa Parks", "3: Amelia Earhart", "4: Mother Teresa", 1],
    ["Which musical instrument has black and white keys?", "1: Violin", "2: Guitar", "3: Piano", "4: Trumpet", 3],
    ["What is the currency of Brazil?", "1: Peso", "2: Real", "3: Rupee", "4: Euro", 2],
    ["In which year did the Berlin Wall fall?", "1: 1985", "2: 1989", "3: 1991", "4: 1995", 2],
    ["Who wrote 'The Great Gatsby'?", "1: F. Scott Fitzgerald", "2: Ernest Hemingway", "3: Jane Austen", "4: Charles Dickens", 1],
    ["What is the tallest mountain in the world?", "1: Mount Everest", "2: K2", "3: Mount McKinley", "4: Mount Kilimanjaro", 1],
    ["What is the largest species of big cat?", "1: Lion", "2: Tiger", "3: Cheetah", "4: Leopard", 2],
    ["Who is known as the 'Father of Physics'?", "1: Isaac Newton", "2: Albert Einstein", "3: Galileo Galilei", "4: Archimedes", 3],
    ["What is the capital city of South Africa?", "1: Johannesburg", "2: Cape Town", "3: Pretoria", "4: Durban", 3],
    ["Who painted 'Starry Night'?", "1: Claude Monet", "2: Vincent van Gogh", "3: Pablo Picasso", "4: Salvador Dalí", 2],
]

def KBC(_questions_):

    Money = 0
    Trys = 0
    levelsOfMoney = [1000,2000,6000,12000,22000,50000,100000,150000,2000000,250000000,2500000000,2500000000000,3000000000000,3000000000000,40000000000000000,50000000000000000000000,6000000006000000000000,70000000000000000000000000000]
    for i in range(len(_questions_)):
        question = _questions_[i]
        
        if Trys <= 2:
            print(i," : ",question[0])
            print("\n",question[1],"\n\n",question[2],"\n\n")
            print(question[3],"\n\n",question[4])
            try:
                reply = int(input("Enter number of right answer : "))
            except ValueError:
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


x = "Value has to be changed"

def InputTypeOfQuestion():
    typeOfQuestion = ["Which field do you belong to ","1 : Astronomy","2 : Movie" , "3 : Data Scientist" , "4 : Python Programming" , "5 : None of these"]
    print(typeOfQuestion[0])
    print(typeOfQuestion[1],"                     ",typeOfQuestion[2])
    print(typeOfQuestion[3],"   ",typeOfQuestion[4] , typeOfQuestion[5])
    try:
        reply = int(input("Enter your field in number"))

    except ValueError:
        print("Your input is not integer")
        InputTypeOfQuestion()
    if reply < 6:
        print(reply)
        x = reply
        if x == 1:
            KBC(_planet_questions_)
        elif x == 2:
            KBC(_movie_questions_) 
        elif x == 3:
            KBC(_data_engineering_questions_)
        elif x == 4:
            KBC(_python_programming_questions_)
        elif x == 5:
            KBC(_random_questions_)   
        else:
            print("Please give right input")
        
    else:
        print("Enter number from 1 to 5")
        InputTypeOfQuestion()

InputTypeOfQuestion()



    

