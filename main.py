import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw


class DesenhoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicativo de Desenho")

        # Configurar a área de desenho
        self.canvas = tk.Canvas(self, bg='white', width=400, height=400)
        self.canvas.pack(expand=True, fill='both')

        # Adicionar eventos do mouse
        self.canvas.bind("<Button-1>", self.iniciar_desenho)
        self.canvas.bind("<B1-Motion>", self.desenhar)

        # Configurar uma imagem para desenhar e um objeto ImageDraw para manipulação
        self.imagem = Image.new("RGB", (400, 400), 'white')
        self.desenho = ImageDraw.Draw(self.imagem)

        # Menu para salvar a imagem
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)
        arquivo_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Arquivo", menu=arquivo_menu)
        arquivo_menu.add_command(label="Salvar", command=self.salvar_imagem)

        self.ultima_posicao = None

    def iniciar_desenho(self, evento):
        self.ultima_posicao = (evento.x, evento.y)

    def desenhar(self, evento):
        if self.ultima_posicao:
            # Desenhe no canvas
            self.canvas.create_line(
                self.ultima_posicao[0],
                self.ultima_posicao[1],
                evento.x,
                evento.y,
                fill='black',
                width=3
            )
            # Desenhe na imagem
            self.desenho.line(
                [self.ultima_posicao, (evento.x, evento.y)],
                fill='black',
                width=3
            )
            self.ultima_posicao = (evento.x, evento.y)

    def salvar_imagem(self):
        # Solicitar ao usuário um local para salvar a imagem
        caminho_arquivo = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All Files", "*.*")]
        )
        if caminho_arquivo:
            self.imagem.save(caminho_arquivo)
            print(f"Imagem salva em: {caminho_arquivo}")


# Executar o aplicativo
app = DesenhoApp()
app.mainloop()