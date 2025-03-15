import re

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
                "flower_playing_cards": "🎴", "cards": "🎴", "deck": "🎴"
                }


def emoji_text(text, custom_mappings=None):
    
    """
    Replace keywords in the text with corresponding emojis.
    
    :param text: The input text.
    :param custom_mappings: A dictionary of custom emoji mappings.
    :return: The text with emojis.
    """
    mappings = {**EMOJI_MAPPINGS, **(custom_mappings or {})}
    
    for word, emoji_char in mappings.items():
        text = re.sub(rf"\b{word}\b", emoji_char, text)
      
    return text



