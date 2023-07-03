import tkinter as tk

class No:
    def __init__(self, dado):
        self.dado = dado
        self.peso = 0
        self.direita = None
        self.esquerda = None
    
    def __str__(self):
        return str(self.dado)


class Arvore:
    def __init__(self, dado = None):
        self.raiz = No(dado)
        self.len = 0


    def insertData(self, value, no = None):
        if self.raiz.dado is None:
            self.raiz.dado = value
            self.len += 1
            self.peso()
            return
        
        if no is None: no = self.raiz
        
        if value <= no.dado:
            if no.esquerda is None:
                no.esquerda = No(value)
                self.len += 1
                self.peso()
                return
            self.insertData(value, no.esquerda)
        
        if value > no.dado:
            if no.direita is None:
                no.direita = No(value)
                self.len += 1
                self.peso()
                return
            self.insertData(value, no.direita)

    
    def insertArray(self, array):
        for data in array:
            self.insertData(data, self.raiz)


    def peso(self,no = None, start = True):
        if start:
            no = self.raiz

        if no is None:
            return  

        pesoDireita = self.altura(no.direita, 1, False)
        pesoEsquerda = self.altura(no.esquerda, 1, False)

        no.peso = pesoDireita - pesoEsquerda

        self.peso(no.esquerda, False)
        self.peso(no.direita, False)

        if start:
            self.balancear()

    def balancear(self, no = None, father = None, start = True, isLeft = True, continuar = True):
        if start:
            no = self.raiz
        
        if not continuar:
            return

        if no is None:
            return
        
        if not( -1 <= no.peso <= 1):
            if no.peso > 0:
                self.giroEsquerda(no, father, isLeft)
            else:
                self.giroDireita(no, father, isLeft)
            
            self.peso()
            continuar = False
        
        self.balancear(no.esquerda, no, False, True, continuar)
        self.balancear(no.direita, no, False, False, continuar)

    def giroEsquerda(self, no, father, isLeft):
        noA = no
        noB = no.direita
        if noB.peso == -1:
            noB.esquerda.direita = noB
            noA.direita = noB.esquerda
            noB.esquerda = None
            noB = noA.direita

        noA.direita = noB.esquerda
        noB.esquerda = noA

        if father is None:
            self.raiz = noB
        elif isLeft:
            father.esquerda = noB
        else:
            father.direita = noB


    def giroDireita(self, no, father, isLeft):
        noA = no
        noB = no.esquerda

        if noB.peso == 1:
            noA.esquerda = noB.direita
            noA.esquerda.esquerda = noB
            noB.direita = None
            noB = noA.esquerda

        noA.esquerda = noB.direita
        noB.direita = noA

        if father is None:
            self.raiz = noB
        elif isLeft:
            father.esquerda = noB
        else:
            father.direita = noB

    def find(self, value, no = None, start = True):
        if start:
            no = self.raiz

        if no is None:
            return False

        if value < no.dado:
            return self.find(value, no.esquerda, False)
        if value > no.dado:
            return self.find(value, no.direita, False)

        return True
    

    def min(self, no):
        if no.esquerda is None:
            return no.dado
        return self.min(no.esquerda)

    
    def remove(self, value, no = None, father = None, isLeft = True, start = True):
        if start:
            no = self.raiz

        if no is None:
            return

        if value < no.dado:
            self.remove(value, no.esquerda, no, True, False)
            return
        
        if value > no.dado:
            self.remove(value, no.direita, no, False, False)
            return

        if no.esquerda == no.direita:
            self.len -= 1
            if father is None:
                self.raiz.dado = None
            elif isLeft:
                father.esquerda = None
            else:
                father.direita = None
            return self.peso()
        
        if no.esquerda is None:
            self.len -= 1
            if father is None:
                self.raiz = self.raiz.direita
            elif isLeft:
                father.esquerda = no.direita
            else:
                father.direita = no.direita
            return self.peso()
        
        if no.direita is None:
            self.len -= 1
            if father is None:
                self.raiz = self.raiz.direita
            elif isLeft:
                father.esquerda = no.esquerda
            else:
                father.direita = no.esquerda
            return self.peso()
        
        min = self.min(no.direita)
        no.dado = min
        self.remove(no.dado, no.direita, no, False, False)
        

    def altura(self,no = None,h = 0, start = True):
        if start:
            no = self.raiz

        if no is None:
            return h -1
        
        x = self.altura(no.esquerda, h+1, False) 
        y = self.altura(no.direita, h+1, False)

        if x > y:
            return x
        return y

    def exibir_arvore(self):
        raiz = self.raiz     

        janela = tk.Tk()
        canvas = tk.Canvas(janela, width=1200, height=720)
        canvas.pack()

        def desenhar_no(no, x, y, dx, dy):
            raio = 20
            cor = "white"
            if no is not None:
                canvas.create_oval(x - raio, y - raio, x + raio, y + raio, fill=cor)
                canvas.create_text(x, y, text=str(no))
                if no.esquerda:
                    canvas.create_line(x, y + raio, x - dx, y + dy - raio)
                    desenhar_no(no.esquerda, x - dx, y + dy, dx/2, dy)
                if no.direita:
                    canvas.create_line(x, y + raio, x + dx, y + dy - raio)
                    desenhar_no(no.direita, x + dx, y + dy, dx/2, dy)

        desenhar_no(raiz, 600, 50, 200, 100)
        janela.mainloop()
        
    def __str__(self):
        return str(self.raiz)
    
    def __len__(self):
        return self.len