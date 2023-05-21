import xlwt
import xlrd
wb = xlwt.Workbook()
ws = wb.add_sheet('Gene Ontology')
ws.write(0,0,'id')
ws.write(0,1,'name')
ws.write(0,2,'definition')
ws.write(0,3,'childnodes')
from xml.dom.minidom import parse
import xml.dom.minidom
DOMTree = xml.dom.minidom.parse('go_obo.xml')
terms = DOMTree.documentElement
terms1 = terms.getElementsByTagName("term")
for term in terms1:
    defs = term.getElementsByTagName("def")[0]
    defstr = defs.getElementsByTagName('defstr')[0]
    id = term.getElementsByTagName('id')[0]
    name = term.getElementsByTagName('name')[0]
    if'autophagosome'in defstr.childNodes[0].data:
       for i in enumerate(terms1):
          print('id:',id.childNodes[0].data)
          ws.write(i, 0, id.childNodes[0].data)
          print('name:',name.childNodes[0].data)
          ws.write(i, 1, name.childNodes[0].data)
          print('definition:',defstr.childNodes[0].data)
          ws.write(i, 2, defstr.childNodes[0].data)
          is_a = defs.getElementsByTagName('is_a')
          print('childnodes:', is_a.length)
          ws.write(i, 3, is_a.length)
          wb.save('Gene Ontology.xls')
