#!/bin/bash
# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ common-bash-utils.sh                                                                                                          ║
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
# ║                                 Added header, added reference data                                                            ║
# ║                                                                                                                               ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║                                                           Reference                                                           ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║                                                                                                                               ║
# ║                                                                                                                               ║
# ║                                                                                                                               ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║                                                             Notes                                                             ║
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║                                                                                                                               ║
# ║                                                                                                                               ║
# ║                                                                                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
USE_AUTOMATION=false


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     printDebug                                                                                                            ║
# ║                                                                                                                               ║
# ║ @brief  Function to add delimiters and error color tags to a variable for terminal printing                                   ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
printDebug()
{
   echo -e $(printDbgVariable "===== DEBUG:") $(printDbgVariable "${1}") $(printDbgVariable "${2}") $(printDbgVariable "=====")
}


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     printError                                                                                                            ║
# ║                                                                                                                               ║
# ║ @brief  Function to add delimiters and error color tags to a variable for terminal printing                                   ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
printError()
{
   echo -e $(printErrVariable "===== ERROR:") $(printErrVariable "${1}") $(printErrVariable "${2}") $(printErrVariable "=====")
}


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     printInfo                                                                                                             ║
# ║                                                                                                                               ║
# ║ @brief  Function to add delimiters and info color tags to a variable for terminal printing                                    ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
printInfo()
{
   echo -e $(printInfVariable "===== INFO:") $(printInfVariable "${1}") $(printInfVariable "${2}") $(printInfVariable "=====")
}


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     printDbgVariable                                                                                                      ║
# ║                                                                                                                               ║
# ║ @brief  Function to add debug color tags to a variable for terminal printing                                                  ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
printDbgVariable()
{
   if [[ "${USE_AUTOMATION}" ==  true ]]
   then
      echo "$@"
   else
      printf '\033[33m'"$@"'\033[0m'
   fi
}


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     printDbgVariableCentered                                                                                              ║
# ║                                                                                                                               ║
# ║ @brief  Function to add debug color tags and center a variable for terminal printing                                          ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
printDbgVariableCentered()
{
   # Capture the current number of columns on the screen
   COLUMNS=${1}

   # Find the length of the variable
   VARLEN=${#2}

   # Determine the proper location for the display
   CENTER=$((($VARLEN+$COLUMNS)/2))

   # Display the centered variable
   if [[ "${USE_AUTOMATION}" ==  true ]]
   then
      printf "%*s" "${CENTER}" "${2}"
   else
      printf "\033[33m%*s\033[0m" "${CENTER}" "${2}"
   fi
}


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     printErrVariable                                                                                                      ║
# ║                                                                                                                               ║
# ║ @brief  Function to add error color tags to a variable for terminal printing                                                  ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
printErrVariable()
{
   if [[ "${USE_AUTOMATION}" ==  true ]]
   then
      echo "$@"
   else
      printf '\033[31m'"$@"'\033[0m'
   fi
}


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     printInfVariable                                                                                                      ║
# ║                                                                                                                               ║
# ║ @brief  Function to add info color tags to a variable for terminal printing                                                   ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
printInfVariable()
{
   if [[ "${USE_AUTOMATION}" ==  true ]]
   then
      echo "$@"
   else
      printf '\033[92m'"$@"'\033[0m'
   fi
}


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     printInfoVariableIndentedArray                                                                                        ║
# ║                                                                                                                               ║
# ║ @brief  Function to add debug color tags and indent variables in a string array for terminal printing                         ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
printInfoVariableIndentedArray()
{
   # Capture the current number of columns on the screen
   INDENT=${1}

   # Generate an array from the longopts string
   IFS=',' read -r -a longOptsArray <<< "${2}"

   # Display each of the variables from the string array, indented
   for index in "${!longOptsArray[@]}"
   do

      if [[ $index -eq 0 ]]
      then

         # Display the variable, with no indent
         printf "\033[92m%s\033[0m\n" "${longOptsArray[index]}"

      else

         # Display the indented variable
         printf "%*s : \033[92m%-s\033[0m\n" "${INDENT}" " " "${longOptsArray[index]}"

      fi

   done
}


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     printVariableCentered                                                                                                 ║
# ║                                                                                                                               ║
# ║ @brief  Function to center a variable for terminal printing                                                                   ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
printVariableCentered()
{
   # Capture the current number of columns on the screen
   COLUMNS=${1}

   # Find the length of the variable
   VARLEN=${#2}

   # Determine the proper location for the display
   CENTER=$((($VARLEN+$COLUMNS)/2))

   # Display the centered variable
   printf "%*s" "${CENTER}" "${2}"
}
