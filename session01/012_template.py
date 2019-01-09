#templates string substitution

import string

foo=10
bar=3

cad = string.Template('$foo + $bar = $res')

result = cad.safe_substitute(foo=foo, bar=bar, res=foo+bar)

print (result)