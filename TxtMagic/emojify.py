import re
from textblob import TextBlob

EMOJI_MAPPINGS ={
                "smile": "😊", "happy": "😊", "joy": "😊","joyful": "😊", "laugh": "😂", "lol": "😂", "funny": "😂",
                "heart_eyes": "😍", "love": "😍", "crush": "😍", "cool": "😎", "sunglasses": "😎", "swag": "😎",
                "angry": "😡", "mad": "😡", "furious": "😡", "sad": "😢", "cry": "😢", "tears": "😢",
                "surprised": "😮", "shock": "😮", "whoa": "😮", "thinking": "🤔", "hmm": "🤔", "confused": "🤔",
                "thumbs_up": "👍", "like": "👍", "approve": "👍", "clap": "👏", "applause": "👏", "bravo": "👏",
                "rocket": "🚀", "fast": "🚀", "launch": "🚀", "fire": "🔥", "lit": "🔥", "hot": "🔥",
                "star": "⭐", "favorite": "⭐", "highlight": "⭐", "sun": "☀️", "bright": "☀️", "morning": "☀️",
                "moon": "🌙", "night": "🌙", "sleep": "🌙", "rainbow": "🌈", "pride": "🌈", "colorful": "🌈",
                "pizza": "🍕", "food": "🍕", "cheese": "🍕", "coffee": "☕", "tea": "☕", "caffeine": "☕",
                "beer": "🍺", "drink": "🍺", "party": "🍺", "wine": "🍷", "red_wine": "🍷", "cheers": "🍷",
                "burger": "🍔", "fast_food": "🍔", "cheeseburger": "🍔", "ice_cream": "🍦", "dessert": "🍦", "sweet": "🍦",
                "dog": "🐶", "puppy": "🐶", "pet": "🐶", "cat": "🐱", "kitten": "🐱", "meow": "🐱",
                "bird": "🐦", "tweet": "🐦", "feather": "🐦", "fish": "🐟", "ocean": "🐟", "sea": "🐟", "Python":"🐍",
                "tree": "🌳", "nature": "🌳", "forest": "🌳", "flower": "🌸", "bloom": "🌸", "blossom": "🌸",
                "book": "📖", "read": "📖", "study": "📖", "computer": "💻", "laptop": "💻", "work": "💻",
                "phone": "📱", "mobile": "📱", "call": "📱", "music": "🎵", "song": "🎵", "melody": "🎵",
                "game": "🎮", "video_game": "🎮", "play": "🎮", "football": "⚽", "soccer": "⚽", "goal": "⚽",
                "basketball": "🏀", "hoops": "🏀", "dunk": "🏀", "car": "🚗", "drive": "🚗", "travel": "🚗",
                "plane": "✈️", "flight": "✈️", "airplane": "✈️", "ship": "🚢", "cruise": "🚢", "boat": "🚢",
                "train": "🚆", "railway": "🚆", "metro": "🚆", "bike": "🚲", "bicycle": "🚲", "ride": "🚲",
                "heart": "❤️", "love": "❤️", "romance": "❤️", "money": "💰", "cash": "💰", "rich": "💰",
                "shopping": "🛍️", "buy": "🛍️", "store": "🛍️", "clock": "⏰", "alarm": "⏰", "time": "⏰",
                "calendar": "📅", "date": "📅", "schedule": "📅", "email": "📧", "message": "📧", "mail": "📧",
                "scissors": "✂️", "cut": "✂️", "craft": "✂️", "lock": "🔒", "security": "🔒", "safe": "🔒",
                "lightbulb": "💡", "idea": "💡", "innovation": "💡", "battery": "🔋", "charge": "🔋", "power": "🔋",
                "microscope": "🔬", "science": "🔬", "experiment": "🔬", "hammer": "🔨", "tool": "🔨", "fix": "🔨",
                "knife": "🔪", "sharp": "🔪", "cut": "🔪", "gun": "🔫", "shoot": "🔫", "weapon": "🔫",
                "bomb": "💣", "explode": "💣", "danger": "💣", "trophy": "🏆", "win": "🏆", "champion": "🏆",
                "medal": "🏅", "gold": "🏅", "winner": "🏅", "running": "🏃", "exercise": "🏃", "run": "🏃",
                "boxing_glove": "🥊", "punch": "🥊", "fight": "🥊", "flag": "🏁", "finish": "🏁", "race": "🏁",
                "yo_yo": "🪀", "toy": "🪀", "fun": "🪀", "puzzle_piece": "🧩", "solution": "🧩", "problem_solving": "🧩",
                "teddy_bear": "🧸", "cute": "🧸", "soft": "🧸", "spades": "♠️", "cards": "♠️", "game": "♠️",
                "black_joker": "🃏", "joker": "🃏", "wildcard": "🃏", "mahjong": "🀄", "game": "🀄", "tiles": "🀄",
                "flower_playing_cards": "🎴", "cards": "🎴", "deck": "🎴",
                # Household items
                "home": "🏠", "house": "🏠", "living": "🏠","bed": "🛏️", "sleep": "🛏️", "rest": "🛏️",
                "couch": "🛋️", "sofa": "🛋️", "relax": "🛋️","tv": "📺", "television": "📺", "watch": "📺",
                "lamp": "💡", "light": "💡", "bright": "💡","shower": "🚿", "bath": "🛁", "clean": "🧼",
                "toilet": "🚽", "bathroom": "🚽", "restroom": "🚽","kitchen": "🍳", "cooking": "🍳", "food": "🍳",
                "fridge": "❄️", "refrigerator": "❄️", "cold": "❄️","microwave": "🍲", "heat": "🍲", "warm": "🍲",
                "washing_machine": "🧺", "laundry": "🧺", "clothes": "👕",
    
                # Office/school
                "office": "🏢", "work": "🏢", "business": "🏢","school": "🏫", "education": "🏫", "learn": "🏫",
                "desk": "🪑", "study": "🪑", "work": "🪑", "pen": "🖊️", "write": "🖊️", "ink": "🖊️",
                "pencil": "✏️", "draw": "✏️", "sketch": "✏️", "paper": "📄", "document": "📄", "print": "📄",
                "folder": "📁", "files": "📁", "organize": "📁", "briefcase": "💼", "business": "💼", "work": "💼",
                "meeting": "🤝", "conference": "🤝", "discussion": "🤝",
    
                # Weather
                "cloud": "☁️", "cloudy": "☁️", "overcast": "☁️", "rain": "🌧️", "raining": "🌧️", "drizzle": "🌧️",
                "snow": "❄️", "snowing": "❄️", "cold": "❄️", "wind": "🌬️", "windy": "🌬️", "breeze": "🌬️",
                "storm": "⛈️", "thunder": "⛈️", "lightning": "⚡","sunny": "☀️", "clear": "☀️", "bright": "☀️",
                "umbrella": "☔", "rainy": "☔", "wet": "☔",
    
                # Health/medical
                "hospital": "🏥", "doctor": "🏥", "health": "🏥", "pill": "💊", "medicine": "💊", "sick": "💊",
                "bandage": "🩹", "hurt": "🩹", "injury": "🩹", "syringe": "💉", "vaccine": "💉", "shot": "💉",
                "ambulance": "🚑", "emergency": "🚑", "help": "🚑", "stethoscope": "🩺", "checkup": "🩺", "health": "🩺",
    
                # Family/people
                "family": "👪", "parents": "👪", "children": "👪", "mom": "👩", "mother": "👩", "mama": "👩",
                "dad": "👨", "father": "👨", "papa": "👨", "baby": "👶", "infant": "👶", "newborn": "👶",
                "grandma": "👵", "grandmother": "👵", "nana": "👵", "grandpa": "👴", "grandfather": "👴", "papa": "👴",
                "couple": "👫", "dating": "👫", "relationship": "👫", "friends": "👭", "buddies": "👭", "pals": "👭",
    
                # Hobbies
                "camera": "📷", "photo": "📷", "picture": "📷", "paint": "🎨", "art": "🎨", "draw": "🎨",
                "guitar": "🎸", "music": "🎸", "play": "🎸", "movie": "🎬", "film": "🎬", "cinema": "🎬",
                "fishing": "🎣", "fish": "🎣", "catch": "🎣", "gardening": "🌱", "plant": "🌱", "grow": "🌱",
                "chess": "♟️", "strategy": "♟️", "game": "♟️",
    
                # Holidays/events
                "birthday": "🎂", "party": "🎂", "celebrate": "🎂", "christmas": "🎄", "xmas": "🎄", "holiday": "🎄",
                "halloween": "🎃", "spooky": "🎃", "scary": "🎃", "easter": "🐣", "eggs": "🐣", "spring": "🐣",
                "new_year": "🎆", "fireworks": "🎆", "celebration": "🎆", "valentine": "💝", "romance": "💝", "february": "💝",
    
                # Technology
                "wifi": "📶", "internet": "📶", "connection": "📶",
                "bluetooth": "📡", "wireless": "📡", "connect": "📡",
                "robot": "🤖", "ai": "🤖", "future": "🤖",
                "vr": "🕶️", "virtual": "🕶️", "reality": "🕶️",
                "website": "🌐", "online": "🌐", "web": "🌐",
                "password": "🔑", "security": "🔑", "login": "🔑",
    
                # Transportation
                "bus": "🚌", "transport": "🚌", "commute": "🚌",
                "taxi": "🚕", "cab": "🚕", "ride": "🚕",
                "truck": "🚚", "delivery": "🚚", "shipping": "🚚",
                "motorcycle": "🏍️", "bike": "🏍️", "ride": "🏍️",
                "scooter": "🛴", "kick": "🛴", "ride": "🛴",
                "helicopter": "🚁", "fly": "🚁", "air": "🚁",
    
                # Zodiac signs
                "aries": "♈", "taurus": "♉", "gemini": "♊",
                "cancer": "♋", "leo": "♌", "virgo": "♍",
                "libra": "♎", "scorpio": "♏", "sagittarius": "♐",
                "capricorn": "♑", "aquarius": "♒", "pisces": "♓",
    
                # Money/business
                "bank": "🏦", "money": "🏦", "finance": "🏦",
                "credit_card": "💳", "debit": "💳", "pay": "💳",
                "receipt": "🧾", "bill": "🧾", "payment": "🧾",
                "stocks": "📈", "invest": "📈", "market": "📈",
                "crypto": "₿", "bitcoin": "₿", "blockchain": "₿",
    
                # Time
                "hourglass": "⏳", "time": "⏳", "wait": "⏳",
                "watch": "⌚", "clock": "⌚", "time": "⌚",
                "stopwatch": "⏱️", "timer": "⏱️", "countdown": "⏱️",
                "alarm": "⏰", "wake": "⏰", "time": "⏰",
    
                # Miscellaneous
                "key": "🔑", "lock": "🔑", "security": "🔑",
                "gift": "🎁", "present": "🎁", "surprise": "🎁",
                "balloon": "🎈", "party": "🎈", "celebrate": "🎈",
                "confetti": "🎊", "celebration": "🎊", "party": "🎊",
                "magic": "🎩", "trick": "🎩", "illusion": "🎩",
                "hiking": "🥾", "walk": "🥾", "mountain": "🥾",
                "camping": "⛺", "tent": "⛺", "outdoors": "⛺",
                "fitness": "💪", "gym": "💪", "exercise": "💪",
                "yoga": "🧘", "meditate": "🧘", "peace": "🧘",
                "shopping": "🛒", "cart": "🛒", "buy": "🛒",
                "receipt": "🧾", "bill": "🧾", "payment": "🧾",
                "package": "📦", "delivery": "📦", "mail": "📦",
                "trash": "🗑️", "garbage": "🗑️", "waste": "🗑️",
                "recycle": "♻️", "eco": "♻️", "green": "♻️",
                "idea": "💡", "lightbulb": "💡", "creative": "💡",
                "warning": "⚠️", "danger": "⚠️", "caution": "⚠️",
                "question": "❓", "ask": "❓", "help": "❓",
                "exclamation": "❗", "important": "❗", "alert": "❗",
                "silence": "🤫", "quiet": "🤫", "shush": "🤫",
                "speak": "🗣️", "talk": "🗣️", "voice": "🗣️",
                "whisper": "🔇", "quiet": "🔇", "secret": "🔇"

                
}


