from sympy import *
    
class LatexExpression:
    def __init__(self, expression):
        self.expression = expression
    
    def to_latex(self):
        return latex(self.expression)

    def to_img(self, filename):
        return preview(self.to_latex(), viewer='file', filename=f'outputs/{filename}')