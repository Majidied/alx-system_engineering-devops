#!/usr/bin/env ruby
puts ARGV[0]&.match(/School/) ? "#{ARGV[0]}$" : '$'