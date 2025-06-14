import sys
import platform
import itertools
import random

# Só importa tkinter se realmente for usar GUI

def le_senhas_existentes(arquivo):
    with open(arquivo, 'r') as f:
        return [linha.strip() for linha in f if linha.strip()]

def substituicoes_comuns(senha):
    mapa = str.maketrans({'a': '@', 'A': '@', 'o': '0', 'O': '0', 'e': '3', 'E': '3', 'i': '1', 'I': '1', 's': '$', 'S': '$'})
    return senha.translate(mapa)

def gerar_variacoes(senha, n_var, especiais):
    variacoes = set()
    variacoes.add(senha)
    variacoes.add(substituicoes_comuns(senha))
    especiais_lista = ['!', '@', '#', '$', '%', '&', '*']
    for _ in range(n_var):
        nova = senha
        # Adiciona caractere especial no início ou fim
        if especiais:
            nova = random.choice(especiais_lista) + nova
            variacoes.add(nova)
            nova = senha + random.choice(especiais_lista)
            variacoes.add(nova)
        # Troca letras por números/símbolos
        variacoes.add(substituicoes_comuns(nova))
    return variacoes

def cli_interface():
    print("Escolha a fonte das senhas base:")
    print("1. Arquivo")
    print("2. Entrada manual")
    opcao = input("Opção (1/2): ").strip()
    senhas = []
    if opcao == "1":
        arquivo = input("Digite o nome do arquivo com as senhas base: ").strip()
        try:
            senhas = le_senhas_existentes(arquivo)
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")
            return
    elif opcao == "2":
        print("Digite as senhas base (uma por linha). Digite 'fim' para terminar:")
        while True:
            senha = input().strip()
            if senha.lower() == 'fim':
                break
            if senha:
                senhas.append(senha)
    else:
        print("Opção inválida.")
        return
    if not senhas:
        print("Nenhuma senha fornecida.")
        return
    n_var = int(input("Quantas variações por senha deseja gerar? "))
    especiais = input("Deseja adicionar caracteres especiais? (s/n): ").strip().lower() == 's'
    todas_variacoes = set()
    for senha in senhas:
        todas_variacoes.update(gerar_variacoes(senha, n_var, especiais))
    out_file = input("Nome do arquivo para salvar o novo dicionário: ").strip()
    with open(out_file, 'w') as f:
        for v in todas_variacoes:
            f.write(v + '\n')
    print(f"Dicionário gerado e salvo em {out_file} com {len(todas_variacoes)} senhas.")

def gui_interface():
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.title("Gerador de Senhas")

    tk.Label(root, text="Nome do arquivo com senhas base:").grid(row=0, column=0)
    arquivo_entry = tk.Entry(root)
    arquivo_entry.grid(row=0, column=1)

    tk.Label(root, text="Quantidade de Variações por Senha:").grid(row=1, column=0)
    n_var_entry = tk.Entry(root)
    n_var_entry.grid(row=1, column=1)

    tk.Label(root, text="Deseja Adicionar Caracteres Especiais? (s/n):").grid(row=2, column=0)
    especiais_entry = tk.Entry(root)
    especiais_entry.grid(row=2, column=1)

    def on_generate():
        arquivo = arquivo_entry.get()
        n_var = int(n_var_entry.get())
        especiais = especiais_entry.get().strip().lower() == 's'
        try:
            senhas = le_senhas_existentes(arquivo)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao ler o arquivo: {e}")
            return
        todas_variacoes = set()
        for senha in senhas:
            todas_variacoes.update(gerar_variacoes(senha, n_var, especiais))
        out_file = input("Nome do arquivo para salvar o novo dicionário: ").strip()
        with open(out_file, 'w') as f:
            for v in todas_variacoes:
                f.write(v + '\n')
        messagebox.showinfo("Sucesso", f"Dicionário gerado e salvo em {out_file} com {len(todas_variacoes)} senhas.")

    tk.Button(root, text="Gerar Dicionário", command=on_generate).grid(row=3, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    choice = input("Escolha a interface (CLI/GUI): ").strip().lower()
    if choice == "cli":
        cli_interface()
    elif choice == "gui":
        # Detecta macOS antigo e força CLI
        if platform.system() == "Darwin":
            mac_ver = platform.mac_ver()[0]
            try:
                major = int(mac_ver.split(".")[0])
            except Exception:
                major = 0
            if major < 26:
                print("GUI não suportada neste macOS. Usando CLI.")
                cli_interface()
                sys.exit(0)
        try:
            gui_interface()
        except Exception as e:
            print(f"Erro ao iniciar a interface gráfica: {e}")
            print("Executando em modo CLI...")
            cli_interface()
    else:
        print("Opção inválida. Usando CLI por padrão.")
        cli_interface() 