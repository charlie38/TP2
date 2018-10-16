#######
# TP2 #
#######

from graphe import Graphe

# Les fonctions dont la documentation contient OBLIGATOIRE sont nécessaires
# pour avoir le point du TP.
# Les fonctions dont le nom est suivi de "# *" sont plus difficiles.
# Les exemples donnés servent aussi de tests unitaires si le fichier est
# exécuté.

# Comment faire le TP :
# - Copiez l'INTÉGRALITÉ de ce fichier dans votre éditeur de texte favori
# - Complétez les fonctions en remplaçant la ligne "pass" par le contenu adéquat
# Mettez votre code APRÈS les docstrings, pas avant, autrement, les tests
# unitaires ne fonctionneront pas !
# - Lorsque vous pensez avoir terminé une fonction, exécutez le fichier sur
# votre machine et vérifiez que les tests unitaires passent. Si ce n'est pas le
# cas, corrigez votre fonction
# - Lorsque les tests unitaires passent pour une fonction, faites un
# copier-coller du fichier complet sur Caseine dans l'onglet "Edit", sauvegardez
# et vérifiez que cela fonctionne sur Caseine avec le bouton "Evaluate"

# Pour ce TP, une classe pour manipuler les graphes vous est fournie. Vous
# n'avaez pas besoin de comprendre comment elle est implémentée, mais vous
# devez comprendre comment l'utiliser. Pour cela, lisez les docstrings et les
# exemples donnés dans le fichier graphe.py. La première partie du TP sert en
# partie à se familiariser avec la classe Graphe.

####################################
# Manipulation de la classe Graphe #
####################################

def graphe_1():
    """Retourne le graphe G1.

        -------------------
        --- OBLIGATOIRE ---
        -------------------

           4
         /   \
        0 --- 1    G1
        |     |
        3 --- 2

        :Examples:

        >>> graphe_1()
        {5: 0--1 0--3 0--4 1--2 1--4 2--3}

    """

    g=Graphe(5,[ (0,1), (0,3), (0,4), (1,2), (1,4), (2,3) ])
    return g

def graphe_2():
    """Retourne le graphe G2.

        -------------------
        --- OBLIGATOIRE ---
        -------------------

             2
        3---/-\---1
         \ 4   0 /    G2
          \ \ / /
           \ 6 /
            \ /
             5

        :Examples:

        >>> graphe_2()
        {7: 0--2 0--6 1--3 1--5 2--4 3--5 4--6}

    """

    g=Graphe(7,[ (0,2), (0,6), (1,3), (1,5), (2,4), (3,5), (4,6) ])
    return g

def graphe_complet(n):
    """Retourne un graphe complet à n sommet.

        -------------------
        --- OBLIGATOIRE ---
        -------------------

        :param n: Nombre de sommets, entier naturel

        :Examples:

        >>> graphe_complet(3)
        {3: 0--1 0--2 1--2}
        >>> graphe_complet(4)
        {4: 0--1 0--2 0--3 1--2 1--3 2--3}

    """

    g=Graphe(n)
    for i in range(n):
        for j in range(n):
            if (i!=j) and (i<j):
                g.ajouter_arete(i,j)
    return g

def cycle(n):
    """Retourne un cycle à n sommet.

        -------------------
        --- OBLIGATOIRE ---
        -------------------

        :param n: Nombre de sommets, entier naturel >= 3

        :Examples:

        >>> cycle(4)
        {4: 0--1 0--3 1--2 2--3}
        >>> cycle(5)
        {5: 0--1 0--4 1--2 2--3 3--4}

    """

    g=Graphe(n, [(0,1),(0,n-1)])
    for i in range(1,n-1):
        g.ajouter_arete(i,i+1)
    return g

def graphe_complementaire(g): # *
    """Retourne le graphe complémentaire de g.

        Retourne un graphe g_comp tel que toute arête de g n'est pas une arête
        de g_comp et toute arête de g_comp n'est pas une arête de g.

        :param g: un graphe (Graphe)

        :Examples:

        >>> graphe_complementaire(graphe_complet(4))
        {4:}
        >>> graphe_complementaire(graphe_1())
        {5: 0--2 1--3 2--4 3--4}

    """

