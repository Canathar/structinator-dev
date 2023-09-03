# -*- coding: utf-8 -*-
# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ xml_tools.py                                                                                                                  ║
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
# ║  0. 0. 1    . dev  1+ 1.00.24423.00 (01 Sep 23) - Initial Creation {J. Laccone}                                               ║
# ║                                                      Added header, added reference data, added python source code encoding    ║
# ║  0. 0. 1    . dev  2+ 1.00.24523.00 (02 Sep 23) - Development Update {J. Laccone}                                             ║
# ║                                                      Added capability to load package resource data                           ║
# ║                                                                                                                               ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║                                                           Reference                                                           ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║                                                                                                                               ║
# ║ Examples Of Xpath Queries Using lxml In Python - GitHub                                                                       ║
# ║ -------------------------------------------------------                                                                       ║
# ║    https://gist.github.com/IanHopkinson/ad45831a2fb73f537a79                                                                  ║
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
# ║             (ex: pycodestyle --ignore E129,E221 --max-line-len=132 xml_tools.py)                                              ║
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
# ║             (ex: pydocstyle --add-ignore D202 xml_tools.py)                                                                   ║
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
# ║             pylint --max-line-length=132 --extension-pkg-allow=lxml <python-file>                                             ║
# ║             (ex: pylint --max-line-length=132 --extension-pkg-allow=lxml xml_tools.py)                                        ║
# ║                                                                                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
"""Module to provide functional capabilities to read/write/verify XML files."""
import datetime
import importlib.resources
import inspect
import logging
from lxml import etree as et

# Set the public version identifer (major.minor.micro) and the local version label
__version__ = "0.0.1.dev2+1.00.24523.00"


# Attach to the root logger
LOG = logging.getLogger()

# Xpath constants used for searching the source data
# see: https://www.w3schools.com/xml/xpath_syntax.asp
CONFIG_HEADER_FILE_NAME_XPATH ='/structinator/config/header_file_name'
CONFIG_TEMPLATE_FILE_NAME_XPATH = '/structinator/config/template_file_name'
STRUCT_XPATH = '/structinator/structs/struct'
STRUCT_MEMBER_XPATH = './/members/member'

# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @class  XmlTools                                                                                                              ║
# ║                                                                                                                               ║
# ║ @brief  Class encapsulating all of the functionality associated with XML support operations                                   ║
# ║                                                                                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
class XmlTools():
    """Class containing the functionality associated with XML support operations."""

    def __init__(self):
        """Initialize the object."""

        fname = __class__.__name__ + '.' +  str(inspect.currentframe().f_code.co_name)
        LOG.debug("%s Entering", fname)

        # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════╗
        # ║                                              Local Variables                                              ║
        # ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════╣
        # ║                                                                                                           ║
        # ║   Parameters used to define the local script                                                              ║
        # ║                                                                                                           ║
        # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════╝
        self.__struct_source_file_name = ""

        self.__struct_source_tree = None

        self.__struct_file_contents = ""

        self.__struct_file_name = ""

        self.__template_file_name = ""

        LOG.debug("%s Exiting", fname)

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                                                                                               ║
    # ║                                     ===== Class Member get Functions =====                                    ║
    # ║                                                                                                               ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                     Script Processing Command Line Arguments get Functions                     ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __get_struct_source_file_name(self):
        """Get Function."""
        return self.__struct_source_file_name

    def __get_struct_source_tree(self):
        """Get Function."""
        return self.__struct_source_tree

    def __get_struct_file_contents(self):
        """Get Function."""
        return self.__struct_file_contents

    def __get_struct_file_name(self):
        """Get Function."""
        return self.__struct_file_name

    def __get_template_file_name(self):
        """Get Function."""
        return self.__template_file_name

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                                                                                               ║
    # ║                                     ===== Class Member set Functions =====                                    ║
    # ║                                                                                                               ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                     Script Processing Command Line Arguments set Functions                     ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __set_struct_source_file_name(self, value):
        """Set Function."""
        self.__struct_source_file_name = value

    def __set_struct_source_tree(self, value):
        """Set Function."""
        self.__struct_source_tree = value

    def __set_struct_file_contents(self, value):
        """Set Function."""
        self.__struct_file_contents = value

    def __set_struct_file_name(self, value):
        """Set Function."""
        self.__struct_file_name = value

    def __set_template_file_name(self, value):
        """Set Function."""
        self.__template_file_name = value

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                                                                                               ║
    # ║                                      ===== Class Member Properties =====                                      ║
    # ║                                                                                                               ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                    Properties For Script Processing Command Line Arguments                     ║
    # ║                                                                                                ║
    # ║ NOTE: Ensure that these properties are defined BELOW the get/set routines they reference       ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    struct_source_file_name = property(__get_struct_source_file_name, __set_struct_source_file_name,
                                       doc='String value denoting the name of the file containting the struct source data')

    struct_source_tree = property(__get_struct_source_tree, __set_struct_source_tree,
                                  doc='Object containing the string data from the struct source data file')

    struct_file_contents = property(__get_struct_file_contents, __set_struct_file_contents,
                                    doc='Object containing the string data to be output to the header file')

    struct_file_name = property(__get_struct_file_name, __set_struct_file_name,
                                doc='String value denoting the name of the output header file')

    template_file_name = property(__get_template_file_name, __set_template_file_name,
                                  doc='String value denoting the name of the template file')

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║ @fn     generate_struct                                                                                                   ║
    # ║                                                                                                                           ║
    # ║ @brief  Function to generate a C++ struct from XML data.                                                                  ║
    # ║                                                                                                                           ║
    # ║ @return void                                                                                                              ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    def generate_struct(self):
        """Function to generate a C++ struct from XML data."""

        fname = __class__.__name__ + '.' +  str(inspect.currentframe().f_code.co_name)
        LOG.debug("%s Entering", fname)

        try:

            # Retrieve the collection of structs from the tree
            structs = self.struct_source_tree.xpath(STRUCT_XPATH)

            # Generate a C++ struct for each of the nodes in the collection
            for struct in structs:

                # Start the struct
                self.struct_file_contents += "// Structure is dynamically generated, DO NOT manually edit!\n"
                self.struct_file_contents += "struct\n{\n"

                # Retrieve the collection of members from the tree
                members = struct.xpath(STRUCT_MEMBER_XPATH)

                # Generate a C++ member for each of the nodes in the collection
                for member in members:

                    # Add the member, type and name
                    self.struct_file_contents += "   " + member.attrib['type'] + " " + member.attrib['name'] + ";\n"

                # End the struct
                self.struct_file_contents += "} " + struct.attrib['name'] + ";\n\n"

        except Exception as ex:

            template = "   Error Generating Struct - Error Type: {0} Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            LOG.error(message)

        finally:

            LOG.debug("%s Exiting", fname)


    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║ @fn     open_struct_source_xml_file                                                                                       ║
    # ║                                                                                                                           ║
    # ║ @brief  Function to open the struct source xml file.                                                                      ║
    # ║                                                                                                                           ║
    # ║ @return void                                                                                                              ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    def open_struct_source_xml_file(self):
        """Function to open the struct source xml file."""

        fname = __class__.__name__ + '.' +  str(inspect.currentframe().f_code.co_name)
        LOG.debug("%s Entering", fname)

        try:

            # Open the specified file
            self.struct_source_tree = et.parse(self.struct_source_file_name)
            LOG.debug("The root tag of the document is: %s", str(self.struct_source_tree.getroot().tag))

            # Retrieve the header file name from the tree
            header_file_node = self.struct_source_tree.xpath(CONFIG_HEADER_FILE_NAME_XPATH)
            self.struct_file_name = header_file_node[0].text
            LOG.debug("The configured header filename is: %s", self.struct_file_name)

            # Retrieve the template file name from the tree
            template_file_node = self.struct_source_tree.xpath(CONFIG_TEMPLATE_FILE_NAME_XPATH)
            self.template_file_name = template_file_node[0].text
            LOG.debug("The configured template filename is: %s", self.template_file_name)

        except Exception as ex:

            template = "   Error Opening XML File - Error Type: {0} Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            LOG.error(message)

        finally:

            LOG.debug("%s Exiting", fname)
