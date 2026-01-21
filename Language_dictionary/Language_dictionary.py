import streamlit as st


ethopia_dict= {
   'Good Morning' : 'Tena yistilign',
   'Please' : 'Ebakesh', 
     'Thank You': 'Ameseginalehu', 
     'Welcome':'metash',  
    'Beautiful' : 'Konjo', 
    'Friend' : 'Guadegna',
    'yes' : 'Awo',
    'No' : 'Ay',
    'sorry' :'Yikirta',
    'Food' : 'Migib',
    'Water' : 'Wuhaa',
    'love' : 'Fikir',
    'God' : 'Egziabher',
    'Peace' : 'Selam',
    'Child' : 'Lij',
    'School' : 'Timhirt bet',
    'Work' : 'Sira',
    'Day' : 'Ken',
    'Time' : 'Gize',
    'Road' : 'Menged',
}
swahili_dict = {
    'Hello' : 'Jambo',
    'thank you' : 'Asante',
    'Yes' : 'Ndiyo',
    'No' : 'Hapana',
    'Excuse me' : 'Samanahi',
    'Okay' : 'Sawa',
    'Water' : 'Maji',
    'Food' : 'Chakula',
    'Friend' : 'Rafiki',
    'Tommorow' : 'Kesho',
    'Me' : 'Mimi',
    'Today' : 'Leo',
    'No problem' : 'Hakuna matata',
    'You' : 'Wewe',
    'Please' : 'Tafadhali',
    'Good' : 'NZuri',
    'Name' : 'Jina',
    'Slowly,slowly' : 'Pole pole',
    'Welcome' : "Karibu",
    'To see' :'Kouna'}

hausa_dict={
              "thank you": "nagode",
              "hello": "sannu",
              "bye": "wallahi",
              "morning": "safe",
              "evening": "mariace",
              "after": "rana",
              "beautiful": "kyau",
              "smart": "mai hankali",
              "strong": "mai karfi",
              "house": "gida",
              "school": "makaranta",
              "mouth": "baki",
              "eye": "ido",
              "head": "kai",
              "food": "abinci",
              'tall' : 'tsayi',
              'short' : 'gajere',
              'fat' : 'mai',
              'slim' : 'siriri',
              'good' : 'mai kyau',
              'bad' :'mara kyau'
              }

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

languages_dict = {
    'Ethopia': ethopia_dict,
    'Swahili' : swahili_dict,
    'Hausa' : hausa_dict,
    'Igbo' : igbo_dict
    }

choice = st.selectbox('Language', 
                      list(languages_dict.keys()))
word = st.text_input('Enter an english word: ').lower()

if word in languages_dict[choice]:
    st.write(f"{word} in {choice} is:{languages_dict[choice][word]}")
else:
    st.write(f'Word not fount in {choice} dictionary')