def degre(g, v):
    """Retourne le degré du sommet d'indice v du graphe g.

        -------------------
        --- OBLIGATOIRE ---
        -------------------

        :param g: Un graphe (Graphe)
        :param v: Un indice d'un sommet de g, entier naturel compris entre 0 et
        g.nombre_sommets()-1

        :Examples:

        >>> g = graphe_1()
        >>> degre(g, 0)
        3
        >>> degre(g, 2)
        2

    """

    res=len(g.voisins(v))
    return res

def degre_max(g):
    """Retourne le degré maximum du graphe g.

        -------------------
        --- OBLIGATOIRE ---
        -------------------

        :param g: Un graphe (Graphe)

        :Examples:

        >>> degre_max(Graphe(10))
        0
        >>> degre_max(graphe_1())
        3
        >>> degre_max(graphe_2())
        2
        >>> degre_max(graphe_complet(5))
        4
        >>> degre_max(cycle(10))
        2

    """

    res=-1
    for i in range(g.nombre_sommets()):
        degre=len(g.voisins(i))
        if degre>res:
            res=degre
    return res

def nombre_aretes(g):
    """Retourne le nombre d'arêtes du graphe g.

        -------------------
        --- OBLIGATOIRE ---
        -------------------

        :param g: Un graphe (Graphe)

        :Examples:

        >>> nombre_aretes(Graphe(10))
        0
        >>> nombre_aretes(graphe_1())
        6
        >>> nombre_aretes(graphe_2())
        7
        >>> nombre_aretes(graphe_complet(5))
        10
        >>> nombre_aretes(cycle(10))
        10

    """

    res=0
    for i in range(g.nombre_sommets()):
        num_voisins=len(g.voisins(i))
        res=res+num_voisins
    res=res/2
    return int(res)

def matrice_adjacence(g):
    """Retourne la matrice d'adjacence du graphe g.

        :param g: Un graphe (Graphe)
        :return: Une matrice (liste de listes)

        :Examples:

        >>> for l in matrice_adjacence(Graphe(3)): print(*l)
        0 0 0
        0 0 0
        0 0 0
        >>> for l in matrice_adjacence(graphe_1()): print(*l)
        0 1 0 1 1
        1 0 1 0 1
        0 1 0 1 0
        1 0 1 0 0
        1 1 0 0 0
        >>> for l in matrice_adjacence(graphe_2()): print(*l)
        0 0 1 0 0 0 1
        0 0 0 1 0 1 0
        1 0 0 0 1 0 0
        0 1 0 0 0 1 0
        0 0 1 0 0 0 1
        0 1 0 1 0 0 0
        1 0 0 0 1 0 0
        >>> for l in matrice_adjacence(graphe_complet(4)): print(*l)
        0 1 1 1
        1 0 1 1
        1 1 0 1
        1 1 1 0
        >>> for l in matrice_adjacence(cycle(5)): print(*l)
        0 1 0 0 1
        1 0 1 0 0
        0 1 0 1 0
        0 0 1 0 1
        1 0 0 1 0

    """

    # Créer une liste de i liste comportant j 0.
    # mat = [[0]*j for i in range(0,i)]

def matrice_incidence(g):
    """Retourne la matrice d'incidence du graphe g.

        :param g: Un graphe (Graphe)
        :return m: Une matrice (liste de listes)

        :Examples:

        >>> for l in matrice_incidence(Graphe(3)): print(*l)
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        >>> for l in matrice_incidence(graphe_1()): print(*l)
        1 1 1 0 0 0
        1 0 0 1 1 0
        0 0 0 1 0 1
        0 1 0 0 0 1
        0 0 1 0 1 0
        >>> for l in matrice_incidence(graphe_2()): print(*l)
        1 1 0 0 0 0 0
        0 0 1 1 0 0 0
        1 0 0 0 1 0 0
        0 0 1 0 0 1 0
        0 0 0 0 1 0 1
        0 0 0 1 0 1 0
        0 1 0 0 0 0 1
        >>> for l in matrice_incidence(graphe_complet(4)): print(*l)
        1 1 1 0 0 0
        1 0 0 1 1 0
        0 1 0 1 0 1
        0 0 1 0 1 1
        >>> for l in matrice_incidence(cycle(5)): print(*l)
        1 1 0 0 0
        1 0 1 0 0
        0 0 1 1 0
        0 0 0 1 1
        0 1 0 0 1

    """


