class Array
  alias_method :oldBracket, :[]
  def [](index)
    if index >= size || index < -size
      return '\0'
    end
    oldBracket(index)
  end

  alias_method :oldMap, :map
  def map(sequence = nil, &block)
    if sequence == nil?
      oldMap(&block)
    else
      result = []
      sequence.to_a.each do |index|
        next if index >= size || index < -size
        result << yield(self[index])
      end
      result
    end
  end
end