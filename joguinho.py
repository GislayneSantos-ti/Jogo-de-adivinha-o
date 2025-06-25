import customtkinter as ctk
import random

# Configuração inicial
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Janela principal
app = ctk.CTk()
app.title("Jogo da Adivinhação")
app.geometry("400x300")

# Variáveis do jogo
numero_secreto = random.randint(1, 10)
tentativas = 3

# Função para verificar o palpite
def verificar_palpite():
    global tentativas
    try:
        palpite = int(campo_palpite.get())
        if palpite == numero_secreto:
            resultado_label.configure(text="🎉 Parabéns! Você acertou!", text_color="green")
            botao_verificar.configure(state="disabled")
        else:
            tentativas -= 1
            if tentativas > 0:
                resultado_label.configure(
                    text=f"❌ Errado! Tentativas restantes: {tentativas}", text_color="orange"
                )
            else:
                resultado_label.configure(
                    text=f"💀 Fim de jogo! Número era {numero_secreto}", text_color="red"
                )
                botao_verificar.configure(state="disabled")
    except ValueError:
        resultado_label.configure(text="⚠️ Digite um número válido!", text_color="yellow")

# Título
titulo = ctk.CTkLabel(app, text="Adivinhe o número de 1 a 10", font=("Arial", 18))
titulo.pack(pady=20)

# Campo para digitar o palpite
campo_palpite = ctk.CTkEntry(app, placeholder_text="Seu palpite aqui")
campo_palpite.pack(pady=10)

# Botão para verificar
botao_verificar = ctk.CTkButton(app, text="Verificar", command=verificar_palpite)
botao_verificar.pack(pady=10)

# Resultado
resultado_label = ctk.CTkLabel(app, text="", font=("Arial", 14))
resultado_label.pack(pady=20)

# Iniciar o app
app.mainloop()
