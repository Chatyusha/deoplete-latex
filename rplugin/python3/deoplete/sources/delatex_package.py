from .base import Base
import re
import json
import os
import pathlib

class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)
        self.name = 'deoplete-latex-pkg'
        self.mark = '[latex]'
        self.input_pattern = (r'^\\usepackage.*{')

    def on_init(self, context):
        vars = context['vars']

        self.json_path=str(pathlib.Path(__file__).parent.parent.parent.parent.parent) + "/grammar/latex/json"


        try:
            # init(load suorce) only work
            pass
        except Exception:
            # Ignore the error
            pass

    def gather_candidates(self, context):
        file_path = self.json_path + "/packages.json"
        pop_json = open(file_path,'r')
        pop_list = json.load(pop_json)
        return pop_list["Packages"]
