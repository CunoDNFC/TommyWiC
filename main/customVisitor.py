from grammar.TommyWiCVisitor import TommyWiCVisitor
from grammar.TommyWiCParser import TommyWiCParser
from grammar.TommyWiCLexer import TommyWiCLexer
from antlr4 import InputStream, CommonTokenStream
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

        for val in vs:
            if val in memory:
                exprs.append(memory[val])
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
        if not 'END' not in ctx.getText() or ctx.END() is None:
            raise SyntaxError("Expected END statement")

        while self.visit(ctx.expression()):
            self.visit(ctx.statements())

        # if ctx.END() is None:
        #     raise SyntaxError("Expected 'END'")

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
        # try:
        #     var = ctx.children[0].symbol.text
        # except:
        #     print(ERROR)
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
        # return int(ctx.children[0].symbol.text)
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
        var, val = ctx.ID().symbol.text, *self.expression_checker(ctx)
        memory[var] += val

    def visitMinusop(self, ctx: TommyWiCParser.MinusopContext):
        var, val = ctx.ID().symbol.text, *self.expression_checker(ctx)
        memory[var] -= val

    def visitMulop(self, ctx: TommyWiCParser.MulopContext):
        var, val = ctx.ID().symbol.text, *self.expression_checker(ctx)
        memory[var] *= val

    def visitDivop(self, ctx: TommyWiCParser.DivopContext):
        var, val = ctx.ID().symbol.text, *self.expression_checker(ctx)
        try:
            memory[var] /= val
        except ZeroDivisionError:
            print(ERROR)


# *******************************************************************
# *******************************************************************
# *******************************************************************
# uncomment for testing:

# def main():
#     input_text = """
#     Oh hi Mark
#     n is just a 9 CHEEP CHEEP CHEEP!
#     f0 is just a 0 CHEEP CHEEP CHEEP!
#     f1 is just a 1 CHEEP CHEEP CHEEP!
#     cur is just a f1 CHEEP CHEEP CHEEP!
#     This is a great party, you invited all my friends
#     0 is great but n is a crowd
#     cur and your stupid mother f0
#     f0 is just a f1 CHEEP CHEEP CHEEP!
#     f1 is just a cur CHEEP CHEEP CHEEP!
#     n is as good in bed as he is at getting promotions... Awful!
#     Everybody betray me. I'm fed up with this world!
#     Yeah, you can say that again cur
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
