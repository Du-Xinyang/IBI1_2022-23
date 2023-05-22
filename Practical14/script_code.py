from openpyxl.workbook import Workbook
from xml.dom.minidom import parse
import xml.dom.minidom
import pandas as pd
DOMTree = xml.dom.minidom.parse('go_obo.xml')
terms = DOMTree.documentElement
terms1 = terms.getElementsByTagName("term")
ids, names, childNodes, defstrs = [], [], [], []
# count the number of nodes
def find_is_a(go_id):
    child_nodes = []
    for term in terms1:
        is_as = term.getElementsByTagName('is_a')
        for is_a in is_as:
            if go_id == is_a.childNodes[0].data:
                child_nodes.append(term.getElementsByTagName('id')[0].childNodes[0].data)
                child_nodes += find_is_a(term.getElementsByTagName('id')[0].childNodes[0].data)
    return child_nodes
# create the excel sheet
for term in terms1:
    defs = term.getElementsByTagName("def")[0]
    defstr = defs.getElementsByTagName('defstr')[0]
    id = term.getElementsByTagName('id')[0]
    name = term.getElementsByTagName('name')[0]
    if'autophagosome'in defstr.childNodes[0].data:
       ids.append(id.childNodes[0].data)
       names.append(name.childNodes[0].data)
       defstrs.append(defstr.childNodes[0].data)
       childNodes.append(len(find_is_a(id.childNodes[0].data)))
df = pd.DataFrame({'id': ids, 'name': names, 'definition': defstrs, 'childnodes': childNodes})
df.to_excel('Gene-Ontology.xlsx', index=False)
