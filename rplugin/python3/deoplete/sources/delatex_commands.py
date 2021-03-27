from .base import Base
from pynvim import Nvim
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
        json_files = ["/greek.json", "/math.json"]
        file_path = [json_path + i for i in json_files ]
        pop_json = [open(i,'r') for i in file_path]
        str_json= [json.load(i) for i in pop_json]
        Keys=["Greeks","Math"]
        self.pop_list = []
        for i in range(len(Keys)):
            self.pop_list += str_json[i][Keys[i]]
        for i in self.pop_list:
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

        return self.pop_list
