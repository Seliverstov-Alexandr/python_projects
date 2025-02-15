prince=99
print(prince)
print(type(5), type(2.0), type(5+2.0))
a=4
b=5
a, b = b, a
print(a,b)
while a < 6: 
 a+=1
 b=b+1
print(b)
# 5 глава, упражнения

print('5.1')
song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray"""
print(song.replace('moray', 'Moray'))

print(5.2)
questions= [
    "We dont serve strings around here. Fre you a string?",
    "What is said on Father's Day in the forest?",
    "What makes the soud 'Sis! Boom! Bah!'?"
]
answers = [
    "An exploding sheep.",
    "No, I'am frayed knot.",
    "Pop, goes the weasel."
]

print('Q: ', questions[0].rjust(4), '\n', 'A: ', answers[1], '\n', 'Q: ', questions[1], '\n', 'A: ', answers[2], '\n', 'Q: ', questions[2], '\n', 'A: ', answers[0])

print(5.3)

words = ['roast beef', 'ham', 'head', 'clam']
print(" My kitty cat likes %s," % words[0], '\n', "My kitty cat likes %s," % words[1], '\n', "My kitty cat likes his %s" % words[2], 
'\n', "And now thinks he's a %s." % words[3])

print('5.4, 5.5 \n' )

letter = '''Dear {salutation} {name}, \n\nThank you for your letter. We are sorry that our {product} \n{verbed} in your {room}. Please note that it should never \nbe used in a {room}, 
especially near any {animals}. \n\nSend us your recipe and {amount} for shipping and handing. \nWe will send you another {product} that, in our tests, \nis {percent}% less likely to have {verbed}. \n\nThank you for your support. \nSincerely, \n{spokesman} \n{job_title}'''
print(letter)
salutation = 'mr'
name = 'Alex'
product = 'PS 5'
verbed = 'crashed'
room = 'bathroom'
animals = 'cats'
percent = '100'
spokesman = 'Pеter'
job_title = 'manager'
amount = '100 000$'
print(letter.format(
    salutation=salutation,
    name=name,
    product=product,
    verbed=verbed,
    room=room,
    animals=animals,
    percent=percent,
    spokesman=spokesman,
    job_title=job_title,
    amount=amount
))
print('\n', 5.6, '\n')
members = ['boat', 'Horse', 'Train']
name_of_members = ['Boaty McBoatface', 'Horsey McHorseface', 'Tranny McTrainface']
members_round_2 = ['Duck', 'pumpkin', 'Spitz']
name_of_members_2 = ['Donald', 'Pumbaa', 'Maya']
winners = ('WINNERS: \n'
'The %s %s\n' % (members[0], name_of_members[0]) +
'The %s %s\n' % (members[1], name_of_members[1]) +
'The %s %s\n' % (members[2], name_of_members[2]))
print(winners)
winners_round_2 = 'WINNERS_roud_2: \n' '%s %s\n' % (members_round_2[0], name_of_members_2[0]) + '%s %s\n' % (members_round_2[1], name_of_members_2[1]) + '%s %s\n' % (members_round_2[2], 
name_of_members_2[2])
print(winners_round_2)

print('\n 5.7 \n')
members = ['boat', 'Horse', 'Train']
name_of_members = ['Boaty McBoatface', 'Horsey McHorseface', 'Tranny McTrainface']
members_round_2 = ['Duck', 'pumpkin', 'Spitz']
name_of_members_2 = ['Donald', 'Pumbaa', 'Maya']
winners_placeholder = "WINNERS: \n {} {} \n {} {} \n {} {}" 
print(winners_placeholder.format(
members_round_2[1],name_of_members_2[1],
members_round_2[2],name_of_members_2[2],
members_round_2[0], name_of_members_2[0]
))

print('\n 5.8 \n')

print(f"WINNERS: \n {members[0]} {name_of_members[0]} \n {members[1]} {name_of_members[1]} \n {members[2]} {name_of_members[2]} ")

print(F"WINNERS ROUD 2 \n {members_round_2[0]} {name_of_members_2[0]} \n\
 {members_round_2[1]} {name_of_members_2[1]} \n {members_round_2[2]} {name_of_members_2[2]}")