from .base import Base

class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'callmekohei'           # なまえ
        self.mark = '[kohei]'               # mark のなまえ

    def gather_candidates(self, context):
        return ["apple","banana","cherry"]  # ポップアップのリスト
