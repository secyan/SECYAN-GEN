from typing import List, Optional

from sqlparse.sql import Identifier

try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources

from . import templates


class BaseNode:
    # Prev statement
    prev: Optional["BaseNode"]

    # next statement
    next: Optional["BaseNode"]

    # Sub query
    child: Optional["BaseNode"]

    def __init__(self):
        """
        Base SQL node object.
        """
        self.self_identify = "Base"
        self.prev: Optional["BaseNode"] = None
        self.child: Optional["BaseNode"] = None
        self.next: Optional["BaseNode"] = None
        self.identifier_list: List[Identifier] = []

    def print_graph(self):
        """
        Print SQL tree Graph
        :return:
        """
        cur = self

        while cur:
            print(f"{cur.self_identify} - {cur.identifier_list}")
            print("|")
            cur = cur.next

    def merge(self):
        """
        Merge data with other nodes
        :return:
        """
        pass

    def to_code(self) -> List[str]:
        """
        Generate code
        :return:
        """
        pass

    def get_last_node(self) -> "BaseNode":
        """
        Get last node in this tree structure
        :return:
        """
        cur = self

        while cur.next:
            cur = cur.next

        return cur

    def open_template_file(self, path: str):
        """
        Open jinja template file
        :param path: Jinja template file path
        :return:
        """
        template = pkg_resources.read_text(templates, path)
        return template
