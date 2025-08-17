def main():
    sentence=(input("what's your sentence? "))
    print(sentence)
    sentence=convert(sentence)
    print(sentence)

def convert(sentence):
    sentence=sentence.replace(":)","🙂")
    sentence=sentence.replace(":(","🙁")
    return sentence



main()



