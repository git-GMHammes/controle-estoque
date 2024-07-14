import os

def list_files_and_contents(directories):
    ignore_files_in_app = {
        "analise.py",
        "setup_project.py",
        "test_db_connection.py",
        "testeSQLAlchemy.py"
    }

    for directory in directories:
        print(f"\nListando arquivos em: {directory}\n")
        if os.path.exists(directory):
            for root, dirs, files in os.walk(directory):
                # Ignore __pycache__ directories
                dirs[:] = [d for d in dirs if d != '__pycache__']
                level = root.replace(directory, '').count(os.sep)
                indent = ' ' * 4 * (level)
                subindent = ' ' * 4 * (level + 1)
                print(f"{root}:")
                for d in dirs:
                    print(f"{subindent}{d}")
                for f in files:
                    if not f.endswith('.pyc'):
                        # Ignore specific files in /app
                        if directory == "/app" and f in ignore_files_in_app:
                            continue
                        print(f"{subindent}{f}")
                        file_path = os.path.join(root, f)
                        try:
                            with open(file_path, 'r') as file:
                                print(file.read())
                        except Exception as e:
                            print(f"Erro ao ler o arquivo {file_path}: {e}")
        else:
            print(f"O caminho {directory} não existe. Verifique o caminho especificado.")

if __name__ == "__main__":
    directories_to_list = ["/app"]  # Substitua por qualquer lista de diretórios que deseja listar
    list_files_and_contents(directories_to_list)
