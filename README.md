<h2>Testes backend Python</h2>
<p>Usage:</p>

<p><strong>P&aacute;gina inicial</strong><br /> localhost:8888/</p>
<p><strong>Cadastro de Animal</strong><br /> localhost:8888/CadastraAnimal<br /> Exemplo:<br /><strong>$</strong> curl -X POST localhost:8888/CadastraAnimal --data "name=Teste&amp;approximate_age=2&amp;typeA=XG&amp;rescue_date='2018-08-05'&amp;adoption_date='2018-08-10'&amp;porte=S&amp;vaccinated=Y"<br /> <br /><strong>Cadastro de Cliente</strong><br /> localhost:8888/CadastroCliente<br /> Exemplo:<br /> <strong>$</strong> curl -X POST localhost:8888/CadastraCliente --data "name=ClienteTest&amp;last_name=SObrenomeTeste&amp;RG='987896541'&amp;proof_of_address='Y'&amp;email='asd@asd.com'&amp;phone='11985236547'"</p>
<p><strong>Exibi&ccedil;&atilde;o das imagens</strong><br /> localhost:8888/foto/{id}<br /> Exemplo:<br /> localhost:8888/foto/2</p>