############
# Parcours #
############


def liste_voisins(g,u):
#retourne la liste de voisins du sommet u dans le graphe g
    res=[]
    for v in g.voisins(u):
        res.append(v)
    return res

def deja_vu(elt,liste):
#retourne True si elt est dans liste
    i=0
    while i<len(liste):
        if liste[i]==elt:
            return True
        i=i+1
    return False

def parcours_rec(g,u,parcourus,parcours):
#parcours les voisins du sommet u et retourne la liste parcourus modifiées
    parcourus.append(u)
    voisins=liste_voisins(g,u)
    for i in voisins:
        if not(deja_vu(i,parcourus)):
            parcourus=parcourus+parcours_rec(g,i,parcourus,parcours)
            parcours.append(i)
    return parcourus

def parcours_postfixe(g, u):
    """Affiche la liste des sommets dans l'ordre dans lequel ils sont traités
    lors d'un parcours postfixé du graphe g en partant du sommet u.

        -------------------
        --- OBLIGATOIRE ---
        -------------------

        :param g: Un graphe (Graphe)

        :Examples:

        >>> parcours_postfixe(graphe_1(), 0)
        3 2 4 1 0
        >>> parcours_postfixe(graphe_1(), 1)
        2 3 4 0 1
        >>> parcours_postfixe(graphe_2(), 0)
        6 4 2 0
        >>> parcours_postfixe(graphe_2(), 1)
        5 3 1
        >>> parcours_postfixe(graphe_complet(5), 0)
        4 3 2 1 0
        >>> parcours_postfixe(cycle(7), 1)
        2 3 4 5 6 0 1

    """

    res=str()
    parcourus=[]
    parcours=[]
    parcourus=parcours_rec(g,u,parcourus,parcours)
    for i in range(len(parcours)):
        res+=str(parcours[i])+" "
    res+=str(u)
    print(res)

# Pour le parcours en largeur, il est nécessaire d'utiliser une file.
# Vous devez donc implémenter les fonctions creer_file, enfiler, defiler et
# est_vide.
# La file est implémentée sous forme d'un tableau avec deux compteurs, un qui
# mémorise le début de la file, l'autre la fin.
# C'est donc une liste de 3 éléments [[e1, e2], debut, fin].
# Notez que les éléments ne sont en pratique pas supprimés de la file. Seul le
# compteur de début est incrémenté lors de l'opération defiler.

def creer_file(n):
    """Retourne une file (File) dont le nombre d'éléments est <= n.

        -------------------
        --- OBLIGATOIRE ---
        -------------------

        :param n: nombre maximum d'éléments ajoutés à la file.

        :Examples:

        >>> creer_file(3)
        [[-1, -1, -1], 0, -1]

    """

def enfiler(f, e):
    """Ajoute un élément à la fin de la file f.

        -------------------
        --- OBLIGATOIRE ---
        -------------------

        :param f: une file (File)
        :param e: élément à ajouter à la file

        :Examples:

        >>> f = creer_file(3)
        >>> f
        [[-1, -1, -1], 0, -1]

        >>> enfiler(f, 2)
        >>> f
        [[2, -1, -1], 0, 0]

        >>> enfiler(f, 3)
        >>> f
        [[2, 3, -1], 0, 1]

    """

