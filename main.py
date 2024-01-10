# Effectuer une addition
def addition(a, b):
    return a + b

# Effectuer une soustraction
def soustraction(a, b):
    return a - b

# Effectuer une multiplication
def multiplication(a, b):
    return a * b

# Effectuer une division
def division(a, b):
    if b != 0:
        return round(a / b,2)
    else:
        return "Erreur: Division par zéro"

# Effectuer le calcul 
def calculatrice():
    print("Calculatrice")
    while True:
        # Mise en place d'un try except pour gérer les erreurs
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
