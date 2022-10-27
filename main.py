import os


def define_env(env):
    "Hook function"

    @env.macro
    def initexo(n):
        env.variables["compteur_exo"] = n
        return ""

    env.variables["compteur_exo"] = 0

    @env.macro
    def exercice():
        env.variables["compteur_exo"] += 1
        return f"Exercice  { env.variables['compteur_exo']}"

    @env.macro
    def correction(bool, texte):
        if bool == False:
            return ""
        else:
            return texte
