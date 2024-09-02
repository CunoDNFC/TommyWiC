# Generated from TommyWiC.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TommyWiCParser import TommyWiCParser
else:
    from TommyWiCParser import TommyWiCParser

# This class defines a complete generic visitor for a parse tree produced by TommyWiCParser.

class TommyWiCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TommyWiCParser#program.
    def visitProgram(self, ctx:TommyWiCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TommyWiCParser#main_func.
    def visitMain_func(self, ctx:TommyWiCParser.Main_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TommyWiCParser#statements.
    def visitStatements(self, ctx:TommyWiCParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TommyWiCParser#statement.
    def visitStatement(self, ctx:TommyWiCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TommyWiCParser#print_stmt.
    def visitPrint_stmt(self, ctx:TommyWiCParser.Print_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TommyWiCParser#print_str.
    def visitPrint_str(self, ctx:TommyWiCParser.Print_strContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TommyWiCParser#print_expression.
    def visitPrint_expression(self, ctx:TommyWiCParser.Print_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TommyWiCParser#condition_stmt.
    def visitCondition_stmt(self, ctx:TommyWiCParser.Condition_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TommyWiCParser#while_stmt.
    def visitWhile_stmt(self, ctx:TommyWiCParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TommyWiCParser#try_except.
    def visitTry_except(self, ctx:TommyWiCParser.Try_exceptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TommyWiCParser#var_assign.
    def visitVar_assign(self, ctx:TommyWiCParser.Var_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TommyWiCParser#not.
    def visitNot(self, ctx:TommyWiCParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TommyWiCParser#or.
    def visitOr(self, ctx:TommyWiCParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TommyWiCParser#and.
    def visitAnd(self, ctx:TommyWiCParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TommyWiCParser#varexpr.
    def visitVarexpr(self, ctx:TommyWiCParser.VarexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TommyWiCParser#trueexpr.
    def visitTrueexpr(self, ctx:TommyWiCParser.TrueexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TommyWiCParser#numberexpr.
    def visitNumberexpr(self, ctx:TommyWiCParser.NumberexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TommyWiCParser#falseexpr.
    def visitFalseexpr(self, ctx:TommyWiCParser.FalseexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TommyWiCParser#less.
    def visitLess(self, ctx:TommyWiCParser.LessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TommyWiCParser#noteq.
    def visitNoteq(self, ctx:TommyWiCParser.NoteqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TommyWiCParser#operations.
    def visitOperations(self, ctx:TommyWiCParser.OperationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TommyWiCParser#plusop.
    def visitPlusop(self, ctx:TommyWiCParser.PlusopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TommyWiCParser#minusop.
    def visitMinusop(self, ctx:TommyWiCParser.MinusopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TommyWiCParser#mulop.
    def visitMulop(self, ctx:TommyWiCParser.MulopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TommyWiCParser#divop.
    def visitDivop(self, ctx:TommyWiCParser.DivopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TommyWiCParser#decrement.
    def visitDecrement(self, ctx:TommyWiCParser.DecrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TommyWiCParser#increment.
    def visitIncrement(self, ctx:TommyWiCParser.IncrementContext):
        return self.visitChildren(ctx)



del TommyWiCParser