import re


def convert_abbreviations(string):
    string = re.sub(r'NFT', 'Nft', string)
    string = re.sub(r'SPL', 'Spl', string)

    return string

def to_snake(string):
    string = convert_abbreviations(string)

    string = re.sub('([A-Z][a-z]+)', r' \1',
                    re.sub('([A-Z]+)', r' \1',
                           string.replace('-', ' ')))
    
    out = '_'.join(string.split()).lower()

    return out
