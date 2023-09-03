#!/bin/bash
# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ build-pyproj.sh                                                                                                               ║
# ║                                                                                                                               ║
# ║    Document Encoding           : UTF-8, UNIX Line Terminator                                                                  ║
# ║    Document Best Viewed/Printed: Page{Legal, Landscape, 0.25in Side Margins}   Font{Monospaced Font, Normal, 10pt}            ║
# ║                                                                                                                               ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║                                                       Revision History                                                        ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║ VV.vv.DOYyy.bb (dd MMM yy) - Initial Creation/Development Update/Maintenance Update                                           ║
# ║                                                                                                                               ║
# ║  1.00.24323.00 (31 Aug 23) - Initial Creation {J. Laccone}                                                                    ║
# ║                                 Added base code                                                                               ║
# ║  1.00.24523.00 (02 Sep 23) - Development Update {J. Laccone}                                                                  ║
# ║                                 Corrected error with versions numbered above 99                                               ║
# ║                                                                                                                               ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║                                                           Reference                                                           ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║                                                                                                                               ║
# ║   Packaging PEPs                                                                                                              ║
# ║   --------------                                                                                                              ║
# ║      https://peps.python.org/topic/packaging/                                                                                 ║
# ║                                                                                                                               ║
# ║   PEP 440 -- Version Identification and Dependency Specification                                                              ║
# ║   --------------------------------------------------------------                                                              ║
# ║      https://www.python.org/dev/peps/pep-0440/                                                                                ║
# ║                                                                                                                               ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║                                                             Notes                                                             ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║                                                                                                                               ║
# ║   Building A Project                                                                                                          ║
# ║   ------------------                                                                                                          ║
# ║      1. Open a terminal window                                                                                                ║
# ║                                                                                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
version='1.00.22423.00'

# ------ Diagnostic Flags ------
DEBUG=false
EXTRA_DEBUG=false

