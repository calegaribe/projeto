class login:

    def _init_(self, usuario, senha):
       self.nome=usuario
       self.senha=senha

    def verificar_login(self, usuario, senha):
        if  usuario==self.usuario and senha==self.senha:
            return True
        else:
            return False 





    