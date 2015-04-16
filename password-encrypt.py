cipher = {'0':'1','1':'2','2':'3','3':'4','4':'5','5':'6','6':'7','7':'8',
          '8':'9','9':'a','a':'b','b':'c','c':'d','d':'e','e':'f','f':'g',
          'g':'h','h':'i','i':'j','j':'k','k':'l','l':'m','m':'n','n':'o',
          'o':'p','p':'q','q':'r','r':'s','s':'t','t':'u','u':'v','v':'w',
          'w':'x','x':'y','y':'z','z':'A','A':'B','B':'C','C':'D','D':'E',
          'E':'F','F':'G','G':'H','H':'I','I':'J','J':'K','K':'L','L':'M',
          'M':'N','N':'O','O':'P','P':'Q','Q':'R','R':'S','S':'T','T':'U',
          'U':'V','V':'W','W':'X','X':'Y','Y':'Z','Z':'!','!':'"','"':'#',
          '#':'$','$':'%','%':'&','&':'\'','\'':'(','(':')',')':'*','*':'+',
          '+':',',',':'-','-':'.','.':'/','/':':',':':';',';':'<','<':'=',
          '=':'>','>':'?','?':'@','@':'[','[':'\\','\\':']',']':'^','^':'_',
          '_':'`','`':'{','{':'|','|':'}','}':'~','~':' ',' ':'\t','\t':'\n',
          '\n':'\r','\r':'','':'','':'0'}
plainFile = open("c0d3sPl41n.txt", 'r')
plainText = plainFile.read()
cipherText = ""
for i in plainText:
    cipherText += cipher[i]
cipherFile = open("c0d3sC1ph3r.txt", 'w')
cipherFile.write(cipherText)

# You will need to manually add the instance of ' '
def printEncrypt():
	import string
	output = "decipher = {"
	for i in range(len(string.printable) - 1):
		first = string.printable[i]
		second = string.printable[i + 1]
		if first == '\\':
			first =  '\\\\'
		if second == '\\':
			second = '\\\\'
		if first == '\'':
			first = '\\\''
		if second == '\'':
			second = '\\\''
		if first == '\n':
			first = '\\n'
		if second == '\n':
			second = '\\n'
		if first == '\t':
			first = '\\t'
		if second == '\t':
			second = '\\t'
		if first == '\r':
			first = '\\r'
		if second == '\r':
			second = '\\r'
		output += "'" + first + "':'" + second + "',"
	output += "'" + string.printable[len(string.printable) - 1] + "':'" + string.printable[0] + "'}"
	print output
