def contain_virus(grid)
  row_length = grid.length
  column_length = grid[0].length
  row_num = 0
  walls_built = 0

  grid.each do |row|
    column_num = 0
    row.each do |element|
      if element == 1
        walls_built += 4
        if (row_num<=row_length && row_num>=0) && (column_num-1<column_length && column_num-1>=0)
          if (grid[row_num])[column_num-1] == 1
            walls_built -= 1
          end
        end
        if (row_num<=row_length && row_num>=0) && (column_num+1<column_length && column_num+1>=0)
          if (grid[row_num])[column_num+1] == 1
            walls_built -= 1
          end
        end
        if (row_num-1<=row_length && row_num-1>=0) && (column_num<column_length && column_num>=0)
          if (grid[row_num-1])[column_num] == 1
            walls_built -= 1
          end
        end
        if (row_num+1<row_length && row_num+1>=0) && (column_num<column_length && column_num>=0)
          if (grid[row_num+1])[column_num] == 1
            walls_built -= 1
          end
        end
      else
      end
      column_num += 1
    end
    row_num += 1
  end
  walls_built
end

isInfected = [[1,1,1,1],[0,0,0,1],[0,0,0,1],[0,0,0,1],[0,0,0,1]]
# Call the function and store the result in a variable
result = contain_virus(isInfected)
# Print the result
puts "Number of walls needed: #{result}"