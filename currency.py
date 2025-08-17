rates = {
    "USD": {"INR": 83.2, "EUR": 0.91},
    "INR": {"USD": 0.012, "EUR": 0.011},
    "EUR": {"USD": 1.1, "INR": 91.4},
}

def convert(amount, from_currency, to_currency):
    try:
        rate = rates[from_currency][to_currency]
        return amount * rate
    except KeyError:
        return None

amt = float(input("Enter amount: "))
frm = input("From currency (USD, INR, EUR): ").upper()
to = input("To currency (USD, INR, EUR): ").upper()

result = convert(amt, frm, to)
if result:
    print(f"{amt} {frm} = {result:.2f} {to}")
else:
    print("Conversion failed. Currency not supported.")

