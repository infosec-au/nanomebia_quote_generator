import random

def random_quote():
	wisdom_quotes = ["How do I inject", "I make boxes alert hard", "prompt, alert, confirm",
					 "Want an awkward hug bro", "oi give me an awkward hug",
					 "Gin and tonics make the world go around", "it's not Silvio, it's DR Silvio to you!",
					 "Master Wahckon Organiser or what mate", "We've had a total of 50 ultra vip tickets purchased for wachkon",
					 "Andrew is going to Tokyo soon, fuck yeah!", "omg I have to share a place with shubs at tokyo FML",
					 "I am the bestest for hosting Hackhouse and Wahckon", "Hacker overlord",
					 "Kali linux is the only linux I have, no dual boot bro", "what's the name of a really good hacker? andrew bro",
					 "OK i am running out of quote ideas", "weak filters in javascript turn me on", "xss, thats cool bro come back when you have rce",
					 "Do you even know how to hack??? srsluy", "One bulldogs gin and tonic please", "do the pwn dance bro",
					 "*dances after getting uid 0*", "*dances after finding persistent xss*", "OMG THIS CLIENT IS SO SLOW", "incident responding expert",
					 "responding to incident responding since 2010'"
					]
	return random.choice(wisdom_quotes)

def random_bios():
	bios = ["WAHCKON OVERLORD",
			"1337 h4x0r straight from hackforums.net",
			"ethics in infosec manager",
			"super wahckon organiser",
			"CTF muncher",
			"injection master",
			"xss cruncher",
			"Gin and Tonic demolisher",
			"Alocohol Lover",
			"Whisky Expert"
			"X-Forwarded-For: Andrews Computer",
			"Anime Lover and Expert",
			"Professional Endorsementer",
			"Cheesecakes endorser ",
			"Professional Box Popper"
			]
	return random.choice(bios)

print random_quote() + " - Andrew Kitis, " + random_bios() + "."