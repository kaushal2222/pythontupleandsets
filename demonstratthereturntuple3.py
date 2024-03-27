# x = [1, 2, 3]
# y = [4, 5, 6]
# zipped = zip(x, y)
# a=list(zipped)
# print(a)

questions = ('name', 'quest', 'favorite color')
answers = ('lancelot', 'the holy grail', 'blue')
for quetion, answer in zip(questions, answers):
  print(f'What is your {quetion}? It is {answer}.')