def defiler(f):
    """Supprime et retourne le premier élément de la file f.

        -------------------
        --- OBLIGATOIRE ---
        -------------------

        :param f: une file (File)

        :Examples:

        >>> f = creer_file(4)
        >>> enfiler(f, 2)
        >>> enfiler(f, 3)
        >>> enfiler(f, 5)
        >>> f
        [[2, 3, 5, -1], 0, 2]

        >>> defiler(f)
        2
        >>> defiler(f)
        3
        >>> defiler(f)
        5
        >>> f
        [[2, 3, 5, -1], 3, 2]

    """

def est_vide(f):
    """Renvoie True si la file f est vide.

        -------------------
        --- OBLIGATOIRE ---
        -------------------

        :param f: une file

        :Examples:

        >>> f = creer_file(4)
        >>> est_vide(f)
        True
        >>> enfiler(f, 2)
        >>> est_vide(f)
        False
        >>> defiler(f)
        2
        >>> est_vide(f)
        True

    """

def parcours_largeur(g, u):
    """Affiche la liste des sommets dans l'ordre dans lequel ils sont traités
    lors d'un parcours en largeur du graphe g en partant du sommet u.

        -------------------
        --- OBLIGATOIRE ---
        -------------------

        :param g: Un graphe (Graphe)
        :param u: Indice d'un sommet de g, entier naturel compris entre 0 et n-1

        :Examples:

        >>> parcours_largeur(graphe_1(), 0)
        0 1 3 4 2
        >>> parcours_largeur(graphe_1(), 1)
        1 0 2 4 3
        >>> parcours_largeur(graphe_2(), 0)
        0 2 6 4
        >>> parcours_largeur(graphe_2(), 1)
        1 3 5
        >>> parcours_largeur(graphe_complet(5), 0)
        0 1 2 3 4
        >>> parcours_largeur(cycle(7), 1)
        1 0 2 6 3 5 4

    """

def parcours_prefixe(g, u):
    """Affiche la liste des sommets dans l'ordre dans lequel ils sont traités
    lors d'un parcours préfixé du graphe g en partant du sommet u.

        :param g: Un graphe (Graphe)

        :Examples:

        >>> parcours_prefixe(graphe_1(), 0)
        0 1 2 3 4
        >>> parcours_prefixe(graphe_1(), 1)
        1 0 3 2 4
        >>> parcours_prefixe(graphe_2(), 0)
        0 2 4 6
        >>> parcours_prefixe(graphe_2(), 1)
        1 3 5
        >>> parcours_prefixe(graphe_complet(5), 0)
        0 1 2 3 4
        >>> parcours_prefixe(cycle(7), 1)
        1 0 6 5 4 3 2

    """

def est_connexe(g):
    """Retourne True si g est connexe, False sinon.

        :param g: Un graphe (Graphe)

        :Examples:

        >>> est_connexe(graphe_1())
        True
        >>> est_connexe(graphe_2())
        False
        >>> est_connexe(graphe_complet(5))
        True
        >>> est_connexe(Graphe(1))
        True
        >>> est_connexe(Graphe(5))
        False

    """

def nombre_composantes_connexes(g):
    """Retourne le nombre de composantes connexes de g.

        :param g: Un graphe (Graphe)

        :Examples:

        >>> nombre_composantes_connexes(graphe_1())
        1
        >>> nombre_composantes_connexes(graphe_2())
        2
        >>> nombre_composantes_connexes(graphe_complet(5))
        1
        >>> nombre_composantes_connexes(Graphe(1))
        1
        >>> nombre_composantes_connexes(Graphe(5))
        5

    """


###############################
# Chemins et cycles eulériens #
###############################

def a_cycle_eulerien(g):
    """Retourne True si g admet un cycle eulérien, False sinon.

        :param g: Un graphe (Graphe)

        :Examples:

        >>> a_cycle_eulerien(graphe_1())
        False
        >>> a_cycle_eulerien(graphe_2())
        False
        >>> a_cycle_eulerien(graphe_complet(4))
        False
        >>> a_cycle_eulerien(graphe_complet(5))
        True
        >>> a_cycle_eulerien(cycle(4))
        True
        >>> a_cycle_eulerien(Graphe(5))
        False

    """

