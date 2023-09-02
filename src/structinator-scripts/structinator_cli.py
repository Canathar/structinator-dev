#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ structinator.py                                                                                                               ║
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
# ║  0. 0. 0 a 1        + 1.00.24423.00 (01 Sep 23) - Initial Creation {J. Laccone}                                               ║
# ║                                                      Added header, added reference data                                       ║
# ║                                                                                                                               ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║                                                           Reference                                                           ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║                                                                                                                               ║
# ║   PEP 0 -- Index of Python Enhancement Proposals (PEPs)                                                                       ║
# ║   -----------------------------------------------------                                                                       ║
# ║      https://peps.python.org/pep-0000/                                                                                        ║
# ║                                                                                                                               ║
# ║                                                                                                                               ║
# ║   PEP 8 -- Style Guide For Python Code                                                                                        ║
# ║   ------------------------------------                                                                                        ║
# ║      https://peps.python.org/pep-0008/                                                                                        ║
# ║                                                                                                                               ║
# ║   PEP 257 -- Docstring Conventions                                                                                            ║
# ║   --------------------------------                                                                                            ║
# ║      https://peps.python.org/pep-0257/                                                                                        ║
# ║                                                                                                                               ║
# ║   PEP 263 -- Defining Python Source Code Encodings                                                                            ║
# ║   ------------------------------------------------                                                                            ║
# ║      https://peps.python.org/pep-0263/                                                                                        ║
# ║                                                                                                                               ║
# ║   PEP 282 -- A Logging System                                                                                                 ║
# ║   ---------------------------                                                                                                 ║
# ║      https://peps.python.org/pep-0282/                                                                                        ║
# ║                                                                                                                               ║
# ║                                                                                                                               ║
# ║   Logging Facility For Python                                                                                                 ║
# ║   ---------------------------                                                                                                 ║
# ║      https://docs.python.org/3/library/logging.html                                                                           ║
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
# ║             (ex: pycodestyle --ignore E129,E221 --max-line-len=132 structinator.py)                                           ║
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
# ║             (ex: pydocstyle --add-ignore D202 structinator.py)                                                                ║
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
# ║             (ex: pylint --max-line-length=132 structinator.py)                                                                ║
# ║                                                                                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
"""Module to generate an interactive tool for demonstration of python wheel development/packaging."""
import datetime
import enum
import getopt
import importlib.resources
import inspect
import logging
import os
import re
import sys
import textwrap

from structinator.xml_tools import open_xml_file


# Set the public version identifer (major.minor.micro) and the local version label
__version__ = "0.0.0a1+1.00.24423.00"


