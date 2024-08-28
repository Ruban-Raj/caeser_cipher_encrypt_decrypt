from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(direction, text, shift):
        shifted_text = ""
        
        if direction == "decode":
            shift *= -1
            
        for letter in text:
            if letter in alphabet:
                current_index = alphabet.index(letter)
                shift_index = current_index + shift
                shift_index %= len(alphabet)
                shifted_text += alphabet[shift_index]
            else:
                shifted_text += letter
            
        print(f'Here is the result of {direction}d: {shifted_text}')

game = True

while game == True:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    ceasar(direction=direction, shift=shift, text=text) 
    game_input = input('Type "yes" to continue the game. Otherwise, type "no"\n').lower()   
    if game_input == 'no':
        print("Good bye")
        game = False
    elif game_input == 'yes':
        game = True
    else:
        print("type a proper text. Game ended")
        game = False
         


