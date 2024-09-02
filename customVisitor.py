from antlr4 import *
from TommyWiCVisitor import TommyWiCVisitor
from TommyWiCLexer import TommyWiCLexer
from TommyWiCParser import TommyWiCParser
from random import choice

memory = {}
ERROR_TEXT = ['What are these characters doing here?',
              'Are you crazy or something?',
              'What the hell is wrong with you!!',
              'Everything is going wrong',
              'Mom stop! It was Billy\'s mistake, just stop!',
              'A mistake? That he leases his body to addicted drug homos?',
              'Why not? What\'s wrong?',
              'You can help by telling me what\'s wrong with my zipper.',
              'What the hell is wrong with you!!',
              ]
ERROR = 'ERROR: ' + choice(ERROR_TEXT)

class customVisitor(TommyWiCVisitor):

    def var_checker(self, var):
        if var in memory:
            return True
        else:
            print(ERROR)

    def expression_checker(self, ctx):
        if isinstance(ctx.expression(), list):
            vs = [self.visit(expr) for expr in ctx.expression()]
        else:
            vs = [self.visit(ctx.expression())]

        exprs = []
        for i, val in enumerate(vs):
            if val in memory:
                exprs[i] = memory[val]
            else:
                try:
                    exprs.append(int(val))
                except ValueError:
                    print(ERROR)
                    return False
        return exprs

    def visitPrint_str(self, ctx: TommyWiCParser.Print_strContext):
        print(ctx.children[1].symbol.text[1:-1])
        return self.visitChildren(ctx)

    def visitPrint_expression(self, ctx: TommyWiCParser.Print_expressionContext):
        print(*self.expression_checker(ctx))

    def visitCondition_stmt(self, ctx: TommyWiCParser.Condition_stmtContext):
        condition_results = self.expression_checker(ctx)
        i = 1
        try:
            if condition_results[0]:
                return self.visit(ctx.statements(0))
            elif ctx.ELIF():
                while i < len(condition_results):
                    if condition_results[i]:
                        return self.visit(ctx.statements(i))
                    i += 1
            if ctx.ELSE():
                return self.visit(ctx.statements(i))
            else:
                return None
        except:
            print(ERROR)

    def visitWhile_stmt(self, ctx: TommyWiCParser.While_stmtContext):
        while self.visit(ctx.expression()):
            self.visit(ctx.statements())
        return None

    def visitDecrement(self, ctx: TommyWiCParser.DecrementContext):
        var = ctx.ID().symbol.text
        if self.var_checker(var):
            memory[var] -= 1
        return None

    def visitIncrement(self, ctx: TommyWiCParser.IncrementContext):
        var = ctx.ID().symbol.text
        if self.var_checker(var):
            memory[var] += 1
        return None

    def visitAnd(self, ctx: TommyWiCParser.AndContext):
        val1, val2 = self.expression_checker(ctx)
        return val1 and val2

    def visitOr(self, ctx: TommyWiCParser.OrContext):
        val1, val2 = self.expression_checker(ctx)
        return val1 and val2

    def visitNot(self, ctx: TommyWiCParser.NotContext):
        val = self.expression_checker(ctx)
        return not val[0]

    def visitNoteq(self, ctx: TommyWiCParser.NoteqContext):
        val1, val2 = self.expression_checker(ctx)
        return val1 != val2

    def visitLess(self, ctx: TommyWiCParser.LessContext):
        val1, val2 = self.expression_checker(ctx)
        return val1 < val2

    def visitVar_assign(self, ctx: TommyWiCParser.Var_assignContext):
        var = ctx.children[0].symbol.text
        val = self.visit(ctx.children[2])
        try:
            val = int(val)
        except:
            pass
        memory[var] = val
        return self.visitChildren(ctx)

    def visitVarexpr(self, ctx: TommyWiCParser.VarexprContext):
        # return self.expression_checker(ctx)[0]
        try:
            return memory[ctx.children[0].symbol.text]
        except Exception:
            print(ERROR)
            return None

    def visitNumberexpr(self, ctx: TommyWiCParser.NumberexprContext):
        # return self.expression_checker(ctx)[0]
        return ctx.children[0].symbol.text

    def visitTrueexpr(self, ctx: TommyWiCParser.TrueexprContext):
        return True

    def visitFalseexpr(self, ctx: TommyWiCParser.FalseexprContext):
        return False

    def visitOperations(self, ctx):
        return self.visitChildren(ctx)

    def visitTry_except(self, ctx: TommyWiCParser.Try_exceptContext):
        try:
            self.visit(ctx.operations(0))
        except:
            if ctx.operations(1):
                self.visit(ctx.operations(1))
            elif ctx.statements():
                self.visit(ctx.statements())


    def visitPlusop(self, ctx: TommyWiCParser.PlusopContext):
        var, val = self.expression_checker(ctx)
        memory[var] += val

    def visitMinusop(self, ctx: TommyWiCParser.MinusopContext):
        var, val = self.expression_checker(ctx)
        memory[var] -= val

    def visitMulop(self, ctx: TommyWiCParser.MulopContext):
        var, val = self.expression_checker(ctx)
        memory[var] *= val

    def visitDivop(self, ctx: TommyWiCParser.DivopContext):
        var, val = self.expression_checker(ctx)
        try:
            memory[var] /= val
        except ZeroDivisionError:
            print(ERROR)

# *******************************************************************
# *******************************************************************
# *******************************************************************
#
# def main():
#     input_text = """
#     Oh hi Mark
#     var is just a 99 CHEEP CHEEP CHEEP!
#     Yeah, you can say that again var
#     This is a great party, you invited all my friends
#     0 is great but var is a crowd
#     var is as good in bed as he is at getting promotions... Awful!
#     Yeah, you can say that again var
#     Everybody betray me. I'm fed up with this world!
#     What a story, Mark
#     """
#
#     input_stream = InputStream(input_text)
#     lexer = TommyWiCLexer(input_stream)
#     token_stream = CommonTokenStream(lexer)
#     parser = TommyWiCParser(token_stream)
#     tree = parser.program()
#
#     visitor = customVisitor()
#     visitor.visit(tree)
#
#
# if __name__ == '__main__':
#     main()
