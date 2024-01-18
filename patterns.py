class Named:
    def __init__(self):
        self.nameai = "Ai Rich"
        self.name = "iquen"
        self.surname = "marba"
        self.mid = "l"

P=Named()

patterns = [
    (r'hello|hi|hey', [f'Hello! im {P.nameai}', f'Hi there! im {P.nameai}', f'Hey! im {P.nameai}']),
    (r'how are you', ['I am good, thank you!', 'I\'m doing well, how about you?']),
    (r'what you name|who are you|name', [f'I am {P.nameai} a simple chatbot .', f'Call me {P.nameai} Chatbot.']),
    (r'quit|good bye|bye', ['Goodbye!', 'See you later.']),
    (r'music|song|play music|play song',
     ['Sure, playing some music for you!', 'Alright, let me play a song for you.']),

    (r'how are you doing today', ['Im doing well, thank you for asking!', 'Feeling good today!']),
    (r'what can you do', ['I can assist you with information, answer questions, or just chat with you.']),
    (r'tell me a joke', ['Why don’t scientists trust atoms? Because they make up everything!',
                         'Sure, here\'s one: Why did the computer catch a cold? It left its Windows open.']),
    (r'weather|forecast', ['Im sorry, I don\t have access to real-time weather information.']),
    (r'thank you', ['You\'re welcome!', 'Anytime!']),
    (r'how old are you', ['I don\'t have an age, as I am a computer program.']),
    (r'who created you', [
        f'I was created by a student named {P.name} {P.surname} a a second year bsit college student from Evsu Ormoc city campus.']),
    (r'close', [f'okay {P.name}', 'okay sir', f'okay {P.name}']),
    (r'open facebook|facebook|fbook', [f'opening facebook {P.name}', f'okay {P.name} opening FB']),
    (r'open youtube|youtube', [f'opening youtube {P.name}', f'okay {P.name} opening youtube']),
    (r'open wife|wifey account|mahal facebook|wifey|wife', [f'opening richelle account {P.name}', f'okay {P.name} opening mahal account']),
    (r'(?:open\s)?chat gpt|gpt', [f'opening chatgpt {P.name}', f'okay {P.name} opening chatgpt Ai']),
    (r'(?:open\s)?facebook|facebook|fbook', [f'Opening Facebook, {P.name}', f'Okay {P.name}, opening FB']),
    (r'(?:open\s)?youtube|youtube', [f'Launching YouTube, {P.name}', f'Okay {P.name}, opening YouTube']),
    (r'(?:open\s)?instagram|ig', [f'Accessing Instagram, {P.name}', f'Okay {P.name}, entering Instagram realm']),
    (r'(?:open\s)?twitter', [f'Initiating Twitter, {P.name}', f'Okay {P.name}, unlocking Twitter']),
    (r'(?:open\s)?linkedin', [f'Navigating to LinkedIn, {P.name}', f'Alright {P.name}, accessing LinkedIn']),
    (r'(?:open\s)?snapchat', [f'Activating Snapchat, {P.name}', f'Okay {P.name}, launching Snapchat']),
    (r'(?:open\s)?reddit', [f'Entering Reddit, {P.name}', f'Okay {P.name}, accessing the Reddit universe']),
    (r'(?:open\s)?pinterest', [f'Unlocking Pinterest, {P.name}', f'Alright {P.name}, entering Pinterest world']),
    (r'(?:open\s)?tiktok', [f'Starting TikTok, {P.name}', f'Okay {P.name}, launching TikTok for you']),
    (r'(?:open\s)?github', [f'Accessing GitHub, {P.name}', f'Alright {P.name}, opening GitHub repository']),
    (r'(?:open\s)?stackoverflow', [f'Initiating Stack Overflow, {P.name}', f'Okay {P.name}, accessing Stack Overflow wisdom']),
    (r'(?:open\s)?amazon', [f'Entering Amazon, {P.name}', f'Okay {P.name}, launching Amazon for you']),
    (r'(?:open\s)?ebay', [f'Starting eBay, {P.name}', f'Alright {P.name}, entering eBay marketplace']),
    (r'(?:open\s)?netflix', [f'Accessing Netflix, {P.name}', f'Okay {P.name}, launching Netflix entertainment']),
    (r'(?:open\s)?spotify', [f'Unlocking Spotify, {P.name}', f'Alright {P.name}, accessing Spotify tunes']),

]