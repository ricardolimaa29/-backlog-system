import mysql.connector
from mysql.connector import errorcode
from tkinter import messagebox
from datetime import timedelta,datetime


def conectar():
    try:
        conn = mysql.connector.connect(
            user='',
            password='',
            host='',
            database=''
        )
        if conn.is_connected():
            return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Algo está errado com o seu nome de usuário ou senha")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("O banco de dados não existe")
        else:
            print(err)
    return None
# Acessar informações
def mostrar_info():
    conn = conectar()
    lista = []
    
    cur = conn.cursor()
    query = "SELECT * FROM formulario ORDER BY status DESC"
    cur.execute(query)
    informacao = cur.fetchall()

    for i in informacao:
        lista.append(i)
    return lista


def inserir_info(i):
    conn = conectar()  # Estabelecer a conexão aqui
    if conn:
        try:
            cur = conn.cursor()  # Obtenção do cursor
            query = "INSERT INTO formulario (nome, NF, data, status) VALUES (%s, %s, %s, %s)"  # Query ajustada para usar %s como placeholders
            cur.execute(query, i)  # Executar a query com os valores passados
            conn.commit()  # Comitar a transação
        except mysql.connector.Error as err:
            print(f"Erro ao inserir dados: {err}")
        finally:
            pass

def atualizar_form(i):
    conn = conectar()
    if conn:
        try:
            cur = conn.cursor()
            query = "UPDATE formulario SET nome=%s, NF=%s,data=%s, status=%s  WHERE id=%s"
            cur.execute(query, i)
            conn.commit()  # Comitar a transação
        except mysql.connector.Error:
            messagebox.showerror(f"Erro", "Erro ao atualizar dados: {Error}")
        finally:
            pass

# Deletar formulario
def deletar_form(i):
    conn = conectar()
    if conn:
        try:
            cur = conn.cursor()
            query = "DELETE FROM formulario WHERE id=%s"
            cur.execute(query, i)
            conn.commit()
        except mysql.connector.Error:
            messagebox.showerror("Erro", "Erro ao deletar dados: {Error}")
        finally:
            pass
# Funcao para buscar no banco de dados e apresentar ao usuario os avisos
def consulta_prazos():
    conn = conectar()
    if conn:
        try:
            cur = conn.cursor()
            query = "SELECT * FROM formulario WHERE status='PENDENTE'"
            cur.execute(query)
            linhas = cur.fetchall()
            for linha in linhas:
                nome = linha[1]
                nf = linha[2]
                data = linha[3]
                primeiro_prazo = data+timedelta(2)
                segundo_prazo = data+timedelta(3)
                hoje = datetime.now()
                if primeiro_prazo == hoje.date():
                    messagebox.showinfo("Aviso diario",f"Fornecedor: {nome}. \nData registrada em: {data}. \nNF:{nf}. \n\n\nEsta vencendo hoje dia {primeiro_prazo}, como 1 prazo de cobrança.")
                elif segundo_prazo == hoje.date():
                    messagebox.showwarning("Aviso diario",f"Fornecedor: {nome}. \nData registrada em: {data}. \nNF:{nf}. \n\n\nEsta vencendo hoje dia {segundo_prazo}, como 2 prazo de cobrança.")
                else:
                    pass
                    
        except mysql.connector.Error:
            print("Erro ao consultar banco dados: {Error}")
        finally:
            pass
