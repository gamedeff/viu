# -*- coding: utf-8 -*-
import sys,os,re,optparse
from PIL import Image

def parseopt(arg):
    usage = "usage: %prog [options] picture."
    parser = optparse.OptionParser(usage=usage)
    parser.add_option('-i','--ipicture',action='store_const', const='i', dest='check', help='Upload to ipicture.ru')
    parser.add_option('-r','--radikal',action='store_const', const='r', dest='check', help='Upload to radikal.ru')
    parser.add_option('-f','--funkyimg',action='store_const', const='f', dest='check', help='Upload to funkyimg.com')
    parser.add_option('-n','--name',action='store', default='Apkawa', dest='name', help='Add name in tumbinals')
    opt, arguments = parser.parse_args(args=arg,)
    try:
        name = arguments[0]
    except IndexError:
        parser.print_help()
        print "No parametrs. "
        sys.exit()
    return opt, arguments

def label(file):
    name=file[1]
    img=Image.open(file[0])
    size=os.stat(file[0]).st_size/1024
    #title=[name,'',img.size[0],'x',img.size[1],' ',size,'Kb']
    title=name+' '+str(img.size[0])+'x'+str(img.size[1])+' '+str(size)+' Kb'
    return title
def ipicture(img):
    refurl=re.findall('http://.*.html',os.popen('curl  -i  \
    -F uploadtype=1 \
    -F name="userfile" \
    -F method="file" \
    -F string_small_on="on" -F string_small="'+label(img)+'"\
    -F filename=@"'+img[0]+'" \
    -F thumb_resize_on="on" \
    -F thumb_resize=200 http://ipicture.ru/Upload/').read())
    url=re.findall('\[IMG\](http://.*)\[\/IMG\]',os.popen('curl '+refurl[0]).read())
    return url
def radikal(img):
    url=re.findall('\[IMG\](http://.*.radikal.ru.*)\[/IMG\]', os.popen('curl -F upload=yes \
    -F F=@"'+img[0]+'" -F VM=200 \
    -F VE=yes -F V="'+label(img)+'"\
    -F CP=yes \
    -F Submit="Загрузить"\
    http://www.radikal.ru/action.aspx').read())
    return url
def funkyimg(img):
    url=re.findall('\[IMG\](http://funkyimg.com/.*)\[/IMG\]\[/URL\]',os.popen('curl \
    -F uptype=file \
    -F addInfo=on -F addInfoType=label -F labelText="'+label(img)+'" \
    -F file="@'+img[0]+'"\
    -F url="" -F MAX_FILE_SIZE=3145728 \
    -F upload="Upload Image" http://funkyimg.com/up.php').read()) 
    url.reverse()
    return url 

def main(arg):
    opt, arguments=parseopt(arg)
    i=0
    tmpurl1 = tmpurl2 = tmpurl3 = tmpurl4 = ''
    host=opt.check
    while i < len(arguments):
        send=[arguments[i],opt.name]
        if host == 'i':
            url=ipicture(send)
        if host == 'r':
            url=radikal(send)
        if host == 'f':
            url=funkyimg(send)
    
        i=i+1
        tmpurl1=tmpurl1+url[0]+'\n'
        tmpurl2=tmpurl2+'[URL='+url[0]+'][IMG]'+url[1]+'[/IMG][/URL] '
        
    print tmpurl1
    print tmpurl2+'\n'
    return None

main(sys.argv)