w,h=gets.split.map &:to_i
step=gets.to_i
obs=[]
cy=cx=-1
d=0
dd=->{[[-1,0],[0,1],[1,0],[0,-1]][d]}
seen={}
(0...h).each do |y|
    row = gets
    (0...w).each do |x|
        if row[x]==?#
            obs << [y,x]
        elsif row[x]==?O
            cy=y
            cx=x
        end
    end
end

while step>0
    dy,dx=dd[]
    while obs.include?([cy+dy, cx+dx])
        d = (d+1)%4
        dy,dx=dd[]
    end
    cy+=dy
    cx+=dx
    step-=1
    if seen.has_key?([cy,cx,d])
        prev_step = seen[[cy,cx,d]]
        step %= prev_step-step
    else
        seen[[cy,cx,d]]=step
    end
end

puts [cx,cy]*" "
