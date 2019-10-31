import requests

def insert_students():
    data = [
        {
            "firstName": "Xiao",
            "lastName": "Ma",
            "userName": "MAXI0009",
            "password": "MAXI0008!",
            "mark": 0
        },
        {
            "firstName": "Xiaoo",
            "lastName": "Maa",
            "userName": "MAXI0007",
            "password": "MAXI0007!",
            "mark": 0
        },
        {
            "firstName": "Eric",
            "lastName": "Ma",
            "userName": "MAXI0006",
            "password": "MAXI0006!",
            "mark": 0
        },
        {
            "firstName": "Ericc",
            "lastName": "Maa",
            "userName": "MAXI0005",
            "password": "MAXI0005!",
            "mark": 0
        },{
            "firstName": "Eric",
            "lastName": "Ma",
            "userName": "MAXI0004",
            "password": "MAXI0004!",
            "mark": 0
        }
    ]
    for datum in data:
        # depends on your server
        r = requests.post("http://localhost:8082/api/student", json=datum)
        print("##############")
        print(r.json())
        print("##############")

def insert_teachers():
    data = [
        {
            "firstName": "Eric",
            "lastName": "Ma",
            "userName": "MAXIAO",
            "password": "MAXIAO123456!",
            "title": "Professor"
        },
    ]
    for datum in data:
        # depends on your server
        r = requests.post("http://localhost:8082/api/teacher", json=datum)
        print("##############")
        print(r.json())
        print("##############")

