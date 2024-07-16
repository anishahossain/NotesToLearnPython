from TriviaClass import Trivia

def trivia_ques():
    question_list = ['How many days are in a lunar year?', 'What is the largest planet?',
                     'What is the largest kind of whale?', 'Which dinosaur could fly?',
                     'Which of these Winnie the Pooh characters is a donkey?',
                     'What is the hottest planet?', 'Which dinosaur had the largest brain compared to body size?',
                     'What is the largest type of penguins?', "Which children's story character is a monkey?",
                     'How long is a year on Mars?']

    options1_list = [354, 'Mars', 'Orca whale', 'Triceratops', 'Pooh', 'Mars', 'Troodon', 'Chinstrap penguins',
                     'Winnie the Pooh', '550 Earth days']
    options2_list = [365, 'Jupiter', 'Humpback whale', ' Tyrannosaurus Rex', 'Piglet', 'Pluto', ' Ichthyosaurus',
                     'Macaroni penguins', 'Curious George', '498 Earth days']

    options3_list = [243, 'Earth', 'Beluga whale', 'Pteranodon', 'Piglet', 'Earth',
                     'Ichthyosaurus', 'Emperor penguins', 'Horton', '126 Earth days']

    options4_list = [379, 'Pluto', 'Blue whale', 'Diplodocus', 'Kanga', 'Venus', 'Gigantoraptor',
                     'White-flippered penguins', 'Goofy', '687 Earth day']

    correct_answers = [1, 2, 4, 3, 2, 4, 1, 3, 2, 4]
    object_list = []
    for i in range(len(question_list)):
        trv = Trivia(question_list[i], options1_list[i], options2_list[i], options3_list[i], options4_list[i],
                     correct_answers[i])
        object_list.append(trv)
    return object_list

