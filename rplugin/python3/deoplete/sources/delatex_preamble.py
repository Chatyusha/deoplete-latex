from .base import Base
import re
import json

class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)
        self.name = 'deoplete-latex'
        self.mark = '[latex]'
        self.input_pattern = (r'^\\')

    def on_init(self, context):
        vars = context['vars']

        self.json_path = vars.get('json_path', '') + '/preamble.json'

        try:
            # init(load suorce) only work
            pass
        except Exception:
            # Ignore the error
            pass

    def gather_candidates(self, context):
        pop_json = open(self.json_path,'r')
        pop_list = json.load(pop_json)
        return pop_list["Preamble"]
