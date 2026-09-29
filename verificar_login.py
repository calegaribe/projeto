class login:

    def _init_(self, usuario, senha):
       self.nome=usuario
       self.senha=senha

    def verificar_login(self, usuario, senha):
            return usuario == self.usuario and senha == self.senha

contas= []

def criar_conta():
     usuario=input("Informe o nome do novo usuário:")
     senha=input("Digite sua senha de acesso a conta: ")

     nova_conta=login(usuario, senha)

     contas.append(nova_conta)

     print("Parabéns! Sua conta foi criada com sucesso!")

def  fazer_login():
     usuario=input("Usuário: ")
     senha=input("Senha: ")

     for conta in contas:
          if conta.verificar_login(usuario, senha):
               print("login realizado com sucesso!!")
          return

     print("Usuário ou senha incorreto/os.")



    