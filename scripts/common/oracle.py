import oracledb
import os

class OracleConnection:
    """Encapsulamento para conexões Oracle seguindo o padrão Factory"""
    
    def __init__(self):
        self.user = os.getenv("ORACLE_USER")
        self.password = os.getenv("ORACLE_PASS")
        self.dsn = os.getenv("ORACLE_DSN")
        self.connection = None

    def connect(self):
        try:
            self.connection = oracledb.connect(
                user=self.user,
                password=self.password,
                dsn=self.dsn
            )
            return self.connection
        except oracledb.Error as e:
            print(f"Erro Crítico de Conexão Oracle: {e}")
            raise

    def execute_query(self, sql, params={}):
        with self.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql, params)
                return cursor.fetchall()