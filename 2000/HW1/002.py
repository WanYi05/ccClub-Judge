n = int(input())
translation_dict = {}

for i in range(n):
    source, target = input().split()
    translation_dict[source] = target

query = input().split()
translated_words = [translation_dict[word] for word in query]
print(" ".join(translated_words))