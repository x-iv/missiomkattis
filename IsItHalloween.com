Input_date = input().upper()
def i_i_h(date):
    month, day = date.split()

    hallo = "OCT 31"
    chris = "DEC 25"
    
    if date == hallo or date == chris:
        return "yup"
    else:
        return "nope"
print(i_i_h(Input_date))
