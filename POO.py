#Programação Orientada a Objetos (POO) é um estilo ou paradigma de programação, não uma linguagem específica.
# Ela é uma forma de organizar e estruturar o código para solucionar problemas de um jeito mais próximo de como o mundo real funciona.
# Os dois conceitos-chave para aprender POO são: classes e objetos.
#=========================================================================================================================================

# Alguns paradigmas:
# - Imperativo ou procedural
# - Funcional
# - Orientado a eventos

#=========================================================================================================================================

# Classe: define características e comportamentos de um objeto; porém, não conseguimos utilizá-la diretamente, pois é abstrata.
# Objetos: podemos usá-los e eles possuem as características e comportamentos que foram definidos nas classes.

#=========================================================================================================================================

# Exemplo:
# Classe Casa: define as características que toda casa deve ter, como número de quartos, cor da parede, tipo de telhado, e os comportamentos, como abrir a porta, ligar a luz.
# Objeto Casa 1: uma casa específica construída usando esse projeto, por exemplo, uma casa com 3 quartos, paredes azuis e telhado de cerâmica.
# Objeto Casa 2: outra casa construída usando o mesmo projeto, mas com 2 quartos, paredes brancas e telhado metálico.

#=========================================================================================================================================

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print(f"{self.nome} diz: Auau!")

    def dormir(self):
        if self.acordado:
            self.acordado = False
            print(f"{self.nome} está dormindo... Zzzz...")
        else:
            print(f"{self.nome} já está dormindo.")

    def acordar(self):
        if not self.acordado:
            self.acordado = True
            print(f"{self.nome} acordou!")
        else:
            print(f"{self.nome} já está acordado.")

# Criando objetos Cachorro
cao_1 = Cachorro("Billy", "preto-branco", False)
cao_2 = Cachorro("Theo", "marrom-preto")  # acordado = True por padrão
cao_3 = Cachorro("Yuri", "branco-preto", False)

# Ações dos cães
cao_1.latir()

print(f"Antes de dormir, {cao_2.nome} está acordado? {cao_2.acordado}")
cao_2.dormir()
print(f"Depois de dormir, {cao_2.nome} está acordado? {cao_2.acordado}")
print(f"Antes de dormir, {cao_3.nome} está acordado? {cao_3.acordado}")
cao_3.dormir()

# Teste método acordar
cao_2.acordar()

#=========================================================================================================================================
class Carro:
    def __init__(self, cor, modelo, ano, valor, placa, sinal_fechado = True):
        self.cor = cor
        self.modelo = modelo 
        self.ano = ano
        self.valor = valor 
        self.placa = placa
        self.sinal_fechado = sinal_fechado

    def buzinar(self):
        print("Carros buzinando bi - bi - bi")

    def abrir_sinal(self):
        if self.sinal_fechado:
            self.sinal_fechado = False
            print("Carros estão passando enquanto o sinal está aberto.")
        else:
            print("O sinal já está aberto.")


    def fechar_sinal(self):
        if not self.sinal_fechado:
            self.sinal_fechado = True
            print("Sinal fechado, carros agurdando o sinal abrir.")
        else:
            print(f"Mesmo com o sinal fechado o carro da cor {self.cor}, modelo {self.modelo}, ano de {self.ano}, com o número da placa {self.placa} , avançou o sinal, multar no valor de {self.valor}")

carro = Carro("Prata", "Audi A3", "2016", "R$ 500,00", "ABC-123")
carro1 = Carro("Preto", "Audi A3", "2016", "R$ 600,00", "ABC-123" , False)

print(f"O sinal está aberto? {carro1.sinal_fechado}")
carro.buzinar()
carro.fechar_sinal()
print(f"O sinal está aberto? {carro.sinal_fechado}")
carro.abrir_sinal()
carro.abrir_sinal()
carro1.fechar_sinal()
carro1.fechar_sinal()

#=========================================================================================================================================

#Método construtor -> Sempre é executado quando uma nova instância da classe é criada. 
#Para declarar o método construtor da classe, criamos um método com o nome __init__.

# class Carro:
    #def __init__(self, cor, modelo, ano, valor, placa, sinal_fechado = True):
        #self.cor = cor
        #self.modelo = modelo 
        #self.ano = ano
        #self.valor = valor 
        #self.placa = placa
        #self.sinal_fechado = sinal_fechado


# Método destrutor -> Sempre é executado quando uma instância é destrída.
# Para declarar o método destrutor da classe, criamos um método com o nome __del__.

# class Carro:
    #def__del__(self):
        #print("Destruindo a instância")

#c = Carro()
#del c

#=========================================================================================================================================

class Fruta:
    def __init__(self, nome, citrica, doce):
        print("Inicializando a classe...")
        self.nome = nome
        self.citrica = citrica
        self.doce = doce

    def __del__(self):
        print(f"Removendo a instância da fruta {self.nome}.")

# Criando objetos
laranja = Fruta("Laranja", citrica=True, doce=False)
manga = Fruta("Manga", citrica=False, doce=True)

# Usando os objetos
print(f"{laranja.nome} é cítrica? {laranja.citrica}")
print(f"{manga.nome} é doce? {manga.doce}")

# Removendo apenas após o uso
del laranja  # Aqui o destrutor será chamado

# manga ainda pode ser usada
print(f"{manga.nome} é doce? {manga.doce}")


#=========================================================================================================================================