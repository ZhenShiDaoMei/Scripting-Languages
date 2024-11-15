require 'set'
class Region
        attr_accessor :infected, :uninfected, :walls
        
        def initialize
            @infected = Set.new
            @uninfected = Set.new
            @walls = 0
        end
    end

def contain_virus_bonus(is_infected)
end

# Example input, where 1 represents infected cells and 0 represents uninfected cells:
# isInfected = [
#   [0, 1, 0, 0, 1],
#   [0, 1, 0, 0, 1],
#   [0, 0, 0, 0, 1]
# ]

isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]

# Call the function and store the result in a variable
result = contain_virus_bonus(isInfected)

# Print the result
puts "Number of walls needed: #{result}"