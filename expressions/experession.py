import sympy
class LatexExpression:
    def __init__(self, expression):
        self.expression = experssion 
    
    def convert_latex(self):
        return sympy.latex(eval(s))