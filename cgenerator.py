import os
from jinja2 import PackageLoader, Environment, FileSystemLoader


def generate(greet):
    TemplateLoader = FileSystemLoader(os.path.abspath("."))
    env = Environment(loader = TemplateLoader)
    template = env.get_template("hello.template")
    fd = open("hello.c", "w")
    fd.write(template.render(name = greet))
    fd.close()
