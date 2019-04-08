'''
Created on 3 de abr de 2019

@author: ik
'''
import tornado.web
import tornado.ioloop
import os
import ast
from src.db import Db

db = Db('clientes.db')

class RequestHandlerRaiz(tornado.web.RequestHandler):
    def get(self): self.render("index.html")

class RequestHandlerCadastraAnimal(tornado.web.RequestHandler):
    def get(self):
        self.write("[GET] Cadastro Animal\n")
    def post(self):
        self.write(self.request.body)
        db.insert_animais(self.get_argument('name'),
                          self.get_argument('typeA'),
                          self.get_argument('rescue_date'),
                          self.get_argument('adoption_date'),
                          self.get_argument('porte'),
                          self.get_argument('vaccinated'),
                          self.get_argument('approximate_age'),
                          self.get_argument('img_dir'))

class RequestHandlerCadastraCliente(tornado.web.RequestHandler):
    def get(self):
        self.write("[GET] Cadastro Cliente\n")
    def post(self):
        db.insert_cliente(self.get_argument('name'),
                          self.get_argument('last_name'),
                          self.get_argument('RG'),
                          self.get_argument('proof_of_address'),
                          self.get_argument('email'),
                          self.get_argument('phone'))

class RequestHandlerFoto(tornado.web.RequestHandler):
    def get(self, name):
        try:
            animal_info= db.select_from_animais_by_id(name)
            animal_path = ast.literal_eval(db.select_img_dir_from_animais_by_id(name))[0][0]
            animal_path += '.png'
            self.write(animal_info + '\n')
            with open(animal_path, 'rb') as arq:
                content = arq.read()
                self.set_header('Content-type', 'image/png')
                self.set_header('Content-length', len(content) + len(animal_info) + 1) 
                self.write(content)
                """
                Implementação com os elementos aqui
                    Conteúdo do banco = animal_info
                    Foto captada do banco = content
                """
        except IOError as ioe:
            self.write('Failed load image' + '\nIO Error: ' + format(ioe))

class RequestHandlerListaClientes(tornado.web.RequestHandler):
    def get(self):
        clients_list = ast.literal_eval(db.select_from_clientes())
        for i in clients_list:
            """
            Implementação com os elementos aqui
            """
            self.write(str(i) + '\n')

class RequestHandlerListaAnimais(tornado.web.RequestHandler):
    def get(self):
        animals_list = ast.literal_eval(db.select_from_animais())
        for i in animals_list:
            """
            Implementação com os elementos aqui
            """
            self.write(str(i) + '\n')

if __name__ == "__main__":
    
    BASE_DIR = os.getcwd()
    db_dir = os.path.join(BASE_DIR, 'desafio.db')
    print('Using databse file:', db_dir)
    db = Db(db_dir)
    db.create_env()
    
    try:
        app = tornado.web.Application([
                (r"/", RequestHandlerRaiz),
                (r"/CadastraAnimal",  RequestHandlerCadastraAnimal),
                (r"/CadastraCliente", RequestHandlerCadastraCliente),
                (r"/ListaClientes", RequestHandlerListaClientes),
                (r"/ListaAnimais", RequestHandlerListaAnimais),
                (r"/foto/([0-9]+)", RequestHandlerFoto)
            ])
        app.listen(8888)
        print('Listening on localhost:8888')
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print("Eitcha", format(e))
    finally:
        db.close_connection_db()
        print('\ndb closed\n')
