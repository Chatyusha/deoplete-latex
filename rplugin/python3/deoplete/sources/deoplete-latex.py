import re
from .base import Base

class Source(Base):

    def __init__ (self, vim):
        Base.__init__(self, vim)

        self.name = "deoplete-latex"
        self.mark = "[latex]"
        self.filetype = ['tex']
        self.input_tattern = (r'')