# ------ Absolute Script Directory
SCRIPT_SOURCE=${BASH_SOURCE[0]}
while [ -L "${SCRIPT_SOURCE}" ]
do
   # Resolve ${SCRIPT_SOURCE} until the file is no longer a symlink
   DIR=$(cd -P "$(dirname "${SCRIPT_SOURCE}")" > /dev/null 2>&1 && pwd)
   SCRIPT_SOURCE=$(readlink "${SCRIPT_SOURCE}")

   # If ${SCRIPT_SOURCE} was a relative symlink, we need to resolve it relative to the path where the symlink file was located
   [[ "${SCRIPT_SOURCE}" != /* ]] && SCRIPT_SOURCE=${DIR}/${SCRIPT_SOURCE}
done
SCRIPT_DIR=$(cd -P "$(dirname "${SCRIPT_SOURCE}")" > /dev/null 2>&1 && pwd)

SCRIPT_NAME=$(basename "${BASH_SOURCE[0]%.*}")
RUNNING_DIR=$(realpath $(dirname "${BASH_SOURCE[0]}"))


# ------ Common Function Library ------
source "${SCRIPT_DIR}"/include/common-bash-utils.sh


# ------ Build Options ------
default_project_file="${RUNNING_DIR}/pyproject.toml"
project_file="${default_project_file}"

default_pre_type=""
pre_type="${default_pre_type}"

default_no_pre=false
no_pre="${default_no_pre}"

post_type=""

default_no_post=false
no_post="${default_no_post}"

dev_type=""

default_no_dev=false
no_dev="${default_no_dev}"


# ------ Version Increment Options ------
default_inc_major=false
inc_major="${default_inc_major}"

default_inc_minor=false
inc_minior="${default_inc_minor}"

default_inc_micro=false
inc_micro="${default_inc_micro}"

default_inc_pre=false
inc_pre="${default_inc_pre}"

default_inc_post=false
inc_post="${default_inc_post}"

default_inc_dev=false
inc_dev="${default_inc_dev}"


# ------ Version Options ------
default_major=""
major="${default_major}"

default_minor=""
minior="${default_minor}"

default_micro=""
micro="${default_micro}"

default_pre=""
pre="${default_pre}"

default_post=""
post="${default_post}"

default_dev=""
dev="${default_dev}"


# ------ Automation Options ------
default_auto=false
auto="${default_auto}"



# Version Information Is Defined As:
#
# Public Version Identifiers
# --------------------------
#    The canonical public version identifiers MUST comply with the following scheme:
#       [N!]N(.N)*[{a|b|rc}N][.postN][.devN]
#
#    Public Version Identifiers are separated into up to five segments:
#       Epoch Segment                 : [N!]
#       Release Segment               : N(.N)*
#       Pre-release Segment           : [{a|b|rc}N]
#       Post-release Segment          : [.postN]
#       Developmental Release Segment : [.devN]
#
#    All numeric components MUST be non-negative integers.
#
#    All numeric components MUST be interpreted and ordered according to their numeric value, not as text strings.
#
#    All numeric components MAY be zero.
#
#
# Local Version Identifiers
# -------------------------
#    Local version identifiers MUST comply with the following scheme:
#       <public version id>[+<local ver label>]
#
#    Local version labels MUST be limited to the following set of permitted characters:
#       ASCII letters ([a-zA-Z])
#       ASCII digits  ([0-9])
#       periods       (.)
#
#    Local version labels MUST start and end with an ASCII letter or digit
#
#
# Project Versioning
# ------------------
#    Public version identifiers will use the following scheme:
#       major.minor.micro[pre-release][.post-release][.dev-release]
#       (epoch is not explicitly used, it defaults to 0)
#       (ex: 99.99.99a99.post99.dev99 -- See notes below)
#
#    Local version labels in will use the following scheme:
#       major.minor.<day-of-year><last-two-digits-of-year>.build
#       (ex: 99.99.36518.99)
#
#    The following local version identifier will be used:
#       NN.NN.NNaaNN.aaaaNNN+VV.vv.DOYyy.bb
#       (ex1: 26.11.14a2.dev19+10.3.10417.12)
#       (ex2: 12.34.10rc42.post24+14.38.12418.21  -- This script handles this case, but it is NOT recommended see NOTE2)
#       (ex3: 17.0.2b5.post22.dev84+23.17.20619.29 -- This script handles this case, but it is NOT recommended see NOTE2, NOTE4)
#
#
# NOTE1: Regex Groups 1, 2, & 3 will ALWAYS be present
#
# NOTE2: Creating post-releases of pre-releases is strongly discouraged, as it makes the version identifier difficult to parse for
#        human readers. In general, it is substantially clearer to simply create a new pre-release by incrementing the
#        numeric component. (Regex Groups 4-7)
#
# NOTE3: While they may be useful for continuous integration purposes, publishing developmental releases of pre-releases to
#        general purpose public index servers is strongly discouraged, as it makes the version identifier difficult to parse for
#        human readers. If such a release needs to be published, it is substantially clearer to instead create a new pre-release
#        by incrementing the numeric component. (Regex Groups 8-9)
#
# NOTE4: Developmental releases of post-releases are also strongly discouraged, but they may be appropriate for projects which
#        use the post-release notation for full maintenance releases which may include code changes (Regex Groups 8-9)
#
# Define the regular expression for the public version id data
#                       major     .      minor     .      micro          pre-release           .  post-release          . dev-release
#                        \1               \2               \3          \4           \5          \6           \7         \8           \9
PVID="version = \"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)([ab]|rc)?(0|[1-9][0-9]*)?(\.post)?(0|[1-9][0-9]*)?(\.dev)?(0|[1-9][0-9]*)?\""
NEW_PVID=""


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     buildWheel                                                                                                            ║
# ║                                                                                                                               ║
# ║ @brief  Function to build the framework distribution package and the wheel                                                    ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
buildWheel()
{
   # Set the library automation flag
   USING_AUTOMATION="${auto}"

   curDate=$(date)
   printInfo "${curDate}" "- Building Source And Binary (wheel) Distribution"

   # Examine the project file for the current version information
   obtainVersion

   # Modify the project file with the new version information
   updateVersion

   # If we are not debugging, build the source and binary distributions with no isolation
   if [[ "${EXTRA_DEBUG}" == false ]]
   then
      python -m build -n
   fi
}


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     displayDebug                                                                                                          ║
# ║                                                                                                                               ║
# ║ @brief  Function to display the status of the internal variables                                                              ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
displayDebug()
{
   # Get the project data
   obtainVersion

   # Determine the current number of columns on the screen
   COLUMNS=$(tput cols)

   # All tab characters that begin the line will be ignored in the output
   #    https://en.wikipedia.org/wiki/Here_document#Unix_shells
   cat <<-EOF

	$(for (( i=1; i<=COLUMNS; i++ )) ; do printf "=" ; done)
	$(printDbgVariableCentered "${COLUMNS}" "Debug Information")
	$(for (( i=1; i<=COLUMNS; i++ )) ; do printf "=" ; done)

	   $(for (( i=1; i<=COLUMNS-6; i++ )) ; do printf "-" ; done)
	$(printDbgVariableCentered "${COLUMNS}" "   Script Variables   ")
	   $(for (( i=1; i<=COLUMNS-6; i++ )) ; do printf "-" ; done)

	   Script Name                         : $(printDbgVariable "${SCRIPT_NAME}")
	   Script Dir                          : $(printDbgVariable "${SCRIPT_DIR}")
	   Script Running Dir                  : $(printDbgVariable "${RUNNING_DIR}")
	   Shortopts                           : $(printDbgVariable "${shortopts}")
	   Longopts                            : $(printInfoVariableIndentedArray "38" "${longopts}")

	   $(for (( i=1; i<=COLUMNS-6; i++ )) ; do printf "-" ; done)
	$(printDbgVariableCentered "${COLUMNS}" "   Public Version Identifier Regular Expression   ")
	   $(for (( i=1; i<=COLUMNS-6; i++ )) ; do printf "-" ; done)
	$(printVariableCentered "${COLUMNS}" "   This variable reflects the regular expression used to scan the project file   ")

	   Public Version Id Regex             : $(printDbgVariable "${PVID}")

	   $(for (( i=1; i<=COLUMNS-6; i++ )) ; do printf "-" ; done)
	$(printDbgVariableCentered "${COLUMNS}" "   Version Variables (Including Project File)   ")
	   $(for (( i=1; i<=COLUMNS-6; i++ )) ; do printf "-" ; done)
	$(printVariableCentered "${COLUMNS}" "   These variables reflect the values of the version variables from the project file   ")

	   Major Version                       : $(printDbgVariable "${major}")
	   Minor Version                       : $(printDbgVariable "${minor}")
	   Micro Version                       : $(printDbgVariable "${micro}")

	   Pre Type                            : $(printDbgVariable "${pre_type}")
	   Pre Version                         : $(printDbgVariable "${pre}")

	   Post "Type"                         : $(printDbgVariable "${post_type}")
	   Post Version                        : $(printDbgVariable "${post}")

	   Dev "Type"                          : $(printDbgVariable "${dev_type}")
	   Dev Version                         : $(printDbgVariable "${dev}")

	   New Public Version Id               : $(printDbgVariable "${NEW_PVID}")

	$(for (( i=1; i<=COLUMNS; i++ )) ; do printf "=" ; done)

	EOF
}


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     obtainVersion                                                                                                         ║
# ║                                                                                                                               ║
# ║ @brief  Function to scan the project file and gather the version data for the individual elements                             ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
obtainVersion()
{
   # ╔════════════════════════════════════════════════════════════════════════╗
   # ║                  Process the Major version information                 ║
   # ╚════════════════════════════════════════════════════════════════════════╝
   # Check for empty value (non-empty value means user input a value)
   if [[ -z "${major}" ]]
   then

      # Only process the values in setup file if the user didn't input a value
      if [[ "${DEBUG}" == true ]] ; then printDebug "Reading Major Version From: ${project_file}" ; fi

      # Retrieve the current value
      major=`sed -n -r "s/${PVID}/\1/p" ${project_file}`
      if [[ "${DEBUG}" == true ]] ; then printDebug "Major Version: ${major}" ; fi

      # Increment the internal value
      if [[ "${inc_major}" == true ]]
      then
         major=$((${major} + 1))
         if [[ "${DEBUG}" == true ]] ; then printDebug "Incremented Major Version: ${major}" ; fi
      fi

   else

      if [[ "${DEBUG}" == true ]] ; then printDebug "Major Value Supplied: ${major}" ; fi

   fi


   # ╔════════════════════════════════════════════════════════════════════════╗
   # ║                  Process the Minor version information                 ║
   # ╚════════════════════════════════════════════════════════════════════════╝
   # Check for empty value (non-empty value means user input a value)
   if [[ -z "${minor}" ]]
   then

      # Only process the values in setup file if the user didn't input a value
      if [[ "${DEBUG}" == true ]] ; then printDebug "Reading Minor Version From: ${project_file}" ; fi

      # Retrieve the current value
      minor=`sed -n -r "s/${PVID}/\2/p" ${project_file}`
      if [[ "${DEBUG}" == true ]] ; then printDebug "Minor Version: ${minor}" ; fi

      # Increment the internal value
      if [[ "${inc_minor}" == true ]]
      then
         minor=$((${minor} + 1))
         if [[ "${DEBUG}" == true ]] ; then printDebug "Incremented Minor Version: ${minor}" ; fi
      fi

   else

      if [[ "${DEBUG}" == true ]] ; then printDebug "Minor Value Supplied: ${minor}" ; fi

   fi


   # ╔════════════════════════════════════════════════════════════════════════╗
   # ║                  Process the Micro version information                 ║
   # ╚════════════════════════════════════════════════════════════════════════╝
   # Check for empty value (non-empty value means user input a value)
   if [[ -z "${micro}" ]]
   then

      # Only process the values in setup file if the user didn't input a value
      if [[ "${DEBUG}" == true ]] ; then printDebug "Reading Micro Version From: ${project_file}" ; fi

      # Retrieve the current value
      micro=`sed -n -r "s/${PVID}/\3/p" ${project_file}`
      if [[ "${DEBUG}" == true ]] ; then printDebug "Micro Version: ${micro}" ; fi

      # Increment the internal value
      if [[ "${inc_micro}" == true ]]
      then
         micro=$((${micro} + 1))
         if [[ "${DEBUG}" == true ]] ; then printDebug "Incremented Micro Version: ${micro}" ; fi
      fi

   else

      if [[ "${DEBUG}" == true ]] ; then printDebug "Micro Value Supplied: ${micro}" ; fi

   fi


   # ╔════════════════════════════════════════════════════════════════════════╗
   # ║                       Process the Pre information                      ║
   # ╚════════════════════════════════════════════════════════════════════════╝
   if [[ "${no_pre}" == true ]]
   then

      if [[ "${DEBUG}" == true ]] ; then printDebug "Suppressing pre-type and value" ; fi
      pre_type=""
      pre=""

   else

      # Check for empty value (non-empty value means user input a value)
      if [[ -z "${pre}" ]]
      then

         # Only process the values in setup file if the user didn't input a value
         if [[ "${DEBUG}" == true ]] ; then printDebug "Reading Pre-Type And Version From: ${project_file}" ; fi

         # Retrieve the current value
         pre_type=`sed -n -r "s/${PVID}/\4/p" ${project_file}`
         pre=`sed -n -r "s/${PVID}/\5/p" ${project_file}`
         if [[ "${DEBUG}" == true ]] ; then printDebug "Pre-Type And Version: ${pre_type}${pre}" ; fi

         if [[ -n "${pre_type}" && -n "${pre}" ]]
         then

            # Increment the internal value
            if [[ "${inc_pre}" == true ]]
            then
               pre=$((${pre} + 1))
               if [[ "${DEBUG}" == true ]] ; then printDebug "Incremented Pre Version: ${pre}" ; fi
            fi

         fi

      else

         if [[ "${DEBUG}" == true ]] ; then printDebug "Pre Value Supplied: ${pre}" ; fi

         # Check that a pre-type was specified
         if [[ -z "${pre_type}" ]]
         then

            printError "A pre-type must be specified along woth a pre verison"
            exit 1

         fi

      fi

   fi


   # ╔════════════════════════════════════════════════════════════════════════╗
   # ║                      Process the Post information                      ║
   # ╚════════════════════════════════════════════════════════════════════════╝
   if [[ "${no_post}" == true ]]
   then

      if [[ "${DEBUG}" == true ]] ; then printDebug "Suppressing post-type and value" ; fi
      post_type=""
      post=""

   else

      # Check for empty value (non-empty value means user input a value)
      if [[ -z "${post}" ]]
      then

         # Only process the values in setup file if the user didn't input a value
         if [[ "${DEBUG}" == true ]] ; then printDebug "Reading Post Version From: ${project_file}" ; fi

         # Retrieve the current value
         post_type=`sed -n -r "s/${PVID}/\6/p" ${project_file}`
         post=`sed -n -r "s/${PVID}/\7/p" ${project_file}`
         if [[ "${DEBUG}" == true ]] ; then printDebug "Post Version: ${post_type}${post}" ; fi

         if [[ -n "${post_type}" && -n "${post}" ]]
         then

            # Increment the internal value
            if [[ "${inc_post}" == true ]]
            then
               post=$((${post} + 1))
               if [[ "${DEBUG}" == true ]] ; then printDebug "Incremented Post Version: ${post}" ; fi
            fi

         fi

      else

         if [[ "${DEBUG}" == true ]] ; then printDebug "Post Value Supplied: ${post}" ; fi

         # Add post "type" here
         post_type=".post"

      fi

   fi


   # ╔════════════════════════════════════════════════════════════════════════╗
   # ║                       Process the Dev information                      ║
   # ╚════════════════════════════════════════════════════════════════════════╝
   if [[ "${dev}" == true ]]
   then

      if [[ "${DEBUG}" == true ]] ; then printDebug "Suppressing dev-type and value" ; fi
      dev_type=""
      dev=""

   else

      # Check for empty value (non-empty value means user input a value)
      if [[ -z "${dev}" ]]
      then

         # Only process the values in setup file if the user didn't input a value
         if [[ "${DEBUG}" == true ]] ; then printDebug "Reading Dev Version From: ${project_file}" ; fi

         # Retrieve the current value
         dev_type=`sed -n -r "s/${PVID}/\8/p" ${project_file}`
         dev=`sed -n -r "s/${PVID}/\9/p" ${project_file}`
         if [[ "${DEBUG}" == true ]] ; then printDebug "Dev Version: ${dev_type}${dev}" ; fi

         if [[ -n "${dev_type}" && -n "${dev}" ]]
         then

            # Increment the internal value
            if [[ "${inc_dev}" == true ]]
            then
               dev=$((${dev} + 1))
               if [[ "${DEBUG}" == true ]] ; then printDebug "Incremented Dev Version: ${dev}" ; fi
            fi

         fi

      else

         if [[ "${DEBUG}" == true ]] ; then printDebug "Dev Value Supplied: ${dev}" ; fi

         # Add dev "type" here
         dev_type=".dev"

      fi

   fi

   # Create the new public version identifier
   NEW_PVID="version = \"${major}.${minor}.${micro}${pre_type}${pre}${post_type}${post}${dev_type}${dev}\""
}


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     updateVersion                                                                                                         ║
# ║                                                                                                                               ║
# ║ @brief  Function to scan the project file and update the version data for the individual elements                             ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
updateVersion()
{
   printInfo "Updating project file with new public version identifier"
   printInfo "New Public Version Identifier: ${NEW_PVID}"

   # Update the version data in place
   # NOTE: The key/value pair is included in the regex of both the existing and the new public version identifiers
   sed -i -r "s/${PVID}/${NEW_PVID}/" "${project_file}"
}


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     Usage                                                                                                                 ║
# ║                                                                                                                               ║
# ║ @brief  Function that displays the operation of the script                                                                    ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
usage()
{
   # All tab characters that begin the line will be ignored in the output
   #    https://en.wikipedia.org/wiki/Here_document#Unix_shells
   cat <<-EOF
	Usage: `basename "$0"` OPERATION [OPTION(S)...]

	OPERATIONS

	   build
	      Build the project


	OPTIONS

	   ========== Build Options ==========

	   --proj-file <arg>
	      String value representing the name of the project file
	         Default: ${default_project_file}

	   --pre-type <arg>
	      String value representing the type of pre-release build
            Valid Values: a, b, rc

	   --no-pre
	      Flag to suppress the pre element and version during build
	         Default: ${default_no_pre}

	   --no-post
	      Flag to suppress the post element and version during build
	         Default: ${default_no_post}

	   --no-dev
	      Flag to suppress the dev element and version during build
	         Default: ${default_no_dev}


	   ========== Version Increment Options ==========

	   -M, --inc-major
	      Increment the existing major version by one
            Mutually exclusive with --major

	   -m, --inc-minor
	      Increment the existing minor version by one
            Mutually exclusive with --minor

	   -u, --inc-micro
	      Increment the existing micro version by one
            Mutually exclusive with --micro

	   -p, --inc-pre
	      Increment the existing pre version by one
            Mutually exclusive with --pre

	   -P, --inc-post
	      Increment the existing post version by one
            Mutually exclusive with --post

	   -d, --inc-dev
	      Increment the existing dev version by one
            Mutually exclusive with --dev


	   ========== Version Options ==========

	   --major <arg>
	      Use the supplied value as the major version
            Valid Values: Positive integer values
            Mutually exclusive with -M, --inc-major

	   --minor <arg>
	      Use the supplied value as the minor version
            Valid Values: Positive integer values
            Mutually exclusive with -m, --inc-minor

	   --micro <arg>
	      Use the supplied value as the micro version
            Valid Values: Positive integer values
            Mutually exclusive with -u, --inc-micro

	   --pre <arg>
	      Use the supplied value as the pre version
            Valid Values: Positive integer values
            Mutually exclusive with -p, --inc-pre

	   --post <arg>
	      Use the supplied value as the post version
            Valid Values: Positive integer values
            Mutually exclusive with -P, --inc-post

	   --dev <arg>
	      Use the supplied value as the dev version
            Valid Values: Positive integer values
            Mutually exclusive with -d, --inc-dev


	   ========== Automation Options ==========

	   --auto
	      Flag denoting that the script is being executed in an automated environment


	   ========== Information Commands ==========

	   -h, --help
	      Display usage information (this text)

	   -v, --version
	      Display version information


	NOTES

	   Script to version/build both a source and binaruy distribution for a python project


	Examples:

	   # Build the project, increment the dev version
	   `basename "$0"` build -d

	   # Build the project, tagged as version 1.4.7.dev5
	   `basename "$0"` build --major 1 --minor 4 --micro 7 --dev 5

	   # Build the project, tagged as version 5.2.1, suppress all modifiers (i.e. pre, post, dev)
	   `basename "$0"` build --major 5 --minor 2 --micro 1 --no-pre --no-post --no-dev

	   # Build the project, in an automated environment, tagged as verison 8.3.5rc2
	   `basename "$0"` build --major 8 --minor 3 --micro 5 --pre-type rc --pre 2 --auto

	EOF
}


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                                                                                               ║
# ║                                                ===  Script Execution Point ===                                                ║
# ║                                                                                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
# Ensure the command line was called with parameters
if [[ $# -eq 0 ]]
then
   usage
   exit 1
fi

# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                Command Line Processor Options                                                 ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

# Define the allowed command line options
# NOTE: The leading - in shortopts is used to allow processing of each non-option argument (values without a leading - or --)
#       as if they were arguments of an option with the character code of 1. In other words, we can mix and match three
#       different types of arg/val pairs (-arg val, --arg val, and arg val)
shortopts="-:dhmMpPu012"

# ------ Operations ------
longopts="build"


# ------ Build Options ------
longopts="${longopts},proj-file:,pre-type:,no-pre,no-post,no-dev"


# ------ Version Increment Options ------
longopts="${longopts},inc-major,inc-minor,inc-micro,inc-pre,inc-post,inc-dev"


# ------ Version Options ------
longopts="${longopts},major:,minor:,micro:,pre:,post:,dev:"


# ----- Automation Options -----
longopts="${longopts},auto"


# ----- Information Options -----
longopts="${longopts},help,version"


# Read the command line options and verify that there was no processing error
OPTS=`getopt -o $shortopts  -l $longopts -- "$@"`
if [[ $? != 0 ]]
then
   usage
   exit 1
fi


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                         Command Line Processor: Configuration Options                                         ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

# Process the command line arguments to extract configuratiuon options
eval set -- "$OPTS"

# Process the configuration options
while true
do
   case "$1" in

      # ====== Debug Options ======

      # Configure the debug option
      -0) DEBUG=true ; shift ;;

      # Configure the extra-debug option
      -1) DEBUG=true ; EXTRA_DEBUG=true ; shift ;;

      # Configure the display=debug option
      -2) DEBUG=true ; shift ;;


      # ====== Build Options ======

      # Configure the proj-file option
      --proj-file)
         case "$2" in
            "") shift 2 ;;
             *)
                # Use the supplied value
                proj_file="${2}"
                shift 2
                ;;
         esac
         ;;

      # Configure the pre-type option
      --pre-type)
         case "$2" in
            "") shift 2 ;;
             *)
                # Use the supplied value
                if [[ "${2}" == "a" || "${2}" == "b" || "${2}" == "rc" ]]
                then
                   pre_type="${2}"
                else
                   printError "Invalid pre-type option:" "${2}"
                   exit 1
                fi
                shift 2
                ;;
         esac
         ;;

      # Configure the no-pre option
      --no-pre) no_pre=true ; shift ;;

      # Configure the no-post option
      --no-post) no_post=true ; shift ;;

      # Configure the no-dev option
      --no-dev) no_dev=true ; shift ;;


      # ====== Version Increment Options ======

      # Configure the inc-major option
      -M|--inc-major) inc_major=true ; shift ;;

      # Configure the inc-minor option
      -m|--inc-minor) inc_minor=true ; shift ;;

      # Configure the inc-micro option
      -u|--inc-micro) inc_micro=true ; shift ;;

      # Configure the inc-pre option
      -p|--inc-pre) inc_pre=true ; shift ;;

      # Configure the inc-post option
      -P|--inc-post) inc_post=true ; shift ;;

      # Configure the inc-dev option
      -d|--inc-dev) inc_dev=true ; shift ;;


      # ====== Version Options ======

      # Configure the major option
      --major)
         case "$2" in
            "") shift 2 ;;
             *)
                # Use the supplied value
                if [[ "${2}" =~ ^[0-9]+$ ]]
                then
                   major="${2}"
                else
                   printError "Invalid major option:" "${2}"
                   exit 1
                fi
                shift 2
                ;;
         esac
         ;;

      # Configure the minor option
      --minor)
         case "$2" in
            "") shift 2 ;;
             *)
                # Use the supplied value
                if [[ "${2}" =~ ^[0-9]+$ ]]
                then
                   minor="${2}"
                else
                   printError "Invalid minor option:" "${2}"
                   exit 1
                fi
                shift 2
                ;;
         esac
         ;;

      # Configure the micro option
      --micro)
         case "$2" in
            "") shift 2 ;;
             *)
                # Use the supplied value
                if [[ "${2}" =~ ^[0-9]+$ ]]
                then
                   micro="${2}"
                else
                   printError "Invalid micro option:" "${2}"
                   exit 1
                fi
                shift 2
                ;;
         esac
         ;;

      # Configure the pre option
      --pre)
         case "$2" in
            "") shift 2 ;;
             *)
                # Use the supplied value
                if [[ "${2}" =~ ^[0-9]+$ ]]
                then
                   pre="${2}"
                else
                   printError "Invalid pre option:" "${2}"
                   exit 1
                fi
                shift 2
                ;;
         esac
         ;;

      # Configure the post option
      --post)
         case "$2" in
            "") shift 2 ;;
             *)
                # Use the supplied value
                if [[ "${2}" =~ ^[0-9]+$ ]]
                then
                   post="${2}"
                else
                   printError "Invalid post option:" "${2}"
                   exit 1
                fi
                shift 2
                ;;
         esac
         ;;

      # Configure the dev option
      --dev)
         case "$2" in
            "") shift 2 ;;
             *)
                # Use the supplied value
                if [[ "${2}" =~ ^[0-9]+$ ]]
                then
                   dev="${2}"
                else
                   printError "Invalid dev option:" "${2}"
                   exit 1
                fi
                shift 2
                ;;
         esac
         ;;


      # ====== Automation Options ======

      # Configure the auto option
      --auto) auto=true ; shift ;;


      # End the processing when we get to a -- with no options
      --) shift ; break ;;


      # If the command line parameter is not listed, keep processing
       *) shift ;;

   esac
done


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                               Command Line Processor: Functions                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

# Process the command line arguments to execute functions
eval set -- "$OPTS"

# Process the functions
while true
do
   case "$1" in

      # Display The Value Of All Script Variables
      -2) displayDebug ;            exit 0  ;;

      # Build Options To Ignore
      --proj-file)                  shift 2 ;;
      --pre-type)                   shift 2 ;;
      --no-pre)                     shift   ;;
      --no-post)                    shift   ;;
      --no-dev)                     shift   ;;

      # Version Increment Options To Ignore
      -M|--inc-major)               shift   ;;
      -m|--inc-minor)               shift   ;;
      -u|--inc-micro)               shift   ;;
      -p|--inc-pre)                 shift   ;;
      -P|--inc-post)                shift   ;;
      -d|--inc-dev)                 shift   ;;

      # Version Increment Options To Ignore
      --major)                      shift   ;;
      --minor)                      shift   ;;
      --micro)                      shift   ;;
      --pre)                        shift   ;;
      --post)                       shift   ;;
      --dev)                        shift   ;;

      # Automation Options To Ignore
      --auto)                       shift   ;;


      # Operations
      build) buildWheel ;           exit $? ;;


      # Display the script usage
      -h|--help) usage ; exit 0 ;;


      # End the processing when we get to a -- with no options
      --) shift ; break ;;


      # Catch for any unknown command line parameters
       *) usage ; exit 0 ;;

   esac
done













