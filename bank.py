def main():
    saudacao = input("Informe sua saudação: ").strip().lower()

    def output():
        if saudacao[:5] == "hello" : return print("$0")
        elif saudacao[0] == "h": return print("$20")
        else: return print("$100")
    output()

main()