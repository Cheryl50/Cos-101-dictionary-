igbo_dict = {
    "food" : "nri",
    "water" : "mmiri",
    "house" : "ụlọ",
    "love" : "ịhụnanya",
    "friend" : "enyi",
    "family" : "ezinụlọ",
    "man" : "nwoke",
    "woman" : "nwanyị",
    "fire" : "ọkụ",
    "earth" : "ala",
    "sky" : "igwe",
    "tree" : "osisi",
    "sun" : "anwụ",
    "moon" : "ọnwa",
    "star" : "kpakpando",
    "child" : "nwa",
    "school" : "ụlọ akwụkwọ",
    "work" : "ọrụ",
    "music" : "egwu",
    "dance" : "ịgba egwu",
} 
def translate_to_igbo(word):
    word = word.lower()
    if word in igbo_dict:
        return igbo_dict[word]
    else:
        return "Word not found in Igbo dictionary"
       