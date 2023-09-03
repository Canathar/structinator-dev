# -*- coding: utf-8 -*-
# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ header_file_tools.py                                                                                                          ║
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
# ║  0. 0. 1    . dev  1+ 1.00.24523.00 (01 Sep 23) - Initial Creation {J. Laccone}                                               ║
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
# ║             (ex: pycodestyle --ignore E129,E221 --max-line-len=132 header_file_tools.py)                                      ║
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
# ║             (ex: pydocstyle --add-ignore D202 header_file_tools.py)                                                           ║
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
# ║             (ex: pylint --max-line-length=132 --extension-pkg-allow=lxml header_file_tools.py)                                ║
# ║                                                                                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
"""Module to provide functional capabilities to read/write C++ header files."""
import datetime
import importlib.resources
import inspect
import logging
import os

# Set the public version identifer (major.minor.micro) and the local version label
__version__ = "0.0.1.dev2+1.00.24523.00"


# Attach to the root logger
LOG = logging.getLogger()

# Header file template constants
HEADER_FILE_NAME = '[[[header_file_name]]]'
HEADER_FILE_CONTENTS = '[[[header_file_contents]]]'
HEADER_FILE_CREATION_DATE = '[[[header_file_creation_date]]]'
HEADER_FILE_GUARD_START = '[[[header_file_guard_start]]]'
HEADER_FILE_GUARD_END = '[[[header_file_guard_end]]]'


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @class  HeaderFileTools                                                                                                       ║
# ║                                                                                                                               ║
# ║ @brief  Class encapsulating all of the functionality associated with the creation of a C++ header file                        ║
# ║                                                                                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
class HeaderFileTools():
    """Class containing the functionality to create a C++ header file."""

    def __init__(self):
        """Initialize the object."""

        fname = 'HeaderFileTools.' + str(inspect.currentframe().f_code.co_name)
        LOG.debug("%s Entering", fname)

        # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════╗
        # ║                                              Local Variables                                              ║
        # ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════╣
        # ║                                                                                                           ║
        # ║   Parameters used to define the local script                                                              ║
        # ║                                                                                                           ║
        # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════╝
        self.__header_file_name = ""

        self.__header_file_contents = ""

        self.__header_template_data = ""

        self.__header_template_file = ""

        LOG.debug("%s Exiting", fname)

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                                                                                               ║
    # ║                                     ===== Class Member get Functions =====                                    ║
    # ║                                                                                                               ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                     Script Processing Command Line Arguments get Functions                     ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __get_header_file_name(self):
        """Get Function."""
        return self.__header_file_name

    def __get_header_file_contents(self):
        """Get Function."""
        return self.__header_file_contents

    def __get_header_template_data(self):
        """Get Function."""
        return self.__header_template_data

    def __get_header_template_file(self):
        """Get Function."""
        return self.__header_template_file

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                                                                                               ║
    # ║                                     ===== Class Member set Functions =====                                    ║
    # ║                                                                                                               ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                     Script Processing Command Line Arguments set Functions                     ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __set_header_file_name(self, value):
        """Set Function."""
        self.__header_file_name = value

    def __set_header_file_contents(self, value):
        """Set Function."""
        self.__header_file_contents = value

    def __set_header_template_data(self, value):
        """Set Function."""
        self.__header_template_data = value

    def __set_header_template_file(self, value):
        """Set Function."""
        self.__header_template_file = value

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
    header_file_name = property(__get_header_file_name, __set_header_file_name,
                                doc='String value denoting the name of the header file to create')

    header_file_contents = property(__get_header_file_contents, __set_header_file_contents,
                                    doc='Object containing the string contents for the header file to create')

    header_template_data = property(__get_header_template_data, __set_header_template_data,
                                    doc='Object containing the string data from the header template file')

    header_template_file = property(__get_header_template_file, __set_header_template_file,
                                    doc='String value denoting the name of the header template file')

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║ @fn     write_header_file                                                                                                 ║
    # ║                                                                                                                           ║
    # ║ @brief  Function to write a specified header file.                                                                        ║
    # ║                                                                                                                           ║
    # ║ @return void                                                                                                              ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    def open_header_template_file(self):
        """Function to open a specified xml file."""

        fname = 'HeaderFileTools.' + str(inspect.currentframe().f_code.co_name)
        LOG.debug("%s Entering", fname)

        try:

            # Obtain the path for the specified template file from the package data
            src_template = importlib.resources.files("structinator").joinpath("data").joinpath(self.header_template_file)

            # Open the header file and read the contents
            header_file = open(src_template, "r", encoding="utf-8")
            self.header_template_data = header_file.read()
            header_file.close()

        except Exception as ex:

            template = "   Error Creating Header File - Error Type: {0} Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            LOG.error(message)

        finally:

            LOG.debug("%s Exiting", fname)


    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║ @fn     write_header_file                                                                                                 ║
    # ║                                                                                                                           ║
    # ║ @brief  Function to write a specified header file.                                                                        ║
    # ║                                                                                                                           ║
    # ║ @return void                                                                                                              ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    def write_header_file(self):
        """Function to open a specified xml file."""

        fname = 'HeaderFileTools.' + str(inspect.currentframe().f_code.co_name)
        LOG.debug("%s Entering", fname)

        try:
            # Generate time/date stamps
            src_time_stamp = datetime.datetime.now()
            mon_day_yr_time_stamp = src_time_stamp.strftime("%d %b %y")

            # Open a new file for output
            with open(f"{self.header_file_name}", "w+", encoding="utf-8") as header_file:

                # Display the original header template data
                LOG.debug("Source Template File Contents:\n%s", self.header_template_data)

                # Create a local copy of the header template data
                header_data = self.header_template_data

                # Replace the file name placeholder with the desired value
                base_file_name = os.path.basename(self.header_file_name.rstrip("/"))
                header_data = header_data.replace(HEADER_FILE_NAME, base_file_name)

                # Replace the file creation date placeholder with the desired value
                header_data = header_data.replace(HEADER_FILE_CREATION_DATE, mon_day_yr_time_stamp)

                # Replace the file guard start/end placeholders with the desired values
                guard_name = base_file_name.replace(".", "_")
                guard_start = f"#ifndef _{guard_name.upper()}_\n#define _{guard_name.upper()}_\n"
                guard_end = f"#endif // _{guard_name.upper()}_"
                header_data = header_data.replace(HEADER_FILE_GUARD_START, guard_start)
                header_data = header_data.replace(HEADER_FILE_GUARD_END, guard_end)

                # Replace the file contents placeholder with the desired value
                header_data = header_data.replace(HEADER_FILE_CONTENTS, self.header_file_contents)

                # Display the modified header data
                LOG.debug("Modified File Contents:\n%s", header_data)

                # Write the header file
                header_file.write(header_data)
                header_file.close()

        except Exception as ex:

            template = "   Error Creating Header File - Error Type: {0} Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            LOG.error(message)

        finally:

            LOG.debug("%s Exiting", fname)
