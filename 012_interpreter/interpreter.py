class Expression:
    def interpret(self, text): pass


class TerminalExpression(Expression):
    def __init__(self, word):
        self.word = word

    def interpret(self, text):
        words = text.split()
        if self.word in text:
            return True
        else:
            return False


class OrExpression(Expression):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def interpret(self, text):
        return self.exp1.interpret(text) or self.exp2.interpret(text)


class AndExpression(Expression):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def interpret(self, text):
        return self.exp1.interpret(text) and self.exp2.interpret(text)


evgeniy = TerminalExpression('Evgeniy')
katia = TerminalExpression('Katia')
kassiyan = TerminalExpression('Kassiyan')
vera = TerminalExpression('Vera')

rule1 = AndExpression(evgeniy, katia)
rule2 = OrExpression(kassiyan, rule1)
rule3 = AndExpression(vera, rule2)

print(rule3.interpret('Evgeniy'))
print(rule3.interpret('Vera Kassiyan'))

