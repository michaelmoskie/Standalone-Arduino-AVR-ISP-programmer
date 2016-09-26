#Convert intel hex files to strings that can be used with Adafruit's standalone programmer
#- Place your hex file in this folder, and name it 'input.hex'
#- Copy the content of output.txt to the images.cpp file
hexfile = open('input.hex','r')
outtext = open('output.txt','w')
for line in hexfile:
	newline = '\"'+line[0:len(line)-2]+"\\n"+'\"'+"\n"
	outtext.write(newline)
hexfile.close()
outtext.close()