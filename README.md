# -backlog-system
Sistema criado para tratar as pendencias do setor de Compras.

Este sistema foi criado para fins de notificar ao usuario suas 'PENDENCIAS' do dia.

<h2>Esta é a tela de inicialização do sistema:</h2>

![Captura de tela 2024-05-23 163247](https://github.com/ricardolimaa29/-backlog-system/assets/147922620/71249c76-c1d5-4818-90d4-f08d64076e42)


<h3>Bibliotecas utilizadas foram anexadas ao requeriments.txt</h3>
<h4>Vocês poderam utilizar tanto o requeriments ou realizar a instalação manualmente com o Pip install + nome_da_biblioteca </h4>

<h2>Utilidades</h2>
<br>
<h3>
  - O sistema tem a funcionalidade de um CRUD comum, LER,CRIAR,EDITAR E EXCLUIR pendencias<br>
  - Alertas são gerados toda vez que o sistema inicializa, notificando os itens em 'PENDENTE'<br>
  - Os Alertas são gerados quando a 'Data registrada' + dias forem iguais ao dia atual do usuario<br>
    <h4>+ 1° Aviso: 'data registrada' + 2 dias = 'dia_atual' ( datetime.now() )</h4><br>
    <h4>+ 2° Aviso: 'data registrada' + 3 dias = 'dia_atual' ( datetime.now() )</h4><br>
  - Registros: podendo deixar todos os FORNECEDORES 'CONFIRMADOS', nao irá notificar o usuario<br>
</h3>

<h1>Telas do sistema:</h1>

  <h2>Editando</h2>
![editando](https://github.com/ricardolimaa29/-backlog-system/assets/147922620/97467b70-3a4d-4482-9ab8-a02132238ade)

  <h2>Salvando</h2>
![salvando](https://github.com/ricardolimaa29/-backlog-system/assets/147922620/2445dd94-77e0-4610-b2d0-91db81541d3e)

  <h2>Excluindo</h2>

![deletando](https://github.com/ricardolimaa29/-backlog-system/assets/147922620/36e981e1-dbcf-405c-aecf-a5b3f0c22352)

