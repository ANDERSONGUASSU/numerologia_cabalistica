from django.shortcuts import render

alpha_dict = {
    "a": 1,
    "e": 5,
    "i": 1,
    "o": 7,
    "u": 6,
    "á": 3,
    "é": 7,
    "í": 3,
    "ó": 9,
    "ú": 8,
    "à": 2,
    "è": 1,
    "ì": 2,
    "ò": 5,
    "ù": 3,
    "â": 8,
    "ê": 3,
    "î": 8,
    "ô": 5,
    "û": 4,
    "ã": 3,
    "õ": 1,
    "ü": 3,
    "b": 2,
    "c": 3,
    "d": 4,
    "f": 8,
    "g": 3,
    "h": 5,
    "j": 1,
    "k": 2,
    "l": 3,
    "m": 4,
    "n": 5,
    "p": 8,
    "q": 1,
    "r": 2,
    "s": 3,
    "t": 4,
    "v": 6,
    "w": 6,
    "x": 6,
    "y": 1,
    "z": 7,
    "ç": 6,
}

vowel_dict = {
    "a": 1,
    "e": 5,
    "i": 1,
    "o": 7,
    "u": 6,
    "á": 3,
    "é": 7,
    "í": 3,
    "ó": 9,
    "ú": 8,
    "à": 2,
    "è": 1,
    "ì": 2,
    "ò": 5,
    "ù": 3,
    "â": 8,
    "ê": 3,
    "î": 8,
    "ô": 5,
    "û": 4,
    "ã": 3,
    "õ": 1,
    "ü": 3,
}

consonant_dict = {
    "b": 2,
    "c": 3,
    "d": 4,
    "f": 8,
    "g": 3,
    "h": 5,
    "j": 1,
    "k": 2,
    "l": 3,
    "m": 4,
    "n": 5,
    "p": 8,
    "q": 1,
    "r": 2,
    "s": 3,
    "t": 4,
    "v": 6,
    "w": 6,
    "x": 6,
    "y": 1,
    "z": 7,
    "ç": 6,
}


def home(request):
    return render(request, "pages/home.html")


def calculate_numerology_alpha(letter):
    return alpha_dict.get(letter.lower(), "")


def calculate_numerology_vowel(letter):
    return vowel_dict.get(letter.lower(), "")


def calculate_numerology_consonant(letter):
    return consonant_dict.get(letter.lower(), "")


def decompose_number(number):
    decomposition = [number]
    while number >= 10:
        digits = [int(digit) for digit in str(number)]
        number = sum(digits)
        decomposition.append(number)
    return decomposition


def calculate_numerology_pyramid(name):
    pyramid = []
    for letter in name:
        numerology_value = calculate_numerology_alpha(letter)
        pyramid.append(numerology_value)
    return pyramid[::-1]


def result(request):
    if request.method == "POST":
        name = request.POST.get("name")
        name = name.replace(" ", "")

        pyramid = calculate_numerology_pyramid(name)

        numerology_alpha = [calculate_numerology_alpha(letter) for letter in name]
        numerology_vowels = [calculate_numerology_vowel(letter) for letter in name]
        numerology_consonants = [
            calculate_numerology_consonant(letter) for letter in name
        ]

        numerology_alpha_binary = [str(num) for num in numerology_alpha]
        numerology_vowels_binary = [str(num) for num in numerology_vowels]
        numerology_consonants_binary = [str(num) for num in numerology_consonants]

        sum_alpha = sum([num for num in numerology_alpha if isinstance(num, int)])
        sum_vowels = sum([num for num in numerology_vowels if isinstance(num, int)])
        sum_consonants = sum(
            [num for num in numerology_consonants if isinstance(num, int)]
        )

        decomposed_alpha = decompose_number(sum_alpha)
        decomposed_vowels = decompose_number(sum_vowels)
        decomposed_consonants = decompose_number(sum_consonants)

        reduced_decomposed_alpha = []
        for i in range(len(decomposed_alpha) - 1):
            pair_sum = decomposed_alpha[i] + decomposed_alpha[i + 1]
            if pair_sum > 9:
                pair_sum = sum([int(digit) for digit in str(pair_sum)])
            reduced_decomposed_alpha.append(pair_sum)
        context = {
            "name": name,
            "numerology_alpha_binary": numerology_alpha_binary,
            "numerology_vowels_binary": numerology_vowels_binary,
            "numerology_consonants_binary": numerology_consonants_binary,
            "sum_vowels": sum_vowels,
            "sum_consonants": sum_consonants,
            "sum_alpha": sum_alpha,
            "reduced_decomposed_alpha": reduced_decomposed_alpha,
            "decomposed_alpha": decomposed_alpha,
            "decomposed_vowels": decomposed_vowels,
            "decomposed_consonants": decomposed_consonants,
            "pyramid": pyramid,
            }

        return render(request, "pages/result.html", context)
    else:
        return render(request, "pages/home.html")
