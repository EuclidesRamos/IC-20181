from PIL import Image
import sys
print """
 >>> E necessario instalar a bibliotela PIL primeiro. <<<
 
  ------------------- Instalacao: -------------------
 LINUX: apt-get install python-imaging
 WINDOWS: http://www.pythonware.com/products/pil/#pil117
  ---------------------------------------------------
  
 >>> A imagem deve estar na mesma pasta que este arquivo
 >>> O arquivo deve ser descrito na entrada com o seu nome
 e seu formato, a exemplo: "img.png"
 >>> A imagem de saida sera salva no mesmo diretorio deste
 arquivo.
"""
img = raw_input('Qual o nome da imagem que voce deseja deixar P&B? ')
image = Image.open(img)
pixels = image.load()

for i in range(image.size[0]):
    for j in range(image.size[1]):
		pixel = pixels[i,j]
		l = (int) (pixel[0] * 0.3 + pixel[1] * 0.59 + pixel[2] * 0.11)
		pixels[i,j] = (l, l, l)

image.save("saida.jpg")
print "Veja o resultado em: saida.jpg"
