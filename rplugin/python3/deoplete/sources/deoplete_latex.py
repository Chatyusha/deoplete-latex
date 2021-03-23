from .base import Base
import re

class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)
        self.name = 'deoplete-latex'
        self.mark = '[latex]'
        self.input_pattern = (r'^\\')

    def gather_candidates(self, context):
        return [
            {
                  'word' : "apple"
                , 'abbr' : "apple  : red, round and delicious!"
                , 'info' : "Apple is delicious"
                , 'kind' : "Food"
                , 'dup'  : 1
            }
        ]
