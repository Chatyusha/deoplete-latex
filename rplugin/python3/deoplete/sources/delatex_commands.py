from .base import Base
import re
import json
import os
import pathlib

class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)
        self.name = 'deoplete-latex-commands'
        self.mark = '[latex]'
        self.input_pattern = (r'\\')
        json_path=str(pathlib.Path(__file__).parent.parent.parent.parent.parent) + "/grammar/latex/json"
        file_path = json_path + "/greek.json"
        pop_json = open(file_path,'r')
        self.pop_list = json.load(pop_json)
        for i in self.pop_list['Greeks']:
            i['dup'] = 1

    def on_init(self, context):
        vars = context['vars']

        try:
            # init(load suorce) only work
            pass
        except Exception:
            # Ignore the error
            pass

    def gather_candidates(self, context):
        return self.pop_list["Greeks"]
