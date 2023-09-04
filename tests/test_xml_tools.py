# -*- coding: utf-8 -*-
# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ test_xml_tools.py                                                                                                             ║
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
# ║  0. 0. 1    . dev  1+ 1.00.24623.00 (03 Sep 23) - Initial Creation {J. Laccone}                                               ║
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
# ║             (ex: pycodestyle --ignore E129,E221 --max-line-len=132 test_xml_tools.py)                                         ║
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
# ║             (ex: pydocstyle --add-ignore D202 test_xml_tools.py)                                                              ║
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
# ║             (ex: pylint --max-line-length=132 test_xml_tools.py)                                                              ║
# ║                                                                                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
"""Module to provide testing capabilities for XmlTools class."""
import os
import shutil
import unittest

from structinator.exceptions import SourceDataTreeEmptyError
from structinator.exceptions import StructHeaderFileNotFoundError
from structinator.exceptions import StructMembersNotFoundError
from structinator.exceptions import StructSourceDataFileNotFoundError
from structinator.exceptions import StructTemplateFileNotFoundError
from structinator.exceptions import StructsNotFoundError

from structinator.xml_tools import XmlTools


class TestXmlTools(unittest.TestCase):
    """Class to test the operatiopon of the XmlTools class."""

    def setUp(self) -> None:

        # Determine our execution location
        self.my_path = os.path.dirname(__file__)
        self.my_path = self.my_path  + '/data/'

        # Create an instance of the class
        self.xts = XmlTools()

        # Call the base class setUp
        return super().setUp()

    def test_generate_struct_fail_no_data_specified(self):
        """Function to test the operation of generate_struct."""

        # ===================
        # == Preconditions ==
        # ====================

        # ===============
        # == Unit Test ==
        # ===============
        with self.assertRaises(Exception) as context:

            # Call the function
            self.xts.generate_struct()

            # Verify error type and message
            self.assertEqual(context.exception, SourceDataTreeEmptyError)
            self.assertEqual(str(context.exception.message), 'Source data tree not loaded from XML file')

    def test_generate_struct_fail_no_members_specified(self):
        """Function to test the operation of generate_struct."""

        # ===================
        # == Preconditions ==
        # ====================
        # Copy the necessary test data to the /tmp dir
        src_test_file = 'struct_source_data_missing_members.xml'
        shutil.copy(self.my_path + src_test_file, '/tmp')
        test_file = '/tmp/' + src_test_file

        # Set the instance source data file
        self.xts.struct_source_file_name = test_file

        # Open/parse the source data
        self.xts.open_struct_source_xml_file()

        # ===============
        # == Unit Test ==
        # ===============
        with self.assertRaises(Exception) as context:

            # Call the function
            self.xts.generate_struct()

            # Verify error type and message
            self.assertEqual(context.exception, StructMembersNotFoundError)
            self.assertEqual(str(context.exception.message), 'No struct members found in source data')

        # Clean-up Aisle Two
        if os.path.isfile(test_file):
            os.remove(test_file)

    def test_generate_struct_fail_no_structs_specified(self):
        """Function to test the operation of generate_struct."""

        # ===================
        # == Preconditions ==
        # ====================
        # Copy the necessary test data to the /tmp dir
        src_test_file = 'struct_source_data_missing_structs.xml'
        shutil.copy(self.my_path + src_test_file, '/tmp')
        test_file = '/tmp/' + src_test_file

        # Set the instance source data file
        self.xts.struct_source_file_name = test_file

        # Open/parse the source data
        self.xts.open_struct_source_xml_file()

        # ===============
        # == Unit Test ==
        # ===============
        with self.assertRaises(Exception) as context:

            # Call the function
            self.xts.generate_struct()

            # Verify error type and message
            self.assertEqual(context.exception, StructsNotFoundError)
            self.assertEqual(str(context.exception.message), 'No structs found in source data')

        # Clean-up Aisle Two
        if os.path.isfile(test_file):
            os.remove(test_file)

    def test_open_struct_source_xml_file_fail_bad_data_file_specified(self):
        """Function to test the operation of open_struct_source_xml_file."""

        # ===================
        # == Preconditions ==
        # ====================
        self.xts.struct_source_file_name = 'bill'

        # ===============
        # == Unit Test ==
        # ===============
        with self.assertRaises(Exception) as context:

            # Call the function
            self.xts.open_struct_source_xml_file()

            # Verify error type and message
            self.assertEqual(context.exception, OSError)
            self.assertEqual(str(context.exception.message), 'Template filename empty in source data')

    def test_open_struct_source_xml_file_fail_no_data_file_specified(self):
        """Function to test the operation of open_struct_source_xml_file."""

        # ===============
        # == Unit Test ==
        # ===============
        with self.assertRaises(Exception) as context:

            # Call the function
            self.xts.open_struct_source_xml_file()

            # Verify error type and message
            self.assertEqual(context.exception, StructSourceDataFileNotFoundError)
            self.assertEqual(str(context.exception.message), 'Class member is empty')

    def test_open_struct_source_xml_file_fail_no_header_file_specified(self):
        """Function to test the operation of open_struct_source_xml_file."""

        # ===================
        # == Preconditions ==
        # ====================
        # Copy the necessary test data to the /tmp dir
        src_test_file = 'struct_source_data_missing_header.xml'
        shutil.copy(self.my_path + src_test_file, '/tmp')
        test_file = '/tmp/' + src_test_file

        # Set the instance source data file
        self.xts.struct_source_file_name = test_file

        # Unit Test
        with self.assertRaises(Exception) as context:

            # Call the function
            self.xts.open_struct_source_xml_file()

            # Verify error type and message
            self.assertEqual(context.exception, StructHeaderFileNotFoundError)
            self.assertEqual(str(context.exception.message), 'Struct Header filename empty in source data')

        # Clean-up Aisle Two
        if os.path.isfile(test_file):
            os.remove(test_file)

    def test_open_struct_source_xml_file_fail_no_template_file_specified(self):
        """Function to test the operation of open_struct_source_xml_file."""

        # ===================
        # == Preconditions ==
        # ====================
        # Copy the necessary test data to the /tmp dir
        src_test_file = 'struct_source_data_missing_template.xml'
        shutil.copy(self.my_path + src_test_file, '/tmp')
        test_file = '/tmp/' + src_test_file

        # Set the instance source data file
        self.xts.struct_source_file_name = test_file

        # ===============
        # == Unit Test ==
        # ===============
        with self.assertRaises(Exception) as context:

            # Call the function
            self.xts.open_struct_source_xml_file()

            # Verify error type and message
            self.assertEqual(context.exception, StructTemplateFileNotFoundError)
            self.assertEqual(str(context.exception.message), 'Template filename empty in source data')

        # Clean-up Aisle Two
        if os.path.isfile(test_file):
            os.remove(test_file)
