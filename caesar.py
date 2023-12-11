def caesar_solver(text:str, shift: int):
    '''Simple Caesar cipher encoder/decoder'''
    new_text = []
    for character in text:
        #Convert text to unicode and back to string
        shifted_char = chr((ord(character) + shift - 97) % 26 + 97)
        new_text.append(shifted_char)
    print(''.join(new_text))