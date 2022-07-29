# создается строка из чисел и потом его херачит как только можно
print("Hi, I am professionally mocking your text :)")
text = input("Enter your text more than 8 characters")
if len(text) <=7:
    print("-----------------------------------------------------------")
    print("| >>> Error! You have entered less than 8 characters. <<< |")
    print("-----------------------------------------------------------")
else:
    #1
    print("|1. Fifth character of the string:|")
    print(">>>", text[4])
    #2
    print("|2. The last symbol:|")
    print(">>>", text[-1])
    #3
    print("|3. All but the last 4 characters:|")
    print(">>>", text[0:-4])
    #4
    print("|4. Latest 7 characters:|")
    print(">>>", text[-8:-1])
    #5
    print("|5. Symbols that are in even places:|")
    print(">>>", text[0:len(text):2])
    #6
    print("|6. Symbols on odd places:|")
    print(">>>", text[1:len(text):2])
    #7
    print("|7. Whole line in reverse order:|")
    print(">>>", text[-1:-(len(text) + 1):-1])
    #8
    print("|8. All through one:|")
    print(">>>", text[0:len(text):2])
    #9
    print("|9. All characters through two in reverse order:|")
    print(">>>", text[-1:-(len(text) + 1):-3])
    #10
    print("|10. We change the left and right halves to the place:|")
    print(">>>", text[(len(text) + 1) // 2:] + text[:(len(text) + 1) // 2])
    print("-------------------------------------")
    print("*** Thank you for your attention! ***")
    print("-------------------------------------")


