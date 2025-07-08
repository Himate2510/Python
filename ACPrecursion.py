def get_input_for_negative():
    num = float(input("Enter a number: "))
    if num < 0:
        print("Negative number entered. Stopping.")
        return
    get_input_for_negative()
   
get_input_for_negative()
