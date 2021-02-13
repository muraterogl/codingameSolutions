const operation = readline()
const pseudoRandomNumber = parseInt(readline())
const shifts = []
for (let i = 0; i < 3; i++) {
    shifts.push(readline())
}
const message = readline();

if(operation==="ENCODE"){
    var m = message.split('').map((c,i)=>String.fromCharCode((c.charCodeAt()+pseudoRandomNumber+i-65)%26+65))
    shifts.forEach(s=>{
        m = m.map(c=>s[c.charCodeAt()-65])
    })
    
}
else{
    var m = message.split('')
    shifts.reverse().forEach(s=>{
        m = m.map(c=>String.fromCharCode(s.indexOf(c)+65))
    })
    m = m.map((c,i)=>{
        var n = c.charCodeAt()-pseudoRandomNumber-i-65
        while(n<0) n+=26
        return String.fromCharCode((n)%26+65)
    })
}
console.log(m.join(''))
 
