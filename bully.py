#type "bully me" in irc for horribot to send three hateful messages
import willie.module
import random

phrases = ['lol you never had a sticky','You are a pansy','You were adopted and your real mother hates you','I will beat you up','All your memes stopped mattering in 2014','You\'re a has been','Stop talking askhole','I will knock you in the gabber m8','birds are more important than you will ever be']

@willie.module.rule('bully me')
def bully(bot, trigger):
	for x in range (0,3):
		bully = random.choice(phrases)
		bot.reply(bully)
