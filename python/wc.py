"""
    _summary_ :  This challenge is to build your own version of the Unix command line tool wc!

    Functional Requirement : 
        WC(1)                      General Commands Manual                      WC(1)

NAME
     wc – word, line, character, and byte count

SYNOPSIS
     wc [--libxo] [-Lclmw] [file ...]

DESCRIPTION
     The wc utility displays the number of lines, words, and bytes contained
     in each input file, or standard input (if no file is specified) to the
     standard output.  A line is defined as a string of characters delimited
     by a ⟨newline⟩ character.  Characters beyond the final ⟨newline⟩
     character will not be included in the line count.

     A word is defined as a string of characters delimited by white space
     characters.  White space characters are the set of characters for which
     the iswspace(3) function returns true.  If more than one input file is
     specified, a line of cumulative counts for all the files is displayed on
     a separate line after the output for the last file.

     The following options are available:

     --libxo
             Generate output via libxo(3) in a selection of different human
             and machine readable formats.  See xo_parse_args(3) for details
             on command line arguments.

     -L      Write the length of the line containing the most bytes (default)
             or characters (when -m is provided) to standard output.  When
             more than one file argument is specified, the longest input line
             of all files is reported as the value of the final “total”.

     -c      The number of bytes in each input file is written to the
             standard output.  This will cancel out any prior usage of the -m
             option.

     -l      The number of lines in each input file is written to the
             standard output.

     -m      The number of characters in each input file is written to the
             standard output.  If the current locale does not support
             multibyte characters, this is equivalent to the -c option.  This
             will cancel out any prior usage of the -c option.

     -w      The number of words in each input file is written to the
             standard output.

     When an option is specified, wc only reports the information requested
     by that option.  The order of output always takes the form of line,
     word, byte, and file name.  The default action is equivalent to
 """
 
 
 