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
# ║  0. 0. 1    . dev  3+ 1.00.24623.00 (03 Sep 23) - Development Update {J. Laccone}                                             ║
# ║                                                      Added additional error handling                                          ║
# ║  0. 0. 1    . dev  4+ 1.00.24723.00 (04 Sep 23) - Development Update {J. Laccone}                                             ║
# ║                                                      Added Xslt capability                                                    ║
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
import inspect
import logging
from lxml import etree as et

from structinator.exceptions import SourceDataTreeEmptyError
from structinator.exceptions import StructHeaderFileNotFoundError
from structinator.exceptions import StructMembersNotFoundError
from structinator.exceptions import StructSchemaFileNotFoundError
from structinator.exceptions import StructSourceDataFileInvalidError
from structinator.exceptions import StructSourceDataFileNotFoundError
from structinator.exceptions import StructTemplateFileNotFoundError
from structinator.exceptions import StructsNotFoundError


# Set the public version identifer (major.minor.micro) and the local version label
__version__ = "0.0.1.dev4+1.00.24723.00"


# Attach to the root logger
LOG = logging.getLogger()

# Xpath constants used for searching the source data
# see: https://www.w3schools.com/xml/xpath_syntax.asp
CONFIG_HEADER_FILE_NAME_XPATH = '/structinator/config/header_file_name'
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
    # pylint: disable=too-many-instance-attributes
    """Class containing the functionality associated with XML support operations."""

    def __init__(self):
        """Initialize the object."""

        fname = __class__.__name__ + '.' + str(inspect.currentframe().f_code.co_name)
        LOG.debug("%s Entering", fname)

        # Internal variable to contain the result of the schema valudation
        self.__is_valid = False

        # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════╗
        # ║                                              Local Variables                                              ║
        # ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════╣
        # ║                                                                                                           ║
        # ║   Parameters used to define the local script                                                              ║
        # ║                                                                                                           ║
        # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════╝

        # Name of the XML file containing the raw struct source data
        self.__struct_source_xml_file_name = ""

        # Name of the XSD file containing the schema to validate the raw struct source data
        self.__struct_source_xsd_file_name = ""

        # Object to store the XSD tree once it is parsed from the schema file
        self.__struct_source_schema = None

        # Object to store the XML tree once it is parsed from the source data file
        self.__struct_source_tree = None

        # String to store the dynamically genertated C++ header file contents
        self.__struct_file_contents = ""

        # Name of the output C++ header file (obtained from the source data file)
        self.__struct_file_name = ""

        # Name of the text file template to use to generate the C++ header file (obtianed from source data file)
        self.__template_file_name = ""

        LOG.debug("%s Exiting", fname)

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                                                                                               ║
    # ║                                     ===== Class Member get Functions =====                                    ║
    # ║                                                                                                               ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __get_is_valid(self):
        """Get Function."""
        return self.__is_valid

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                     Script Processing Command Line Arguments get Functions                     ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __get_struct_source_xml_file_name(self):
        """Get Function."""
        return self.__struct_source_xml_file_name

    def __get_struct_source_xsd_file_name(self):
        """Get Function."""
        return self.__struct_source_xsd_file_name

    def __get_struct_source_schema(self):
        """Get Function."""
        return self.__struct_source_schema

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
    def __set_is_valid(self, value):
        """Set Function."""
        self.__is_valid = value

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                     Script Processing Command Line Arguments set Functions                     ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __set_struct_source_xml_file_name(self, value):
        """Set Function."""
        self.__struct_source_xml_file_name = value

    def __set_struct_source_xsd_file_name(self, value):
        """Set Function."""
        self.__struct_source_xsd_file_name = value

    def __set_struct_source_schema(self, value):
        """Set Function."""
        self.__struct_source_schema = value

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
    is_valid = property(__get_is_valid, __set_is_valid,
                        doc='Boolean flag denoting whether or not XML struct source data is valid')

    struct_source_xml_file_name = property(__get_struct_source_xml_file_name, __set_struct_source_xml_file_name,
                                           doc='String name of XML file containing the raw struct source data')

    struct_source_xsd_file_name = property(__get_struct_source_xsd_file_name, __set_struct_source_xsd_file_name,
                                           doc='String name of XML file containing schema to validate the raw struct source data')

    struct_source_schema = property(__get_struct_source_schema, __set_struct_source_schema,
                                    doc='Object to store XML schema once it is parsed from the schema file')

    struct_source_tree = property(__get_struct_source_tree, __set_struct_source_tree,
                                  doc='Object to store XML tree once it is parsed from the source data file')

    struct_file_contents = property(__get_struct_file_contents, __set_struct_file_contents,
                                    doc='String to store the dynamically genertated C++ header file contents')

    struct_file_name = property(__get_struct_file_name, __set_struct_file_name,
                                doc='String name of output C++ header file (obtained from the source data file)')

    template_file_name = property(__get_template_file_name, __set_template_file_name,
                                  doc='String name of text file template to generate the C++ header file (from source data file)')

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║ @fn     generate_struct                                                                                                   ║
    # ║                                                                                                                           ║
    # ║ @brief  Function to generate a C++ struct from XML data.                                                                  ║
    # ║                                                                                                                           ║
    # ║ @return void                                                                                                              ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    def generate_struct(self):
        """Generate a C++ struct from XML data."""

        fname = __class__.__name__ + '.' + str(inspect.currentframe().f_code.co_name)
        LOG.debug("%s Entering", fname)

        try:

            # =======================================================
            # == Process the struct(s) that are in the source data ==
            # =======================================================
            # Verify that the source data tree is valid
            if self.__is_valid is False:
                raise StructSourceDataFileInvalidError('XML Document Is Invalid')

            # Verify that the source tree was populated
            if self.struct_source_tree is None:
                raise SourceDataTreeEmptyError('Source data tree not loaded from XML file')

            # Retrieve the collection of structs from the tree
            structs = self.struct_source_tree.xpath(STRUCT_XPATH)

            # Verify that there are structs
            if len(structs) == 0:
                raise StructsNotFoundError('No structs found in source data')

            # Generate a C++ struct for each of the nodes in the collection
            for struct in structs:

                # Start the struct
                self.struct_file_contents += "// Structure is dynamically generated, DO NOT manually edit!\n"
                self.struct_file_contents += "struct\n{\n"

                # Retrieve the collection of members from the tree
                members = struct.xpath(STRUCT_MEMBER_XPATH)

                # Verify that there are members
                if len(members) == 0:
                    raise StructMembersNotFoundError('No struct members found in source data')

                # Generate a C++ member for each of the nodes in the collection
                for member in members:

                    # Add the member, type and name
                    self.struct_file_contents += "   " + member.attrib['type'] + " " + member.attrib['name'] + ";\n"

                # End the struct
                self.struct_file_contents += "} " + struct.attrib['name'] + ";\n\n"

        except (SourceDataTreeEmptyError, StructsNotFoundError, StructMembersNotFoundError) as struct_err:

            template = "   Error Generating Struct - Error Type: {0} Arguments: {1}"
            message = template.format(type(struct_err).__name__, struct_err.args)
            LOG.error(message)

        except StructSourceDataFileInvalidError as struct_err:

            template = "   Error Generating Struct - Error Type: {0} Arguments: {1}"
            message = template.format(type(struct_err).__name__, struct_err.args)
            LOG.error(message)
            print(message)

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
        """Open the struct source xml file."""

        fname = __class__.__name__ + '.' + str(inspect.currentframe().f_code.co_name)
        LOG.debug("%s Entering", fname)

        try:

            # ===================================================
            # == Open the supplied file and parse the contents ==
            # ===================================================
            # Verify that the specified file has been supplied
            if self.struct_source_xml_file_name == "":
                raise StructSourceDataFileNotFoundError('Class member is empty')

            # Open the specified file
            self.struct_source_tree = et.parse(self.struct_source_xml_file_name)
            LOG.debug("The root tag of the document is: %s", str(self.struct_source_tree.getroot().tag))

            # =====================
            # == Header filename ==
            # =====================
            # Retrieve the header file name from the tree
            header_file_node = self.struct_source_tree.xpath(CONFIG_HEADER_FILE_NAME_XPATH)

            # Verify that the header filename was retrieved
            if header_file_node[0].text is None:
                raise StructHeaderFileNotFoundError('Struct Header filename empty in source data')

            # Store the header file name
            self.struct_file_name = header_file_node[0].text
            LOG.debug("The configured header filename is: %s", self.struct_file_name)

            # =======================
            # == Template filename ==
            # =======================
            # Retrieve the template file name from the tree
            template_file_node = self.struct_source_tree.xpath(CONFIG_TEMPLATE_FILE_NAME_XPATH)

            # Verify that the template filename was retrieved
            if template_file_node[0].text is None:
                raise StructTemplateFileNotFoundError('Template filename empty in source data')

            # Store the template file name
            self.template_file_name = template_file_node[0].text
            LOG.debug("The configured template filename is: %s", self.template_file_name)

        except OSError as err:

            template = "   Error Opening XML File - Error Type: {0} Arguments: {1}"
            message = template.format(type(err).__name__, err.args)
            LOG.error(message)

        except (StructHeaderFileNotFoundError, StructSourceDataFileNotFoundError, StructTemplateFileNotFoundError) as struct_err:

            template = "   Error Opening XML File - Error Type: {0} Arguments: {1}"
            message = template.format(type(struct_err).__name__, struct_err.args)
            LOG.error(message)

        finally:

            LOG.debug("%s Exiting", fname)

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║ @fn     validate_struct_source_xml_file                                                                                   ║
    # ║                                                                                                                           ║
    # ║ @brief  Function to validate the struct source xml file.                                                                  ║
    # ║                                                                                                                           ║
    # ║ @return void                                                                                                              ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    def validate_struct_source_xml_file(self):
        """Validate the struct source xml file."""

        fname = __class__.__name__ + '.' + str(inspect.currentframe().f_code.co_name)
        LOG.debug("%s Entering", fname)

        try:

            # =================================================
            # == Open the schema file and parse the contents ==
            # =================================================
            # Verify that the specified file has been supplied
            if self.struct_source_xsd_file_name == "":
                raise StructSchemaFileNotFoundError('Class member is empty')

            # Open the specified file
            self.struct_source_schema = et.XMLSchema(file=self.struct_source_xsd_file_name)
            LOG.debug("Schema document is: %s", self.struct_source_schema)

            # Validate the XML source document
            self.is_valid = self.struct_source_schema.validate(self.struct_source_tree)
            if self.is_valid is False:
                raise StructSourceDataFileInvalidError('XML Document Is Invalid')

        except StructSchemaFileNotFoundError as struct_err:

            template = "   Error Validating XML File - Error Type: {0} Arguments: {1}"
            message = template.format(type(struct_err).__name__, struct_err.args)
            LOG.error(message)

        except StructSourceDataFileInvalidError as struct_err:

            template = "   Error Validating XML File - Error Type: {0} Arguments: {1}"
            message = template.format(type(struct_err).__name__, struct_err.args)
            LOG.error(message)
            print(message)

        finally:

            LOG.debug("%s Exiting", fname)
