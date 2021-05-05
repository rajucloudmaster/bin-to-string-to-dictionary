data1 = b'{"Data":[],"Total":140,"AggregateResults":null,"Errors":null}'
str = data1.decode("UTF-8")

Dict = dict((x.strip(), y.strip())
            for x, y in (element.split(':')
                         for element in str.split(',')))

print("the Total value  is-------**************************************-----> ", Dict.get('"Total"'))
