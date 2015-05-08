from csudoci.html.parser import html_to_tree
from csudoci.html.manip import get_links_as_ul

from csudoci.html.manip import get_links_as_ul, get_links_as_ul2


def get_elements(tree, selector):
    
    '''
    Auteur: Stéphane Menoud
    =======================
    
    Fonction:
    =========
    get_elements() construit une liste des sous-arbres de tree possédant pour racine une balise figurant dans la liste selector.
    
    Paramètres:
    ===========
    tree : il s'agit de l'arbre HTML sur lequel la fonction va travailler
    selector : il s'agit d'une liste de chaînes de caractères qui correspondent aux balises à extraire de l'arbre

    Sortie:
    =======
    Il en ressort la liste des éléments extraits de l'arbre.

    '''
    element = []
    root = tree
    
    if root.tag in selector:
        element.append(tree)
    else:
        for c in tree.children:
            element += get_elements(c, selector)

    return element
    
    
    
    
    
    


def table_matieres(tree, level):
    
    '''
    Auteur: Stéphane Menoud
    =======================
    
    Fonction:
    ========
    html_tree() prend un arbre HTML et construit un arbre HTML représentant une table des matières sur la base des balises <h1>, <h2>, etc ...
    
    Paramètres:
    ==========
    tree : il s'agit de l'arbre HTML sur lequel la fonction va travailler
    level : il s'agit d'une indication qui correspond au niveau maximum de titre que la fonction doit prendre en compte pour construire la table des matières (ex. 3 : <h1>, <h2>, <h3>)

    Sortie:
    =======
    Arbre html

    '''
    titletags = ['h1', 'h2','h3', 'h4', 'h5', 'h6'] #les éléments h peuvent aller au maximum jusqu'à h6
    
    titletags_list = get_elements(tree, titletags[:level])

    return titletags_list
    
    
    
    
    
    
    
    

def remove_links(tree):
    
    '''
    Auteur: Stéphane Menoud
    =======================
    
    Fonction:
    ========
    html_tree() prend un arbre HTML en paramètre et en retire ensuite tous les liens tout en conservant le texte se trouvant entre les balises des liens.
    
    Paramètres:
    ==========
    tree : Il s'agit de l'arbre sur lequel la fonction va effectuer son action


    Sortie:
    =======
    Il en ressort un arbre HTML dont les liens ont été retiré.
    '''

    
    for element in tree.children:
        remove_links(element)
    
    if tree.tag == 'a' and tree.parent != None:
        children = tree.children
        
        
        closechildren = tree.parent.children #closechildren équivaut à l'ensemble des enfants du parent du lien que l'on va retirer
        linklocation = 0
        
        while closechildren[linklocation].tag != 'a':
            linklocation += 1
            
        closechildren = closechildren[:linklocation] + tree.children + closechildren[linklocation:]
            

            
    return remove_links(tree)