SENTIMENT_EMOJIS = {
    "positive": ["😍", "🎉", "🔥", "😃"],
    "neutral": ["😐", "🙂"],
    "negative": ["😢", "😡", "💔"]
}


LETTER_EMOJI_MAPPINGS = {
    "A": "🅰️ ", "B": "🅱️ ", "C": "©️ ", "D": "🅳", "E": "🅴", "F": "🅵", "G": "🅶", "H": "🅷",
    "I": "ℹ️ ", "J": "🅹", "K": "🅺", "L": "🛴", "M": "Ⓜ️ ", "N": "🅽", "O": "🅾️", "P": "🅿️ ",
    "Q": "🆀", "R": "🆁", "S": "💲", "T": "🆃", "U": "🆄", "V": "🆅", "W": "🆆", "X": "❎",
    "Y": "🆈", "Z": "💤",
    "0": "0️⃣", "1": "1️⃣", "2": "2️⃣", "3": "3️⃣", "4": "4️⃣", "5": "5️⃣", "6": "6️⃣", "7": "7️⃣", "8": "8️⃣", "9": "9️⃣"
}



def emoji_text(text, custom_mappings=None):
    """
    Replace keywords in the text with corresponding emojis.
    Then, replace ALL remaining letters/numbers with emoji versions.
    
    :param text: The input text.
    :param custom_mappings: A dictionary of custom emoji mappings.
    :return: The text with emojis.
    """
    mappings = {**EMOJI_MAPPINGS, **(custom_mappings or {})}
    
    # First, replace whole words with emojis (case-insensitive)
    for word, emoji_char in mappings.items():
        text = re.sub(rf"\b{word}\b", emoji_char, text, flags=re.IGNORECASE)
    
    # Then, replace EVERY remaining letter/number (even inside words)
    for char, emoji_char in LETTER_EMOJI_MAPPINGS.items():
        text = text.replace(char, emoji_char)
        text = text.replace(char.lower(), emoji_char)  # Handle lowercase letters
    
    return text


def add_emojis_With_text(text):
    """
    Replaces words in the text with corresponding emojis.
    
    :param text: Input sentence.
    :return: Text with words replaced by emojis.
    """
    words = text.split()
    for i, word in enumerate(words):
        clean_word = re.sub(r'[^\w\s]', '', word).lower()  # Remove punctuation & lowercase
        if clean_word in EMOJI_MAPPINGS:
            words[i] = f"{word} {EMOJI_MAPPINGS[clean_word]}"  # Append emoji to word
    return " ".join(words)


def analyze_sentiment(text):
    """
    Analyzes the sentiment of the given text and appends suitable emojis.
    
    :param text: Input sentence.
    :return: Text with sentiment-based emojis.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # Get sentiment score (-1 to 1)
    
    if polarity > 0.2:
        emojis = " ".join(SENTIMENT_EMOJIS["positive"])
    elif polarity < -0.2:
        emojis = " ".join(SENTIMENT_EMOJIS["negative"])
    else:
        emojis = " ".join(SENTIMENT_EMOJIS["neutral"])
    
    return f"{text} {emojis}"



