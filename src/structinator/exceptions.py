# -*- coding: utf-8 -*-
# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ exceptions.py                                                                                                                 ║
# ║                                                                                                                               ║
# ║    Document Encoding           : UTF-8, UNIX Line Terminator                                                                  ║
# ║    Document Best Viewed/Printed: Page{Legal, Landscape, 0.25in Side Margins}   Font{Monospaced Font, Normal, 10pt}            ║
# ║                                                                                                                               ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║                                                       Revision History                                                        ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║  <public version id>+<local ver id>   <date>                     <Revision Type>                                              ║
# ║ NN.NN.NNaaNN.aaaaNNN+VV.vv.DOYyy.bb (dd MMM yy) - Initial Creation/Development Update/Maintenance Update                      ║
# ║                                                                                                                               ║
# ║  0. 0. 1    . dev  1+ 1.00.24523.00 (02 Sep 23) - Initial Creation {J. Laccone}                                               ║
# ║                                                      Added header, added reference data, added python source code encoding    ║
# ║                                                                                                                               ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║                                                           Reference                                                           ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║                                                                                                                               ║
# ║                                                                                                                               ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║                                                             Notes                                                             ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║                                                                                                                               ║
# ║ Code Check Prerequisites                                                                                                      ║
# ║ ========================                                                                                                      ║
# ║    1. Open a terminal window                                                                                                  ║
# ║    2. Change to the desired python environment (SCL, anaconda/miniconda, venv, base OS)                                       ║
# ║    3. Verify that the desired tools are installed in the desired python environment by typing the following command(s)        ║
# ║       into the terminal window:                                                                                               ║
# ║                                                                                                                               ║
# ║          pip list                                                                                                             ║
# ║          (Search Returned List For The Following: pycodestyle, pydocstyle, pylint)                                            ║
# ║                                                                                                                               ║
# ║                                                                                                                               ║
# ║ Code Check Procedures                                                                                                         ║
# ║ =====================                                                                                                         ║
# ║                                                                                                                               ║
# ║    Style Compliance Procedure                                                                                                 ║
# ║    --------------------------                                                                                                 ║
# ║       1. Open a terminal window                                                                                               ║
# ║       2. Check this file for compliance to the python coding standard by typing the following command(s) into                 ║
# ║          the terminal window:                                                                                                 ║
# ║          NOTE1: This is the command line tool to check style compliance with PEP8                                             ║
# ║          NOTE2: Ignore discussed here: https://github.com/PyCQA/pycodestyle/issues/386                                        ║
# ║                                                                                                                               ║
# ║             pycodestyle --ignore E129,E221 --max-line-len=132 <python-file>                                                   ║
# ║             (ex: pycodestyle --ignore E129,E221 --max-line-len=132 exceptions.py)                                             ║
# ║                                                                                                                               ║
# ║                                                                                                                               ║
# ║    Docstring Compliance Procedure                                                                                             ║
# ║    ------------------------------                                                                                             ║
# ║       1. Open a terminal window                                                                                               ║
# ║       2. Check this file for compliance to the python document standard by typing the following command(s) into               ║
# ║          the terminal window:                                                                                                 ║
# ║          NOTE1: This is the command line tool to check compliance with PEP257                                                 ║
# ║          NOTE2: Ignore discussed here: https://github.com/PyCQA/pydocstyle/issues/141                                         ║
# ║                                                                                                                               ║
# ║             pydocstyle --add-ignore D202 <python-file>                                                                        ║
# ║             (ex: pydocstyle --add-ignore D202 exceptions.py)                                                                  ║
# ║                                                                                                                               ║
# ║                                                                                                                               ║
# ║    Functional Compliance Procedure                                                                                            ║
# ║    -------------------------------                                                                                            ║
# ║       1. Open a terminal window                                                                                               ║
# ║       2. Check this file for functional programming errors by typing the following command(s) into                            ║
# ║          the terminal window:                                                                                                 ║
# ║          NOTE1: This is the command line tool to check functional compliance with PEP8                                        ║
# ║          NOTE2: Use the command "pylint --long-help" to display the current linter configuration                              ║
# ║                                                                                                                               ║
# ║             pylint --max-line-length=132 <python-file>                                                                        ║
# ║             (ex: pylint --max-line-length=132 exceptions.py)                                                                  ║
# ║                                                                                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
"""Module to provide custom exception definitions."""


# Set the public version identifer (major.minor.micro) and the local version label
__version__ = "0.0.1.dev1+1.00.24523.00"


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @class  UnknownOperationError                                                                                                 ║
# ║                                                                                                                               ║
# ║ @brief  Class containing the definition of an unknown operation exception                                                     ║
# ║                                                                                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
class UnknownOperationError(Exception):
    """Class containing the definition of an unknown operation exception."""

    def __init__(self, message):
        """Initialize the object."""

        self.message = message
        super().__init__(self.message)
