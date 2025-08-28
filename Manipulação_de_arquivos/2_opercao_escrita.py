arquivo = open("bootcamp_Santander\Manipulação_de_arquivos/teste.txt","w")

arquivo.write("escrevendo dados em um novo arquivo.")
arquivo.writelines(["Escrevendo","um","novo","texto"])
arquivo.close()