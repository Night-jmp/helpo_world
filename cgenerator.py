import os
from jinja2 import PackageLoader, Environment, FileSystemLoader
from abc import ABC, abstractmethod

class CgeneratorHandler(ABC):

    def __init__(self, *args, **kwargs):
        self.arguments = args

        for key, val in kwargs.items():
            self.__dict__[key] = val

    @abstractmethod
    def generate(self):
        pass

class CgeneratorHandlerV1(CgeneratorHandler):

    def generate(self, greet):
        # Very complex C code generator made from a template.
        TemplateLoader = FileSystemLoader(os.path.abspath("."))
        env = Environment(loader = TemplateLoader)
        template = env.get_template("hello.template")
        fd = open("hello.c", "w")
        program = template.render(name = greet) 
        print(program)
        fd.write(program)
        fd.close()

class cgeneratorHandlerFactory:
    def __init__(self, cgeneratorVersion):
        self.cgeneratorVersion = str(cgeneratorVersion)

    def generateCgeneratorHandler(self) -> CgeneratorHandler:
        return globals()["CgeneratorHandlerV" + self.cgeneratorVersion]()
