# graphNSI.py
from tkinter import Tk, Frame, Canvas, TOP, BOTH, YES

root = None
application = None
canvas = None
btnQuitter = None

# Dimensions de la fenêtre graphique
longueur = 1600
hauteur = 800


def init(titre):
    """Initialisation de la fenêtre graphique"""
    initDrawing(titre, 0, 0, longueur, hauteur)


def show():
    showDrawing()


def tracerRepere():
    minX = -longueur / 2
    maxX = longueur / 2
    minY = -hauteur / 2
    maxY = hauteur / 2
    tracerDroite(minX, 0, maxX, 0, 1)
    tracerDroite(0, minY, 0, maxY, 1)


def tracerRectangle(x1, y1, x2, y2, e):
    """
    Tracer un rectangle de coordonnées (x1,y1) (x2,y2) et d'épaisseur e (en pixels).
    Le repère est un repère orthonormé classique.

    y

    ˆ
    |
    (0,0) --> x

    """
    drawRect(
        x1 + (longueur / 2),
        hauteur / 2 - y1,
        x2 + (longueur / 2),
        hauteur / 2 - y2,
        e,
        0,
        0,
        0,
    )


def tracerDroite(x1, y1, x2, y2, e):
    """
    Tracer une droite de coordonnées (x1,y1) (x2,y2) et d'épaisseur e (en pixels).
    Le repère est un repère orthonormé classique.

    y

    ˆ
    |
    (0,0) --> x

    """
    drawLine(
        x1 + (longueur / 2),
        hauteur / 2 - y1,
        x2 + (longueur / 2),
        hauteur / 2 - y2,
        e,
        0,
        0,
        0,
    )


def tracerCercle(x1, y1, rayon, e):
    """
    Tracer un cercle de centre (x1,y1) et de rayon 'rayon' avec une épaisseur
    e (en pixels). Le repère est un repère orthonormé classique.

    y

    ˆ
    |
    (0,0) --> x
    """
    drawCircle(x1 + (longueur / 2), hauteur / 2 - y1, rayon, e, 0, 0, 0)


def initDrawing(titre, x, y, largeur, hauteur):
    """Définition d'une fenêtre graphique"""
    global root, application, canvas, btnQuitter
    root = Tk()
    root.geometry("{}x{}+{}+{}".format(largeur, hauteur, x, y))
    application = Frame(root, bg="white")
    application.pack(fill=BOTH, expand=YES)
    application.master.title(titre)

    canvas = Canvas(application, bg="white", highlightthickness=0)
    canvas.pack(side=TOP, fill=BOTH, expand=YES)


#    btnQuitter = Button(application, text="Quitter", command=root.destroy)
#    btnQuitter.pack(side=RIGHT)


def drawRect(x1, y1, x2, y2, epaisseur, rouge, vert, bleu):
    """Tracé d'un rectangle"""
    global canvas
    couleur = "#%02x%02x%02x" % (rouge, vert, bleu)
    canvas.create_rectangle(
        x1, y1, x2, y2, width=str(epaisseur), outline=couleur, fill=None
    )


def paintRect(x1, y1, x2, y2, rouge, vert, bleu):
    """Remplissage d'un rectangle"""
    global canvas
    couleur = "#%02x%02x%02x" % (rouge, vert, bleu)
    canvas.create_rectangle(x1, y1, x2, y2, outline=couleur, fill=couleur)


def drawCircle(x, y, rayon, epaisseur, rouge, vert, bleu):
    """Tracé d'un cercle"""
    global canvas
    couleur = "#%02x%02x%02x" % (rouge, vert, bleu)
    canvas.create_oval(
        x - rayon,
        y - rayon,
        x + rayon,
        y + rayon,
        width=str(epaisseur) + "p",
        outline=couleur,
        fill=None,
    )


def paintCircle(x, y, rayon, rouge, vert, bleu):
    """Remplissage d'un cercle (disque)"""
    global canvas
    couleur = "#%02x%02x%02x" % (rouge, vert, bleu)
    canvas.create_oval(
        x - rayon, y - rayon, x + rayon, y + rayon, outline=couleur, fill=couleur
    )


def drawPixel(x, y, rouge, vert, bleu):
    """Tracé d'un pixel"""
    global canvas
    couleur = "#%02x%02x%02x" % (rouge, vert, bleu)
    canvas.create_rectangle(x, y, x, y, outline=couleur)


def drawLine(x1, y1, x2, y2, epaisseur, rouge, vert, bleu):
    """Tracé d'un segment de droite"""
    global canvas
    couleur = "#%02x%02x%02x" % (rouge, vert, bleu)
    canvas.create_line(x1, y1, x2, y2, width=str(epaisseur) + "p", fill=couleur)


def drawText(x1, y1, texte, taille, rouge, vert, bleu):
    """Ecriture d'un texte"""
    global canvas
    couleur = "#%02x%02x%02x" % (rouge, vert, bleu)
    canvas.create_text(x1, y1, font=("Helvetica", taille), text=texte)


def showDrawing():
    """Affichage de la fenêtre graphique et attente de la fermeture"""
    global root
    root.mainloop()
