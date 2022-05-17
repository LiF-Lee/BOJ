txt = `
"데이터, 이것은 분리되면 안된다",12,"아무것도 없다","요기도,있지롱",38474
`
regex = /(\".*?\")|\,/g
replace_txt = txt.replace(regex, (...m) => m[1] || '\n')
console.log(replace_txt)

