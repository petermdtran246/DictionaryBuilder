def build_dictionary(words):
    dictionary = {}
    words.extend(dictionary)
    your_dictionary = {x:words.count(x) for x in words}
    print (f'The dictionary returned from calling build_dictionary(words) is:\n{your_dictionary}')
    return your_dictionary

if __name__ == '__main__':
    words = input().split()
    your_dictionary = build_dictionary(words)
    sorted_keys = sorted(your_dictionary.keys())
    for key in sorted_keys:
        print(f'{key} - {str(your_dictionary[key])}')