# Attach to the root logger
LOG = logging.getLogger()


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @class  OperationType                                                                                                         ║
# ║                                                                                                                               ║
# ║ @brief  Enumeration to represent all of the choices available for script operation                                            ║
# ║                                                                                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
class OperationType(enum.Enum):
    """Enumeration to represent all of the choices available for script operation."""

    GENERATE = 1
    VERIFY = 2

    UNKNOWN = 100


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @class  CommandLineProcessor                                                                                                  ║
# ║                                                                                                                               ║
# ║ @brief  Class encapsulating all of the functionality associated with the command line options and arguments passed            ║
# ║         to the script                                                                                                         ║
# ║                                                                                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
class CommandLineProcessor():
   # pylint: disable=too-many-instance-attributes,too-few-publicmethods
    """Class containing the scripts comamnd line processor object."""

    def __init__(self):
        """Initialize the object."""

        fname = 'CommandLineProcessor.' + str(inspect.currentframe().f_code.co_name)
        LOG.debug("%s Entering", fname)

        self.__operation = OperationType.UNKNOWN

        LOG.debug("%s Exiting", fname)

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                                                                                               ║
    # ║                                     ===== Class Member get Functions =====                                    ║
    # ║                                                                                                               ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

    # ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                     Script Processing Command Line Arguments get Functions                     ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __get_operation(self):
        """Get Function."""
        return self.__operation

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
    operation = property(__get_operation,
                         doc='Enumerated value denoting the desired execution for the script')


    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║ @fn     process_command_line                                                                                  ║
    # ║                                                                                                               ║
    # ║ @brief  Function to process the command line options and arguments passed to the script                       ║
    # ║                                                                                                               ║
    # ║ @param  argv - List of command line arguments                                                                 ║
    # ║                                                                                                               ║
    # ║ @return void                                                                                                  ║
    # ║                                                                                                               ║
    # ║ @note   Custom command line options/arguments may be added here                                               ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    def process_command_line(self, argv):
        # pylint: disable=too-many-branches,too-many-statements,too-many-nested-blocks
        """Process the command line options and arguments passed to the script."""

        fname = 'CommandLineProcessor.' + str(inspect.currentframe().f_code.co_name)
        LOG.debug("%s Entering", fname)

        try:

            # Add any script specific command line options/arguments
            # Any additional options/arguments MUST be processed in the for loop below
            script_short_opts = "*hv"
            script_long_opts = ["help", "log", "version"]

            # If we have no arguments, display usage
            if len(argv) < 1:
                usage()
                sys.exit(2)

            # Process the operation first (unless help or version is requested)
            cmd_operation = argv[0]

            # ===== Operations =====
            if cmd_operation == "generate":
                self.__operation = OperationType.GENERATE

            elif cmd_operation == "verify":
                self.__operation = OperationType.VERIFY

            # ===== Special Case Items =====
            elif cmd_operation in ("-h", "--help"):
                display_help()

            elif cmd_operation in ("-v", "--version"):
                display_version()

            # ===== Unknown Operation =====
            else:
                print(f"\nUnknown Operation: {cmd_operation}")
                usage()
                sys,exit(3)

            # Parse the command line into options/arguments
            # pylint: disable=unused-variable
            opts, args = getopt.getopt(argv[1:], script_short_opts, script_long_opts)

            # Process the received options and arguments
            # pylint: enable=unused-variable
            for opt, arg in opts:

                # Print the command line options if we are run time debugging (DEBUG is defined as 10)
                # https://docs.python.org/3/library/logging.html#levels
                if LOG.getEffectiveLevel() == 10:
                    template = "Option: {0}   Argument: {1}"
                    message = template.format(str(opt), str(arg))
                    print(message)
                    LOG.debug(message)

                # ===== Information Commands - Always Available =====

                # Log
                if opt == "--log":
                    LOG.debug("Using Log File")

                # Debug
                elif opt == "-*":
                    LOG.debug("Logging Level Set To: DEBUG")

                # Help
                elif opt in ("-h", "--help"):
                    # This is where command based help would be added
                    display_help()

                # Version
                elif opt in ("-v", "--version"):
                    display_version()



                # ADD CUSTOM COMMAND LINE OPTION PROCESSING BELOW!!!
                #
                # If you have script specific command line arguments, add the processing of each
                # option (and possible argument) using the template below
                #
                # Short Option
                # ------------
                # elif opt == "-<single-character-option>":
                #
                # Long Option
                # -----------
                # elif opt == "--<multiple-character-option>":
                #
                # Short/Long Option
                # -----------------
                # elif opt in ("-<single-character-option>", "--<multiple-character-option>"):

                else:
                    raise Exception('Invalid Command Line Argument: ' + opt)

        except getopt.GetoptError as ex:

            template = "   GetoptError - Error Type: {0} Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            LOG.error(message)
            usage()
            sys.exit(2)

        finally:

            LOG.debug("%s Exiting", fname)


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     display_help                                                                                                          ║
# ║                                                                                                                               ║
# ║ @brief  Function to display help text                                                                                         ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ║                                                                                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
def display_help():
    """Command line option for help was passed to this script."""

    usage()
    sys.exit()


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     display_version                                                                                                       ║
# ║                                                                                                                               ║
# ║ @brief  Function to display version string                                                                                    ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ║                                                                                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
def display_version():
    """Command line option for version was passed to this script."""

    print(__version__)
    sys.exit()


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     script_main                                                                                                           ║
# ║                                                                                                                               ║
# ║ @brief  Function to act at the 'main' execution point of the script when not imported                                         ║
# ║                                                                                                                               ║
# ║ @param  argv - List of command line arguments                                                                                 ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
def script_main(argv):
    """Execute script from this point when not imported."""

    fname = str(inspect.currentframe().f_code.co_name)
    LOG.debug("%s Entering", fname)
    LOG.info("----- Program Start -----")

    operation_status = False

    LOG.debug("   ***** Initialize CommandLineProcessor *****")
    clp = CommandLineProcessor()

    LOG.debug("   ***** Process Command Line Options *****")
    clp.process_command_line(argv)

    LOG.debug("   ***** Verify That a Valid Operation Was Specified *****")
    if clp.operation == OperationType.UNKNOWN:

        raise Exception('No operation specified!')

    else:

        LOG.debug("   ***** Perform The Specified Operation *****")

        operation_name = str(clp.operation.name)
        LOG.info("   ===== Operation: %s =====", operation_name)
        print(f"Perform {operation_name} Operation")

        if clp.operation == OperationType.GENERATE:

            # Obtain the path for the specified sample XML file from the package data
            src_file = importlib.resources.files("structinator").joinpath("data").joinpath("basic_struct_example_1.xml")

            # Load the specified sample XML file from the package data
            open_xml_file(src_file)

            operation_status = True

        elif clp.operation == OperationType.VALIDATE:

            operation_status = True

    if operation_status is False:

        raise Exception('Operation Error')

    LOG.debug("%s Exiting", fname)
    LOG.info("----- Program End -----")


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     usage                                                                                                                 ║
# ║                                                                                                                               ║
# ║ @brief  Function to display the available command line options and arguments that can be passed to the script                 ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ║                                                                                                                               ║
# ║ @note   Custom command line options/arguments may be added here                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
def usage():
    # pylint: disable=too-many-locals,too-many-statements
    """Display the script operation."""

    script_basename = os.path.basename(__file__.rstrip("/"))

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                        Script Name And General Header                                         ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

    # Define the common indent for use with dedent
    script_usage = """
    ^"""

    # Add the script specific Usage line
    script_usage += """Usage: """ + script_basename  + """ OPERATION [OPTION(S)...]

    OPERATION"""

    # Process the text to make it look pretty
    tmp_text = textwrap.dedent(script_usage)
    usage_text = re.sub(r'\^', '', tmp_text)

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                                   Operations                                                  ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

    # Define the common indent for use with dedent
    operations = """
    ^"""

    # Add the operations
    operations += """
        generate
           Create a C++ header file from the supplied XML files

        verify
           Perform a validation on an XML file using a supplied XSL file


    OPTIONS"""

    # Process the text to make it look pretty
    tmp_text = textwrap.dedent(operations)
    usage_text += re.sub(r'\^', '', tmp_text)

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                              Information Options                                              ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

    # Define the common indent for use with dedent
    info_usage_text = """
    ^"""

    # Add the section header
    info_usage_text += """
       ========== Information Options =========="""

    info_usage_text += """

        -h, --help
           Display usage information (this text)"""

    info_usage_text += """

        --log
           Generate a log file"""

    info_usage_text += """

        -v, --version
           Display the script version
    """

    # Process the text to make it look pretty
    tmp_text = textwrap.dedent(info_usage_text)
    usage_text += re.sub(r'\^', '', tmp_text)

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                           Script Notes And Examples                                           ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    script_evoke = "./" + script_basename

    general_msg_example_text_1 = "   --log --option-one"
    general_msg_example_text_2 = "   --option-two opt-2-argument"

    # Define the common indent for use with dedent
    script_notes_examples = """
    ^"""

    # Add the script specific NOTES and Examples
    script_notes_examples += """

    NOTES

       This script is designed to provide an example framework


    Examples:

       # Obtain the version of the script
       """ + script_evoke + """ --version

       # Start the script with the various options
       """ + script_evoke + """ test1 \\
       """ + general_msg_example_text_1 + """ \\
       """ + general_msg_example_text_2 + """ \\

    """

    # Process the text to make it look pretty
    tmp_text = textwrap.dedent(script_notes_examples)
    usage_text += re.sub(r'\^', '', tmp_text)

    # ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                                  Usage Output                                                 ║
    # ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

    # Display The Script Usage
    print(usage_text)
    sys.exit(0)


