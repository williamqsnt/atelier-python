# Fonction pour calculer une addition
def addition(a, b):
    return a + b

# Fonction pour calculer une soustraction
def soustraction(a, b):
    return a - b



def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur: Division par zéro"

def calculatrice():
    print("Calculatrice de base en Python")
    while True:
        try:
            a = float(input("Entrez le premier nombre: "))
            operation = input("Entrez l'opération (+, -, *, /): ")
            b = float(input("Entrez le deuxième nombre: "))

            if operation == '+':
                resultat = addition(a, b)
            elif operation == '-':
                resultat = soustraction(a, b)
            elif operation == '*':
                resultat = multiplication(a, b)
            elif operation == '/':
                resultat = division(a, b)
            else:
                print("Opération non valide.")
                continue

            print("Résultat: ", resultat)

        except ValueError:
            print("Erreur: Veuillez entrer des nombres valides.")

if __name__ == "__main__":
    calculatrice()
