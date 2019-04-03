'''
Created on 3 de abr de 2019

@author: ik
'''
import tornado.web
import tornado.ioloop
import os
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
                         self.get_argument('approximate_age'))

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
        img_dir = os.path.join('../imgs', name) + '.png'
        try:
            with open(img_dir, 'rb') as arq:
                content = arq.read()
                self.set_header('Content-type', 'image/png')
                self.set_header('Content-length', len(content)) 
                self.write(content)
        except IOError:
            self.write('Failed load image')

if __name__ == "__main__":
    
    BASE_DIR = os.getcwd()
    db_dir = os.path.join(BASE_DIR, 'desafio.db')
    print(db_dir)
    db = Db(db_dir)
    db.create_env()
    
    try:
        app = tornado.web.Application([
                (r"/", RequestHandlerRaiz),
                (r"/CadastraAnimal", RequestHandlerCadastraAnimal),
                (r"/CadastraCliente", RequestHandlerCadastraCliente),
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