def a_chemin_eulerien(g):
    """Retourne True si g admet un chemin eulérien, False sinon.

        :param g: Un graphe (Graphe)

        :Examples:

        >>> a_chemin_eulerien(graphe_1())
        True
        >>> a_chemin_eulerien(graphe_2())
        False
        >>> a_chemin_eulerien(graphe_complet(2))
        True
        >>> a_chemin_eulerien(graphe_complet(4))
        False
        >>> a_chemin_eulerien(graphe_complet(5))
        True
        >>> a_chemin_eulerien(cycle(4))
        True
        >>> a_chemin_eulerien(Graphe(5))
        False

    """

def promenade(g, u):
    """Retourne le chemin élémentaire obtenu en parcourant g depuis le sommet
    d'indice u en choisissant la première arête disponible jusqu'à ce qu'il n'y
    en aie plus de disponible.
    Les arêtes parcourues sont supprimées de g.

        :param g: Un graphe (Graphe)

        :Examples:

        >>> g = graphe_1()
        >>> promenade(g, 0)
        [0, 1, 2, 3, 0, 4, 1]
        >>> g
        {5:}

        >>> g = graphe_1()
        >>> promenade(g, 4)
        [4, 0, 1, 2, 3, 0]
        >>> g
        {5: 1--4}

        >>> g = graphe_2()
        >>> promenade(g, 0)
        [0, 2, 4, 6, 0]
        >>> g
        {7: 1--3 1--5 3--5}

        >>> g = graphe_2()
        >>> promenade(g, 1)
        [1, 3, 5, 1]
        >>> g
        {7: 0--2 0--6 2--4 4--6}

    """

def graphe_3():
    """Retourne le graphe G3.

          1   7   4
         / \ / \ / \
        0   2   8   5
         \ / \ / \ /
          3   9   6

        :Examples:

        >>> graphe_3()
        {10: 0--1 0--3 1--2 2--3 2--7 2--9 4--5 4--8 5--6 6--8 7--8 8--9}

    """

    return Graphe(10, [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (2, 7), (7, 8), (8, 9), (9, 2),
        (8, 4), (4, 5), (5, 6), (6, 8)])

def cycle_eulerien(g, u=0): # *
    """Retourne un cycle eulérien de g en partant du sommet u.

        :param g: Un graphe (Graphe) eulérien
        :param u: L'indice d'un sommet de g, entier naturel compris entre 0 et
        g.nombre_sommets()-1

        :Examples:

        >>> c = cycle_eulerien(graphe_3())
        >>> g = graphe_3()
        >>> g.supprimer_chemin(c)
        >>> g
        {10:}

        >>> c = cycle_eulerien(cycle(4))
        >>> g = cycle(4)
        >>> g.supprimer_chemin(c)
        >>> g
        {4:}

        >>> c = cycle_eulerien(graphe_complet(5))
        >>> g = graphe_complet(5)
        >>> g.supprimer_chemin(c)
        >>> g
        {5:}
    """

def chemin_eulerien(g): # *
    """Retourne un chemin eulérien de g en partant du sommet u.

        :param g: Un graphe (Graphe) contenant un chemin eulérien

        :Examples:

        >>> c = chemin_eulerien(graphe_1())
        >>> g = graphe_1()
        >>> g.supprimer_chemin(c)
        >>> g
        {5:}

        >>> c = chemin_eulerien(graphe_3())
        >>> g = graphe_3()
        >>> g.supprimer_chemin(c)
        >>> g
        {10:}

        >>> c = chemin_eulerien(cycle(4))
        >>> g = cycle(4)
        >>> g.supprimer_chemin(c)
        >>> g
        {4:}

        >>> c = chemin_eulerien(graphe_complet(5))
        >>> g = graphe_complet(5)
        >>> g.supprimer_chemin(c)
        >>> g
        {5:}

    """


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.FAIL_FAST)
