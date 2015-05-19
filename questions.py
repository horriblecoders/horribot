#This acts as a magic eightball
#There is probably a much better way to write this but I am not sure how.
import willie.module
import random

responses = ['Yes', 'No', 'Go away', 'Ask again later', 'You would be surprise', 'Google it nerd', 'You were trying to be funny but that wasn\'t funny','It is certain','It is decidedly so','Without a doubt','Yes definitely','You may rely on it','As I see it, yes','Most likely','Outlook good','Signs point to yes','Reply hazy try again','Better not tell you now','Do you think im a fortune teller?','Ask someone else, I am mad at you right now','Don\'t count on it','My reply is no','My sources say no','Outlook not so good','Very doubtful','Be quiet']

@willie.module.rule('horribot: do')
def doOne(bot, trigger):
	greeting = random.choice(responses)
	bot.reply(greeting)

@willie.module.rule('horribot do')
def doTwo(bot, trigger):
	greeting = random.choice(responses)
	bot.reply(greeting)

@willie.module.rule('horribot, do')
def doThree(bot, trigger):
	greeting = random.choice(responses)
	bot.reply(greeting)

@willie.module.rule('horribot, is')
def is1(bot, trigger):
	greeting = random.choice(responses)
	bot.reply(greeting)

@willie.module.rule('horribot is')
def is2(bot, trigger):
	greeting = random.choice(responses)
	bot.reply(greeting)

@willie.module.rule('horribot: is')
def is3(bot, trigger):
	greeting = random.choice(responses)
	bot.reply(greeting)

@willie.module.rule('horribot: what')
def what1(bot, trigger):
	greeting = random.choice(responses)
	bot.reply(greeting)

@willie.module.rule('horribot, what')
def what2(bot, trigger):
	greeting = random.choice(responses)
	bot.reply(greeting)

@willie.module.rule('horribot what')
def what3(bot, trigger):
	greeting = random.choice(responses)
	bot.reply(greeting)

@willie.module.rule('horribot: how')
def how1(bot, trigger):
	greeting = random.choice(responses)
	bot.reply(greeting)

@willie.module.rule('horribot, how')
def how2(bot, trigger):
	greeting = random.choice(responses)
	bot.reply(greeting)

@willie.module.rule('horribot how')
def how3(bot, trigger):
	greeting = random.choice(responses)
	bot.reply(greeting)

@willie.module.rule('horribot: where')
def where1(bot, trigger):
	greeting = random.choice(responses)
	bot.reply(greeting)

@willie.module.rule('horribot, where')
def where2(bot, trigger):
	greeting = random.choice(responses)
	bot.reply(greeting)

@willie.module.rule('horribot where')
def where3(bot, trigger):
	greeting = random.choice(responses)
	bot.reply(greeting)

@willie.module.rule('horribot: when')
def when1(bot, trigger):
	greeting = random.choice(responses)
	bot.reply(greeting)

@willie.module.rule('horribot, when')
def when2(bot, trigger):
	greeting = random.choice(responses)
	bot.reply(greeting)

@willie.module.rule('horribot when')
def when3(bot, trigger):
	greeting = random.choice(responses)
	bot.reply(greeting)

@willie.module.rule('horribot: why')
def why1(bot, trigger):
	greeting = random.choice(responses)
	bot.reply(greeting)

@willie.module.rule('horribot, why')
def why2(bot, trigger):
	greeting = random.choice(responses)
	bot.reply(greeting)

@willie.module.rule('horribot why')
def why3(bot, trigger):
	greeting = random.choice(responses)
	bot.reply(greeting)

@willie.module.rule('horribot: are')
def are1(bot, trigger):
	greeting = random.choice(responses)
	bot.reply(greeting)

@willie.module.rule('horribot, are')
def are2(bot, trigger):
	greeting = random.choice(responses)
	bot.reply(greeting)

@willie.module.rule('horribot are')
def are3(bot, trigger):
	greeting = random.choice(responses)
	bot.reply(greeting)
