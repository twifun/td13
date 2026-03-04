import numpy as np

def rectangles_gauche(f, a, b, n):
    """
    I_gauche = rectangles_gauche(props['func'], props['a'], props['b'], n_test)
    Méthode des rectangles à gauche
    Paramètres :
    -----------
    f : fonction à intégrer
    a, b : bornes de l'intervalle
    n : nombre de subdivisions
    Retourne :
    ---------
    Approximation de l'intégrale
    """
    h = (b - a) / n
    x = np. linspace (a, b - h, n)
    # Points à gauche de chaque subdivision
    return h * np.sum(f(x))

def rectangles_droite(f, a, b, n):
    """
    Méthode des rectangles à droite
    Paramètres :
    -----------
    f : fonction à intégrer
    a, b : bornes de l'intervalle
    n : nombre de subdivisions
    Retourne :
    ---------
    Approximation de l'intégrale
    """
    h = (b - a) / n
    x = np. linspace(a + h, b, n)
    # Points à gauche de chaque subdivision
    return h * np.sum(f(x))
def rectangles_milieu(f, a, b, n):
    """
    Méthode des rectangles à droite
    Paramètres :
    -----------
    f : fonction à intégrer
    a, b : bornes de l'intervalle
    n : nombre de subdivisions
    Retourne :
    ---------
    Approximation de l'intégrale
    """
    h = (b - a) / n
    x = np. linspace(a + h/2, b-h/2, n)
    # Points à gauche de chaque subdivision
    return h * np.sum(f(x))

def trapeze(f, a, b, n):
    """
    Méthode des trapèzes
    Paramètres :
    -----------
    f : fonction à intégrer
    a, b : bornes de l'intervalle
    n : nombre de subdivisions
    Retourne :
    ---------
    Approximation de l'intégrale
    """
    h = (b - a) / n
    x = np. linspace(a, b, n+1)
    # Points à gauche de chaque subdivision
    return h/2 * (f(x[0]) + 2*np.sum(f(x[1:-1])) + f(x[-1]))

def simpson(f, a, b, n):
    """
    Méthode de Simpson
    Paramètres :
    -----------
    f : fonction à intégrer
    a, b : bornes de l'intervalle
    n : nombre de subdivisions
    Retourne :
    ---------
    Approximation de l'intégrale
    """
    h = (b - a) / n
    x = np. linspace(a, b, n+1)
    # Points à gauche de chaque subdivision
    return h/3 * (f(x[0]) + 4*np.sum(f(x[1:-1:2]))+ 2*np.sum(f(x[2:-1:2])) + f(x[-1]))