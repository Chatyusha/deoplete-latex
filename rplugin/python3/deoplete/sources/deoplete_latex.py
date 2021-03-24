from .base import Base
import re

class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)
        self.name = 'deoplete-latex'
        self.mark = '[latex]'
        self.input_pattern = (r'^\\')

    def on_init(self, context):
        vars = context['vars']

        self.json_path = vars.get('', '')

        try:
            # init(load suorce) only work
            pass
        except Exception:
            # Ignore the error
            pass

    def gather_candidates(self, context):
        return [
            {
                  'word' : "begin",
                  'dup'  : 1
            }
        ]
