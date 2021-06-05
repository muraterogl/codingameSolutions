a = gets.split.map &:to_i
b = gets.split.map &:to_i
result = 0

while a.size > 0 do
    factor = [a[0], b[0]].min
    result += factor * a[1] * b[1]
    a[0] -= factor
    b[0] -= factor
    a = a[2..] if a[0] == 0
    b = b[2..] if b[0] == 0 
end

puts result