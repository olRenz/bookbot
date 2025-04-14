def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def word_count(file_path):
    words = get_book_text(file_path)
    return len(words.split())


def word_dict(file_path):
    words = get_book_text(file_path)
    letter_dict = {}

    for letter in words.lower():
        if letter.isalpha():
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1

    return letter_dict


def dic_organizer(file_path):
    letter_dict = word_dict(file_path)
    dict_list = []

    for letter in letter_dict:
        total = letter_dict[letter]
        dict_list.append({"letter": letter, "total": total})

    return dict_list


def sort_on(dict):
    return dict["total"]


def sort_list(file_path):
    unsorted_list = dic_organizer(file_path)
    unsorted_list.sort(reverse=True, key=sort_on)

    sorted_list = []
    for entry in unsorted_list:
        sorted_list.append(f"{entry['letter']}: {entry['total']}")

    return sorted_list
