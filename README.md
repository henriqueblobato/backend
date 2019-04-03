# backend

Usage:

Página inicial
  localhost:8888/

Cadastro de Animal
    localhost:8888/CadastraAnimal
    Exemplo:
      curl -X POST localhost:8888/CadastraAnimal --data "name=Teste&approximate_age=2&typeA=XG&rescue_date='2018-08-05'&adoption_date='2018-08-10'&porte=S&vaccinated=Y"
        
Cadastro de Cliente
  localhost:8888/CadastroCliente
  Exemplo:
    curl -X POST localhost:8888/CadastraCliente --data "name=ClienteTest&last_name=SObrenomeTeste&RG='987896541'&proof_of_address='Y'&email='asd@asd.com'&phone='11985236547'"

Exibiço das imagens
  localhost:8888/foto/{id}
  Exemplo:
    localhost:8888/foto/2
