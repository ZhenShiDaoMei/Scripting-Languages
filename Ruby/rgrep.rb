#!/usr/bin/env ruby
# args = ARGF.argv
args = ARGV
option_list = []
pattern = nil
pattern_count = 0

def error_message(message)
  puts message
  exit(1)
end

if ARGV.length < 2
  error_message("Missing required arguments")
end

file_name = ARGV[0]

ARGV.each_with_index do |arg, index|
  case arg
  when '-w', '-p', '-v', '-c', '-m'
    option_list << arg
  else
    if arg.start_with?('-')
      error_message("Invalid option")
    end
    unless arg.include?(".txt")
      pattern = arg
      pattern_count += 1
    end
  end
end

if pattern_count > 1
  error_message("Invalid option") #can only have 1 pattern
end
if pattern_count == 0
  error_message("Missing required arguments")
end

if (option_list.include?('-c') && !(option_list.include?('-w') || option_list.include?('-p') || option_list.include?('-v'))) ||
  (option_list.include?('-m') && !(option_list.include?('-w') || option_list.include?('-p'))) ||
  (option_list.include?('-v') && option_list.include?('-m'))
  error_message("Invalid combination of options")
end

option_list << '-p' if option_list.empty?
file_lines = File.readlines(file_name)
case option_list.first
when '-w'
  pattern = /\b#{Regexp.escape(pattern)}\b/
  result = file_lines.select { |line| line.match(pattern) }
when '-p'
  result = file_lines.select { |line| line.match(/#{pattern}/)}
when '-v'
  result = file_lines.reject { |line| line.match(/#{pattern}/) }
end

if option_list.include?('-c')
  puts result.length
elsif option_list.include?('-m')
  matched = result.map { |line| line.scan(/#{pattern}/).join(' ')}
  puts matched
else
  puts result
end