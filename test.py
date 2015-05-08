from tp_html.py import *

def load_test_file(filename):
    with open('in_files/' + filename, mode='r') as fd:
        content = fd.read()

        return content


def test_get_elements(content):

   print(get_elements(content, ['a','h1']))

def test_table_matieres(content):
    
    print(table_matieres(content, 3))
    print(table_matieres(content, 2))

   

def test_remove_links(content):
    
    print(remove_links(content))
    

print("Tests des fonctions avec le fichier test numéro 1 :")
load_test_file(test1.html)

test_get_elements(content)

test_table_matieres(content)

test_remove_links(content)

print("Tests des fonctions avec le fichier test numéro 2 :")  

load_test_file(test2.html)

test_get_elements(content)

test_table_matieres(content)

test_remove_links(content)
