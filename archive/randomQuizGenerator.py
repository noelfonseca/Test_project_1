#! python3

#randomQuizGenerator.py - creates quizzes with questions and answers in random order, along with the answer key

import random

# KEYS are states, VALUES are the capitals

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee','Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence','South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(35):
   # Create the quiz and answer key files.
   quizFile = open('capitalsquiz%s.txt' %(quizNum + 1), 'w')
   answerKeyFile = open('capitalsquiz_answers%s.txt' %(quizNum + 1), 'w')

   # Write out the header for the quiz.
   quizFile.write('Name:\n\nDate:\n\nPeriod\n\n')
   quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' %(quizNum + 1))
   quizFile.write('\n\n')

   # Shuffle the order of the states
   states = list(capitals.keys())     # generates a list of states
   random.shuffle(states)             # shuffles the states


   # Loop through all 50 states, making a question for each.
   for questionNum in range(50):
      #Get right and wrong answers.
      correctAnswer = capitals[states[questionNum]]
      wrongAsnwers = list(capitals.values())
      del wrongAsnwers[wrongAsnwers.index(correctAnswer)]
      wrongAsnwers = random.sample(wrongAsnwers, 3)
      answerOptions = wrongAsnwers + [correctAnswer]
      random.shuffle(answerOptions)

      # Write the question and the answer options to the quiz file.
      quizFile.write('%s. What is the capital of %s\n' % (questionNum + 1, states[questionNum]))
      for i in range(4):
         quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
      quizFile.write('\n')

      #Write the answer key to file.

      answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
   quizFile.close()
   answerKeyFile.close()