import oracledb
import os
import sys

def validate_oracle():
    print("--- Iniciando Validação Oracle ---")
    print(f"Python version: {sys.version}")
    
    try:
        oracledb.init_oracle_client()
        print("Modo 'Thick' inicializado com sucesso usando Instant Client.")
    except Exception as e:
        print(f"Falha ao carregar Instant Client: {e}")
        return

    user = os.getenv("DB_USER", "admin")
    password = os.getenv("DB_PASS")
    dsn = "MONACO_DEV"

    print(f"Tentando conexão com alias: {dsn}...")
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as connection:
            print("Conexão estabelecida com sucesso!")
            with connection.cursor() as cursor:
                cursor.execute("SELECT 'Conexão OK' FROM DUAL")
                res = cursor.fetchone()
                print(f"Resultado do Banco: {res[0]}")
    except oracledb.Error as e:
        print(f"Erro de conexão Oracle: {e}")

if __name__ == "__main__":
    validate_oracle()