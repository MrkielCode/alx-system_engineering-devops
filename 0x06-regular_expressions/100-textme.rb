#!/usr/bin/env ruby

match = ARGV[0].match(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)

if match
  from = match[1]
  to = match[2]
  flags = match[3]
  puts "#{from},#{to},#{flags}"
end
