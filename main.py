# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import Gramatica as g
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

   #f = open("./entrada.txt", "r")
   #  input = f.read()
   #print(input)
   #parser.parse(input)
   fgraph = open('./Reportes/ast.dot', 'w+')  # creamos el archivo
   fgraph.write("graph \"\" {")
   fgraph.write("\tnode [style=filled];");
   fgraph.write("\tnode [shape = box];");
   fgraph.write("\tnode [fillcolor=\"cyan4\"];");
   fgraph.write("\tnode [color=\"#EE0000\"];");
   fgraph.write("\tedge [color=\"#31CEF0\"];\n");
   fgraph.close()
   g.parse()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
