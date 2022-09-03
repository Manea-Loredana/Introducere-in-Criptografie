# -*- coding: utf-8 -*-
"""


@author: loredana
"""

from collections import defaultdict
from matplotlib import pyplot
from scipy.stats import chisquare

eng_freq = {
    'A': 0.08167, 
    'B': 0.01492,
    'C': 0.02782, 
    'D': 0.04253, 
    'E': 0.12702, 
    'F': 0.02228, 
    'G': 0.02015,
    'H': 0.06094, 
    'I': 0.06966, 
    'J': 0.00153, 
    'K': 0.00772, 
    'L': 0.04025, 
    'M': 0.02406, 
    'N': 0.06749,
    'O': 0.07507, 
    'P': 0.01929, 
    'Q': 0.00095, 
    'R': 0.05987, 
    'S': 0.06327, 
    'T': 0.09056,
    'U': 0.02758,
    'V': 0.00978, 
    'W': 0.02360,
    'X': 0.00150,
    'Y': 0.01974, 
    'Z': 0.00074,
}
lang_freq = defaultdict(float, eng_freq)
template_freq = defaultdict(float)


def read_file():
    text_result = ''
    filename = 'original_text.txt'
    file = open(filename, 'r')
    for line in file:
        text_result += line
    text_result = ''.join(filter(str.isalpha, text_result.upper()))
    return text_result


def write_to_file(mode):
    if mode == 'e':
        file = open('encrypt_text.txt', 'w')
        file.write(encrypt_text)
    else:
        file = open('decrypt_text.txt', 'w')
        file.write(decrypt_text)
    file.close()


def encrypt_symbol(i, encrypt_key):
 return alphabet[(alphabet.index(text[i]) + alphabet.index(encrypt_key[(i + 1) % len(encrypt_key)])) % len(alphabet)]
 

def Vigenere_encryption(encrypt_key):
    encrypt_result = ''
    for i in range(0, len(text)):
        encrypt_result = encrypt_result + encrypt_symbol(i, encrypt_key)
    return encrypt_result


def decrypt_symbol(i, decrypt_key):
    return alphabet[(alphabet.index(encrypt_text[i]) - alphabet.index([(i + 1) % len(decrypt_key)])) % len(alphabet)]


def Vigenere_decryption(decrypt_key):
    decrypt_result = ''
    for i in range(0, len(encrypt_text)):
        decrypt_result += decrypt_symbol(i, decrypt_key)
    return decrypt_result


def Kasiski_method():
    lgramms = defaultdict(list)
    l = 4
    while l < 7:  # while l < len(encrypt_text)/2
        for i in range(0, len(encrypt_text) - l):
            str = ''
            j = i + l
            str += encrypt_text[i:j]
            if str in l_gramms:
                lgramms[str].append(i - lgramms.get(str)[-1])
            else:
                lgramms[str].append(i)
        l += 1
    return lgramms


def GCD(x, y):
    gcd_value = 0
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if (x % i == 0) and (y % i == 0):
            gcd_value = i
    return gcd_value


def count_GCD():
    l_gramms_gcd_ = defaultdict(int)
    for l__key in l_gramms:
        if len(l_gramms[l__key]) != 1:
            for i in range(0, len(l_gramms[l__key]) - 1):
                gcd = GCD(l_gramms[l__key][i], l_gramms[l__key][i + 1])
                if gcd > 3:
                    l_gramms_gcd_[gcd] += 1
    print(sorted(l_gramms_gcd_.items(), key=lambda x: x[1], reverse=True))
    return l_gramms_gcd_


def count_template_frequency():
    temp_freq = defaultdict(int)
    for letter in encrypt_text:
        temp_freq[letter] += 1
    for key in lang_freq:
        template_freq[key] = temp_freq[key] / len(encrypt_text)


def shift(freq, j):
    return list(freq.values())[j:] + list(freq.values())[:j]


def chi_square():
    chis = [chisquare(shift(template_freq, i), list(lang_freq.values())).statistic for i in range(0, len(alphabet))]
    return chis.index(min(chis))


if __name__ == '__main__':
    alphabet = 'A, B, C ,D ,E, F, G, H, I, K, L, M, N ,O, P, Q, R, S, T, V, X, Y, Z '
    alphabet = alphabet.split(',')
    text = read_file()

    key = input('Input key: ')
    
    encrypt_text = Vigenere_encryption(key)
    write_to_file('e')

    decrypt_text = Vigenere_decryption(key)
    write_to_file('d')

    l_gramms = defaultdict(list)
    l_gramms = Kasiski_method()

    l_gramms_gcd = count_GCD()

    lists = sorted(l_gramms_gcd.items())
    x, y = zip(*lists)
    pyplot.plot(x, y)
    pyplot.show()
    count_template_frequency()

    key_shift = chi_square()
    key_length_variant = input('Input key length: ')
    shift(template_freq, key_length_variant)