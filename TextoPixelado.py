from PIL import Image
import sys
def help():
    help_text = """
Uso: python TextoPixelado.py [opções] [imagem]

Opções:
  -o CARACTERE  Define o caractere usado para representar cada pixel da imagem. 
                Exemplo: '■', '▒', '░', '█', '□', '●', '○'.
                Valor padrão: '■'.

  -s ARQUIVO     Define o nome do arquivo onde a saída será salva. 
                Se este parâmetro não for fornecido, a saída será apenas exibida no terminal.

  -h             Mostra esta mensagem de ajuda.

Exemplo:
  python TextoPixelado.py imagem.png -o '▒' -s saída.txt

Notas:
  - O script redimensiona a imagem para 75x75 pixels se ela for maior que isso.
  - A imagem será convertida para uma representação de texto usando caracteres e cores ANSI.
  - A imagem deve estar em um formato suportado pelo Pillow (ex: PNG, JPEG).

Para mais informações, consulte o código-fonte do script.
"""
    print(help_text)


# Configurações iniciais
nome_arquivo = ''
caraquiter = '■'
args = sys.argv[1:]

# Processa argumentos
if len(args)==0:
	arquivo = input('nome do arquivo: ')
	args = arquivo.split()
output = []

salvar = False
i = 0
while i < len(args):
    if args[i] == '-o' and i+1 < len(args):
        caraquiter = args[i+1]
        i += 2
    elif args[i] == '-s' and i+1 < len(args):
        nome_arquivo = args[i+1]
        salvar = True
        i += 2
    else:
        i += 1
    
if '-h' in args:
    help()
    sys.exit()

# Abre e redimensiona a imagem
img = Image.open(args[0])
largura, altura = img.size
if largura > 75 or altura >75:
	img = img.resize((75, 75))
largura, altura = img.size




def rgb_to_ansi(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"
    
# Converte a imagem para texto com caracteres ANSI
for a in range(altura):
	line = []
	for l in range(largura):
		pixel = img.getpixel((l, a))
		ansi_color = rgb_to_ansi(pixel[0], pixel[1], pixel[2])
		line.append(f"{ansi_color}{caraquiter}\033[0m")
	output.append(''.join(line))
	
# Exibe o resultado	
print('\n'.join(output))

# Salva o resultado em um arquivo, se necessário
if salvar:
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write('\n'.join(output))