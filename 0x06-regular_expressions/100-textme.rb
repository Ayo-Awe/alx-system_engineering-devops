#!/usr/bin/env ruby

to = ARGV[0].scan(/\[to:\+?[0-9A-Za-z]*\]/).join
from = ARGV[0].scan(/\[from:\+?[0-9A-Za-z]*\]/).join
flags = ARGV[0].scan(/\[flags:[*-1:0]*\]/).join

# Remove descriptors
to["[to:"] = ""
to["]"]=""
flags["[flags:"] = ""
flags["]"]=""
from["[from:"] = ""
from["]"]=""

# Format message
message = "%s,%s,%s" % [from,to,flags]

# Print message
puts message

