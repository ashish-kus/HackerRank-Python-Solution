import sys
import xml.etree.ElementTree as etree

# def get_attr_number(node):
#     result=0
#     for element in node.iter():
#         result+=len(element.attribute)
#     return result
#     

# def get_attr_number(node):
#     # result=0
#     return len(element.attribute) for element in node.iter() 
def get_attr_number(node):
    return sum(len(element.attrib) for element in node.iter())

    


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
