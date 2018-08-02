SearchTool.py
================

This script searches the PREEMPT shared drive for files matching keyword
specifications. It begins by allowing you to specify the subdirectories 
within PREEMPT that you'd like to narrow your search to, which speeds up
the searching process. Next, you specify keywords to search with. Keywords
are specified in groups, such that all keywords in a group need to be found
in a filename to match. Multiple groups can be specified, and only one group
need be satisfied to match. Lastly, you specify a file extension to include
in your search.

Currently, matched files are copied to a folder written to the local user's
desktop titled SearchTool_Matches.
