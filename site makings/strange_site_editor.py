css_file = open('test.css', 'w+')

css_file.write('.aa{margin:-2px;transition:3s all;width:10px;height:300px;}\n'
               '.aa1{color:red;background-color:red;}\n'
               '.aa2{color:blue;background-color:blue;}\n'
               '.aa3{color:yellow;background-color:yellow;}\n'
               '.aa4{color:green;background-color:green;}\n'
               '.borderer{border-bottom:2px solid #000000;\n'
               '    border-right:2px solid #000000;\n'
               '    border-left:2px solid #E1E1E1;\n'
               '    border-top:2px solid #E1E1E1;}\n'
               '.hop:hover{color:black;\n'
               '    background-color:black;\n'
               )

css_file.close()

htmlfile = open('test.html', 'w+')
stroka=''
list = ['aa1', 'aa2', 'aa3', 'aa4']
stroka1='        <h class="borderer aa hop '
stroka2='">_</h>'
for x in range(10000):
    stroka=stroka+stroka1+list[x%4]+stroka2+'\n'

htmlfile.write('<!DOCTYPE html>\n'
                   '<html>\n'
                   '    <head>\n'
                   '        <meta charset="UTF-8"/>\n'
                   '        <title>Site</title>\n'
                   '        <link href="test.css" rel="stylesheet" type="text/css" />\n'
                   '    </head>\n'
                   '    <body>\n'
                   +stroka+
                   '    </body>\n'
                   '</html>')

htmlfile.close()
