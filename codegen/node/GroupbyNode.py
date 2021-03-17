from typing import List

from jinja2 import Template
from sqlparse.sql import Identifier, Function

from .BaseNode import BaseNode
from ..table.table import Table


class GroupByNode(BaseNode):
    def __init__(self, tables: List[Table]):
        """
        Group By statement
        :param tables: a list of tables used to generate code
        """
        super().__init__(tables=tables)
        self.self_identify = "GroupBy"
