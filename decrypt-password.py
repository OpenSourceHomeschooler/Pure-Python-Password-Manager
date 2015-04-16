decipher = {'1':'0','2':'1','3':'2','4':'3','5':'4','6':'5','7':'6','8':'7',
          '9':'8','a':'9','b':'a','c':'b','d':'c','e':'d','f':'e','g':'f',
          'h':'g','i':'h','j':'i','k':'j','l':'k','m':'l','n':'m','o':'n',
          'p':'o','q':'p','r':'q','s':'r','t':'s','u':'t','v':'u','w':'v',
          'x':'w','y':'x','z':'y','A':'z','B':'A','C':'B','D':'C','E':'D',
          'F':'E','G':'F','H':'G','I':'H','J':'I','K':'J','L':'K','M':'L',
          'N':'M','O':'N','P':'O','Q':'P','R':'Q','S':'R','T':'S','U':'T',
          'V':'U','W':'V','X':'W','Y':'X','Z':'Y','!':'Z','"':'!','#':'"',
          '$':'#','%':'$','&':'%','\'':'&','(':'\'',')':'(','*':')','+':'*',
          ',':'+','-':',','.':'-','/':'.',':':'/',';':':','<':';','=':'<',
          '>':'=','?':'>','@':'?','[':'@','\\':'[',']':'\\','^':']','_':'^',
          '`':'_','{':'`','|':'{','}':'|','~':'}',' ':'~','\t':' ','\n':'\t',
          '\r':'\n','':'\r','':'','0':''}

cipherFile = open("c0d3sC1ph3r.txt", 'r')
cipherText = cipherFile.read()
plainText = ""
for i in cipherText:
    plainText += decipher[i]
plainFile = open("c0d3sPl41n.txt", 'w')
plainFile.write(plainText)

def printDecrypt():
	import string
	output = "decipher = {"
	for i in range(1, len(string.printable)):
		first = string.printable[i]
		second = string.printable[i - 1]
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
	output += "'" + string.printable[0] + "':'" + string.printable[len(string.printable) - 1] + "'}"
	print output
