class Usuario : 
    def __init__(self,nombre,apellido,dni,email)
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.email = email
        
    

    def comprar(self)
        print("que articulo desea comprar ?")

    def vender(self)
        print("que articulo desea vender ?")     

class Cliente(Usuario):
      def __init__(self,nombre,apellido)
          
      def comprar(self)
          print ("que articulo desea comprar ?")

      def vender(self)
          print ('que articulo desea vender ?')     

cliente1 = Cliente("manuel","lara")
Usuario1 = Usuario("manuel","lara",30340072,"laraherrastimanuel@gmail.com" )
