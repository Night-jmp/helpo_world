import os
from jinja2 import PackageLoader, Environment, FileSystemLoader


def generate(greet):
    # Very complex C code generator made from a template.
    TemplateLoader = FileSystemLoader(os.path.abspath("."))
    env = Environment(loader = TemplateLoader)
    template = env.get_template("hello.template")
    fd = open("hello.c", "w")
    program = template.render(name = greet) 
    print(program)
    fd.write(program)
    fd.close()
