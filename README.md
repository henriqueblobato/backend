# Python backend test

Testes para backend em Python utilizando servidor web tornado e banco de dados sqlite3

### Installation

Instalação das dependências

```sh
$ pip3 install tornado torndb sqlite3
$ git clone https://github.com/henriqueblobato/backend.git
$ cd backend
$ python3 index.py
```
### Usage

##### Página principal

```sh
localhost:8000/
```

##### Cadastro de Animais Abandonados
```sh
Exemplo:
$ curl -X POST localhost:8888/CadastraAnimal --data "name=Teste&approximate_age=2&typeA=XG&rescue_date='2018-08-05'&adoption_date='2018-08-10'&porte=S&vaccinated=Y&img_dir='../img/1.png'"
```

##### Cadastro de Clientes
```sh
Exemplo:
$ curl -X POST localhost:8888/CadastraCliente --data "name=ClienteTest&last_name=SObrenomeTeste&RG='987896541'&proof_of_address='Y'&email='asd@asd.com'&phone='11985236547'"
```
##### Exibição de imagens e informações dos animais

```sh
Exemplo:
localhost:8888/foto/{id}
localhost:8888/foto/2
```

