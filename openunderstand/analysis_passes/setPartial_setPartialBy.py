# expression -> NEW creator


"""
## Description
This module find all OpenUnderstand call and callby references in a Java project


## References


"""

__author__ = 'Soheil Hoseini'
__version__ = '0.1.0'

from openunderstand.gen.javaLabeled.JavaParserLabeledListener import JavaParserLabeledListener
from openunderstand.gen.javaLabeled.JavaParserLabeled import JavaParserLabeled
import openunderstand.analysis_passes.class_properties as class_properties


class SetPartialSetByPartial(JavaParserLabeledListener):

    def __init__(self):

        ############ Soheil
        self.currentMethod = ""
        self.currentClass = ""
        self.partialsList = []
        self.fieldName = ""
        self.instanceName = ""

        ############################ Ali
        self.Currentmethod = ""
        self.setpartial = []
        self.dict = []

    ########################## Soheil
    @property
    def getPartialsList(self):
        return self.partialsList

    # Save the name of the current method
    def enterMethodDeclaration(self, ctx: JavaParserLabeled.MethodDeclarationContext):
        self.currentMethod = str(ctx.IDENTIFIER())

    # Save the name of the field and the instance
    def enterExpression1(self, ctx: JavaParserLabeled.Expression1Context):
        self.fieldName = str(ctx.IDENTIFIER())

        # Check if we have a field assignment
        if ctx.DOT().getText() == ".":
            self.instanceName = str(ctx.expression())

        # Check the existence of the record before adding it to the list
        tmpDict = {"currentClass": self.currentClass, "currentMethod": self.currentMethod,
                   "instanceName": self.instanceName, "fieldName": self.fieldName,"col":str(ctx.start).split(",")[3].split(":")[1],"line":str(ctx.start).split(",")[3].split(":")[0]}

        alreadyExists = False
        for dict in self.partialsList:
            if dict["currentClass"] == self.currentClass and dict["currentMethod"] == self.currentMethod \
                    and dict["fieldName"] != "":
                alreadyExists = True

        if not alreadyExists:
            self.partialsList.append(tmpDict)

    # Save the name of the current class
    def enterClassDeclaration(self, ctx: JavaParserLabeled.ClassDeclarationContext):
        self.currentClass = str(ctx.IDENTIFIER())

    ############################ ALi
    @property
    def get_dict(self):
        return self.dict

    @property
    def get_Currentmethod(self):
        return self.Currentmethod

    @property
    def get_setpartial(self):
        return self.setpartial

    def enterExpression2(self, ctx: JavaParserLabeled.Expression21Context):
        # self.setpartial.append(self, ctx.getChild(0).IDENTIFIER().getText())
        # self.dict.append(self, dict(zip(self.Currentmethod, self.setpartial)))
        pass

