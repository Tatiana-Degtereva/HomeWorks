# Самостоятельная работа по уроку "Произвольное число параметров".
# Задача "Однокоренные":
# Напишите функцию single_root_words, которая принимает одно обязательное слово в параметр root_word,
# а далее неограниченную последовательность в параметр *other_words.
# Функция должна составить новый список same_words только из тех слов списка other_words,
# которые содержат root_word или наоборот root_word содержит одно из этих слов.
# После вернуть список same_words в качестве результата своей работы.

def single_root_words(root_word, *other_words):
    same_words = []
    root_word_lower=root_word.lower()
    for i in other_words:
        i_lower=i.lower()
        if i_lower.count(root_word_lower) == False and root_word_lower.count(i_lower) == False:
            continue
        else:
            same_words.append(i)
    return(same_words)

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)