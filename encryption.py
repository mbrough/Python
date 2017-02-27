import random

# Generates and returns a random key
def keyGen(alpha):      
        key = ""
        for i in range(len(alpha)):
            index = random.randint(0, 25-i)
            key = key + alpha[index]
            alpha = alpha[:index] + alpha[index+1:]
        return key

# Encrypts plaintext using a random key and a Caeser cipher
def caeser(plainText) :
# header for function caesar that takes plainText as an argument
        alphabet = ("abcdefghijklmnopqrstuvwxyz")
        key = keyGen("abcdefghijklmnopqrstuvwxyz")
        print("Random key: ")
        print(alphabet)
        print(key)
        #convert plainText to all lowercase letters
        plainText = plainText.lower()
        cipherText = ""
        for ch in plainText:
            idx = alphabet.find(ch)
            # if index is positive
            if idx >= 0 :
                    # append to cipherText a character sitting in key[idx]
                    cipherText = cipherText + str(key[idx])
            # else if index is negative but ch is a digit
            elif idx < 0 and ch.isdigit() :
                    # append that digit to cipherText
                    cipherText = cipherText + str(ch)
            # else if index is negative but ch is not a digit
            elif idx < 0 and not ch.isdigit() :
                    # append a blank to cipherText
                    cipherText = cipherText + " "
                    
        return cipherText

# Encrypts plaintext using transposition cipher
def trans(plainText):
        # extract all chars sitting in even positions into evenChars string
        evenChars = plainText[::2]

        # extract all chars sitting in odd positions into oddChars string
        oddChars = plainText[1::2]
        
        cipherText = oddChars + evenChars
        return cipherText

# Encrypts plaintext using ASCII shift
def ascii_shift(plainText):
        shift = random.randint(1, 25)
        print("Shift: ", shift)
        # construct and return cipherText as plainText in which
        # each char is replaced with old char + shift (look up chr and ord functions)
        plainText = plainText.lower()
        cipherText = ""
        for ch in plainText :
                cipherText = cipherText + chr(7 + ord(ch))
        return cipherText
# Driver
def my_main():
        # prompt for a phrase, store results into variable msg
        msg = input("Enter a message to encrypt:")

        print('Which encryption do you want to use?')
        choice = input('Enter 1 for random Caeser cipher, 2 for transposition, 3 for an ASCII shift: ')
        if choice.isdigit():
                int_choice = int(choice)

        # while statement that is entered if choice contains more than just digits
        # or int_choice is not within the range [1, 3] 
        while not choice.isdigit() or int_choice < 1 or int_choice > 3 :

                print('Invalid input - try again')
                choice = input('Enter 1 for random Caeser cipher, 2 for transposition, 3 for an ASCII shift: ')
                if choice.isdigit():
                        int_choice = int(choice)

        # based on the user's choice (1, 2 or 3)  call appropriate encryption function and
        # store the result into variable cipherText
        if int_choice is 1 :
                # random caeser cipher
                cipherText = caeser(msg)
        elif int_choice is 2 :
                #transposition
                cipherText = trans(msg)
        elif int_choice is 3 :
                #ASCII shift
                cipherText = ascii_shift(msg)
                
        print('The encrypted message is: ', cipherText)

        # loop to repeat program if desired
        char_input = input('Repeat? Enter y to repeat or q to quit: ')
        while (char_input is not "y") and (char_input is not "q") :
                print("Invalid Selection.")
                char_input = input('Repeat? Enter y to repeat or q to quit: ')
        if char_input is "y" :
                my_main()
        elif char_input is "q":
                return
        
if __name__ == '__main__':
        my_main()

        
    
    