# Program Execution Location
# This code allows the script to be either run from a command line or imported
if __name__ == "__main__":

    try:

        # Determine the logging level required
        # NOTE: If there is no logging command line option specified, logging will be disabled
        if "--log" in sys.argv:
            if "-*" in sys.argv:
                LOG_LEVEL = 'DEBUG'
            else:
                LOG_LEVEL = 'INFO'
        else:
            LOG_LEVEL = None
            LOG.addHandler(logging.NullHandler())

        # Determine whether or not a log file is required
        if "--log" in sys.argv:

            # Determine base file name
            # NOTE: os.path.basename is used to handle the case where the script is NOT run in the working directory
            BASE_FILE_REGEX = re.compile(r"(.*).py*")
            BASE_FILE_NAME = "/tmp/" + BASE_FILE_REGEX.sub(r"\1", os.path.basename(__file__.rstrip("/")))

            # Display the base file name (if required))
            if LOG_LEVEL == "DEBUG":
                print('Base File Name:', BASE_FILE_NAME)

            # Configure common logging parameters
            LOG_FILE = BASE_FILE_NAME + '.log'
            LOG_FORMAT = '%(asctime)-15s [%(levelname)s] -- [%(module)s]: %(message)s'
            logging.basicConfig(format=LOG_FORMAT, filename=LOG_FILE, level=LOG_LEVEL)

        # Call the main execution function, removing the first argument (the script name)
        script_main(sys.argv[1:])

    # Script level catch all for exceptions that are not of the following types: KeyboardInterrupt, SystemExit
    # NOTE1: This is not a bare 'except:' as a bare 'except:' is equivalent to 'except BaseException:'
    # NOTE2: Disabling the pylint warning as this is an intentional broad-except to capture and log script level exceptions
    #
    # pylint: disable=broad-except
    except Exception as ex:

        TEMPLATE = "   Unable To Execute Script - Error Type: {0} Arguments:\n{1!r}"
        MESSAGE = TEMPLATE.format(type(ex).__name__, ex.args)
        LOG.exception(MESSAGE)
        print("  ", str(ex))