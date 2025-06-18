from fpdf import FPDF

#Criaçao pdf
pdf = FPDF()
pdf.add_page()
#titulo do pdf
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Meu Projeto - Relatório", ln=True, align='C')
#fonte do pdf
pdf.set_font("Arial", size=12)

#so pra teste mesmo
desc2 = 'A colocar'
nome2 = "sem"

#objetos
projetos = []
reco = []

def projeto_finalizado():
   
   projeto = {
      "Nome": nome2,
      "Descriçao": desc2
   }
   projetos.append(projeto)

   print(projetos)

   dados = reco
   dados2 = projetos
   pdf.ln(10)  # Linha em branco
   pdf.cell(200, 10, txt=f"{dados},{dados2} ", ln=True)
   pdf.output("relatorio.pdf")

def recursosque():

    while True:
       
       recursos = input('Digite os recursos que voçe adicionou, caso queira terminar digite (n) ')
       print(f'Voce adicionou {recursos}')

       if recursos == 'n':
          projeto_finalizado()
          break
       else:
          reco.append(recursos)
          
    
        

while True:
    print("1 - Criar projeto")

    modo = int(input("Digite uma opçao: "))
    print('----------------------')
    
    if modo == 1:
      
      print("Criando projeto...")
      print('projeto criado')
      print('------------------')

      nome2 = str(input("Nome do seu projeto: "))

      print(f'Projeto {nome2}  Descriçao doprojeto {desc2}')
      print('------------------')

      desc2 = str(input("Descriçao do seu projeto: "))

      recursos_cosenquido = input('Voce ja tem algum recurso em maos?(s)/(n)')

      if recursos_cosenquido == 's':
         recursosque()
      else:
         print('------------------')
         print('Sem problema se voce nao tiver')
         print('------------------')

      print('------------------')
    else:
       break
      
        