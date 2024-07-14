import os

def create_directory(path):
    """ Cria um diretório se ele não existir. """
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Pasta '{path}' criada com sucesso!")
    else:
        print(f"Pasta '{path}' já existe.")

def create_file(path, content=""):
    """ Cria um arquivo se ele não existir, com conteúdo opcional. """
    if not os.path.isfile(path):
        with open(path, 'w') as file:
            file.write(content)
        print(f"Arquivo '{path}' criado com sucesso!")
    else:
        print(f"Arquivo '{path}' já existe.")

# Estrutura de diretórios e arquivos para criar
directories = [
    "config",
    "principal/model", "principal/view", "principal/template",
    "usuario/model", "usuario/view", "usuario/template",
    "produto/model", "produto/view", "produto/template",
    "estoque/model", "estoque/view", "estoque/template",
    "templates/main"
]

files = {
    "constructor.py": "",
    "app.py": "",
    "config/router.py": "",
    "usuario/model/user_model.py": "",
    "usuario/view/user_view.py": "",
    "usuario/template/user_template.html": "",
    "principal/model/main_model.py": "",
    "principal/view/main_view.py": "",
    "principal/template/main_template.html": "",
    "produto/model/product_model.py": "",
    "produto/view/product_view.py": "",
    "produto/template/product_template.html": "",
    "estoque/model/stock_model.py": "",
    "estoque/view/stock_view.py": "",
    "estoque/template/stock_template.html": "",
    "templates/main/base_template.html": "",
    "templates/index.html": ""
}

# Caminho base onde os diretórios e arquivos devem ser criados
base_path = '/app'  # Ajuste esse caminho conforme o caminho absoluto do diretório no seu container

# Criar diretórios
for directory in directories:
    create_directory(os.path.join(base_path, directory))

# Criar arquivos
for file_path, content in files.items():
    create_file(os.path.join(base_path, file_path), content)

print("Estrutura de diretórios e arquivos criada com sucesso!")
