#!/usr/bin/env python3
"""Wrapper script for cpplint."""
import sys
from typing import List

from hooks.utils import StaticAnalyzerCmd


class CpplintCmd(StaticAnalyzerCmd):
    """Class for the cpplint command."""

    command = "cpplint"
    lookbehind = "cpplint "

    def __init__(self, args: List[str]):
        super().__init__(self.command, self.lookbehind, args)
        self.parse_args(args)
        self.add_if_missing(["--verbose=0"])

    def run(self):
        """Run cpplint"""
        self.run_command(self.args + self.files)  # cpplint is unique in requiring args before filename
        self.exit_on_error(stream_redirect=[(sys.stdout, None)]) # cpplint writes relevant output to stderr, so ignore stdout


def main(argv: List[str] = sys.argv):
    cmd = CpplintCmd(argv)
    cmd.run()


if __name__ == "__main__":
    main()