def insert_questions():
    data = [
       {
            "description" : "What are the types of requirements?",
            "character" : "Product Manager",
            "world" : "Requirement Gathering and Analysis",
            "section" : "Requirement Engineering",
            "level" : "EASY",
            "difficulty" : "EASY",
            "choiceA" : "Availability",
            "choiceB" : "Reliability",
            "choiceC" : "Usability",
            "choiceD" : "All of the mentioned",
            "correctChoice" : "D",
            "award" : 15,
            "bonus" : False
        },
        {
            "description" : "What happens during the requirements gathering and analysis phase of the software development lifecycle (SDLC)?",
            "character" : "Product Manager",
            "world" : "Requirement Gathering and Analysis",
            "section" : "Requirement Engineering",
            "level" : "EASY",
            "difficulty" : "EASY",
            "choiceA" : "The customer pays for the scope of work",
            "choiceB" : "The project team codes each requirement",
            "choiceC" : "The project manager hires the project team",
            "choiceD" : "The customer gives the expectations of the project",
            "correctChoice" : "D",
            "award" : 15,
            "bonus" : False
        },
        {
            "description" : "What Is SRS In Project?",
            "character" : "Product Manager",
            "world" : "Requirement Gathering and Analysis",
            "section" : "Requirement Engineering",
            "level" : "EASY",
            "difficulty" : "EASY",
            "choiceA" : "A document that captures complete description about how the system is expected to perform.",
            "choiceB" : "A document that is not required in SDLC",
            "choiceC" : "A document that captures the progress of the projects",
            "choiceD" : "An introduction to the project",
            "correctChoice" : "A",
            "award" : 15,
            "bonus" : False
        },
        {
            "description" : "How Many Types Of Software Requirements Are There?",
            "character" : "Product Manager",
            "world" : "Requirement Gathering and Analysis",
            "section" : "Requirement Engineering",
            "level" : "EASY",
            "difficulty" : "EASY",
            "choiceA" : "1",
            "choiceB" : "2",
            "choiceC" : "3",
            "choiceD" : "4",
            "correctChoice" : "B",
            "award" : 15,
            "bonus" : False
        },
        {
            "description" : "Which one of the following is not a step of requirement engineering?",
            "character" : "Product Manager",
            "world" : "Requirement Gathering and Analysis",
            "section" : "Requirement Engineering",
            "level" : "EASY",
            "difficulty" : "EASY",
            "choiceA" : "Elicitation",
            "choiceB" : "Design",
            "choiceC" : "Analysis",
            "choiceD" : "Documentation",
            "correctChoice" : "B",
            "award" : 15,
            "bonus" : False
        },
        {
            "description" : "The computer-based system can have a profound effect on the design that is chosen and also the implementation approach will be applied.",
            "character" : "Product Manager",
            "world" : "Requirement Gathering and Analysis",
            "section" : "Requirement Engineering",
            "level" : "EASY",
            "difficulty" : "EASY",
            "choiceA" : "Behavioral elements",
            "choiceB" : "Flow-oriented elements",
            "choiceC" : "Scenario-based elements",
            "choiceD" : "Class-based elements",
            "correctChoice" : "A",
            "award" : 15,
            "bonus" : True
        },

        {
            "description" : "What Is The Requirement Gathering?",
            "character" : "Product Manager",
            "world" : "Requirement Gathering and Analysis",
            "section" : "Requirement Engineering",
            "level" : "MEDIUM",
            "difficulty" : "MEDIUM",
            "choiceA" : "Gather the hardware resources that are needed project",
            "choiceB" : "Gather information on coding the project",
            "choiceC" : "The practise of collecting the requirements of a system from users, customers and other stakeholders.",
            "choiceD" : "All of the above",
            "correctChoice" : "C",
            "award" : 15,
            "bonus" : False
        },
        {
            "description" : "What are the benefits of a good SRS?",
            "character" : "Product Manager",
            "world" : "Requirement Gathering and Analysis",
            "section" : "Requirement Engineering",
            "level" : "MEDIUM",
            "difficulty" : "MEDIUM",
            "choiceA" : "Enables costing and pricing of the project",
            "choiceB" : "Management of customer expectations",
            "choiceC" : "Input for detailed design",
            "choiceD" : "All of the above",
            "correctChoice" : "D",
            "award" : 15,
            "bonus" : False
        },
        {
            "description" : "Which of the following is NOT a Functional Requirements",
            "character" : "Product Manager",
            "world" : "Requirement Gathering and Analysis",
            "section" : "Requirement Engineering",
            "level" : "MEDIUM",
            "difficulty" : "MEDIUM",
            "choiceA" : "Business Rules",
            "choiceB" : "Performance",
            "choiceC" : "Historical Data",
            "choiceD" : "Certification Requirements",
            "correctChoice" : "B",
            "award" : 15,
            "bonus" : False
        },
        {
            "description" : "Which of the following is NOT a Non-Functional Requirements",
            "character" : "Product Manager",
            "world" : "Requirement Gathering and Analysis",
            "section" : "Requirement Engineering",
            "level" : "MEDIUM",
            "difficulty" : "MEDIUM",
            "choiceA" : "Security",
            "choiceB" : "Performance",
            "choiceC" : "Cost",
            "choiceD" : "Authentication",
            "correctChoice" : "D",
            "award" : 15,
            "bonus" : False
        },
        {
            "description" : "Which of the following is not a diagram studied in Requirement Analysis?",
            "character" : "Product Manager",
            "world" : "Requirement Gathering and Analysis",
            "section" : "Requirement Engineering",
            "level" : "MEDIUM",
            "difficulty" : "MEDIUM",
            "choiceA" : "Use Cases",
            "choiceB" : "Entity Relationship Diagram",
            "choiceC" : "State Transition Diagram",
            "choiceD" : "Activity Diagram",
            "correctChoice" : "D",
            "award" : 15,
            "bonus" : False
        },
        {
            "description" : "Which sentences about Requirement Analysis is NOT TRUE?",
            "character" : "Product Manager",
            "world" : "Requirement Gathering and Analysis",
            "section" : "Requirement Engineering",
            "level" : "MEDIUM",
            "difficulty" : "MEDIUM",
            "choiceA" : "It is the process of determining user expectations for a new or modified product.",
            "choiceB" : "Requirements identified can be unquantifiable, relevant and detailed",
            "choiceC" : "In software engineering, such requirements are often called functional specifications",
            "choiceD" : "Known also as Requirements Engineering",
            "correctChoice" : "C",
            "award" : 15,
            "bonus" : True
        },
        {
            "description" : "____ and _____ are the two issues of Requirement Analysis",
            "character" : "Product Manager",
            "world" : "Requirement Gathering and Analysis",
            "section" : "Requirement Engineering",
            "level" : "HARD",
            "difficulty" : "HARD",
            "choiceA" : "Performance, Design",
            "choiceB" : "Stakeholder, Developer",
            "choiceC" : "Functional, Non-Functional",
            "choiceD" : "None of the mentioned",
            "correctChoice" : "B",
            "award" : 15,
            "bonus" : False
        },
        {
            "description" : "Coad and Yourdon suggested _______ selection characteristics that should be used as an analyst considers each potential object for inclusion in the requirement analysis",
            "character" : "Product Manager",
            "world" : "Requirement Gathering and Analysis",
            "section" : "Requirement Engineering",
            "level" : "HARD",
            "difficulty" : "HARD",
            "choiceA" : "Three",
            "choiceB" : "Four",
            "choiceC" : "Five",
            "choiceD" : "Six",
            "correctChoice" : "D",
            "award" : 15,
            "bonus" : False
        },
        {
            "description" : "The requirements that result from requirements analysis are typically expressed from one of three perspectives or views. What is that perspective or view?",
            "character" : "Product Manager",
            "world" : "Requirement Gathering and Analysis",
            "section" : "Requirement Engineering",
            "level" : "HARD",
            "difficulty" : "HARD",
            "choiceA" : "Developer",
            "choiceB" : "User",
            "choiceC" : "Non-Functional",
            "choiceD" : "Physical",
            "correctChoice" : "D",
            "award" : 15,
            "bonus" : False
        },
        {
            "description" : "In Software validation which of the following conditions: \n i) A \n ii) B \n iii) C \n iv) D",
            "character" : "Product Manager",
            "world" : "Requirement Gathering and Analysis",
            "section" : "Requirement Engineering",
            "level" : "HARD",
            "difficulty" : "HARD",
            "choiceA" : "i & iv",
            "choiceB" : "ii & iii",
            "choiceC" : "i, iii & iv",
            "choiceD" : "All of the above",
            "correctChoice" : "D",
            "award" : 15,
            "bonus" : False
        },
        {
            "description" : "What Are The Features Of SRS",
            "character" : "Product Manager",
            "world" : "Requirement Gathering and Analysis",
            "section" : "Requirement Engineering",
            "level" : "HARD",
            "difficulty" : "HARD",
            "choiceA" : "User Requirements are expressed in natural language",
            "choiceB" : "Design description should be written in Pseudocode.",
            "choiceC" : "Format of Forms and GUI screen prints.",
            "choiceD" : "All of the above",
            "correctChoice" : "D",
            "award" : 15,
            "bonus" : False
        },
        {
            "description" : "What Is A Static Analysis Tool?",
            "character" : "Product Manager",
            "world" : "Requirement Gathering and Analysis",
            "section" : "Requirement Engineering",
            "level" : "HARD",
            "difficulty" : "HARD",
            "choiceA" : "A tool is used to analyse the software while running the program.",
            "choiceB" : "It is the analysis of computer software that is performed without actually executing programs",
            "choiceC" : "It is the to execute the software and test for error",
            "choiceD" : "All of the above",
            "correctChoice" : "C",
            "award" : 15,
            "bonus" : True
        }
    ]

    # Need to put the correct 'Authroization' here to do the authentication
    headers = {'Authorization': 'TJhjh9+Ww8bmtS21WgaelDmEWSN7ckjDj3VUBAZ3Vp54gq96odaF7fki7M0uRkqZllmPQjsHVgdILXAYlmaXMV7lBj2kcztrhTAOIYORsT2EroYWEi9UxAOtKH6WLOJa'}

    for datum in data:
        # depends on your server
        r = requests.post("http://localhost:8082/api/question", json=datum, headers=headers)
        print("##############")
        print(r.json())
        print("##############")

# insert_students()
# insert_teachers()
# insert_questions()
