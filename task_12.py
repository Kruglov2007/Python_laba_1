#  разбивает текст на слова;
#  считает общее количество слов;
#  ведет подсчет частоты каждого слова;
#  определяет самое часто встречающееся слово;
#  находит самое короткое и самое длинное слова;
#  отбрасывает слова длиной менее трех символов и повторяет анализ

text=input("Ваш текст:").strip().lower().split()
def TZ(text):
    if not text:  # Защита от пустого списка
        print("Список слов пуст!")
        return
    new_txt=set(text)
    print(f"Количество слов:{len(text)}")
    counter=0
    max_word=0
    l_word=''
    s_word=text[0]
    most_freq_word = ''
    for word in new_txt:
        print(f"Слово {word} встречается: {text.count(word)}")
        if len(word)<len(s_word):
            s_word=word

        if len(word)>max_word:
            max_word=len(word)
            l_word=word
        if text.count(word)>counter:
            counter=text.count(word)
            most_freq_word = word 
    print(f"Самое часто встречающееся слово: '{most_freq_word}' (встречается {counter} раз(а))")
    print(f"Самое длинное слово:{l_word}")
    print(f"Самое короткое слово:{s_word}")


TZ(text)
text=[w for w in text if len(w) > 2]
TZ(text)