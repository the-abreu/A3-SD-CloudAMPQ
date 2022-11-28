# (A3) Sistemas Distribuídos e Mobile: Mensageria com RabbitMQ

## Apresentação
Esse projeto foi realizado pelos alunos da turma de Sistemas Distribuídos e Mobile do turno noturno da UNIFACS (Nomes e RA's dos alunos no arquivo PDF).

## Descrição
Este projeto possui o propósito de realizar um sistema em que tenhamos uma matriz (Publisher), que envia uma fila de mensagens para as filiais (Subscriber), tendo entre os dois um intermediador que neste caso é o RabbitMQ (Como sugerido no enunciado deste trabalho).

## Pré-Requisitos
* Possuir instalado em sua máquina a linguagem Python;
* Possuir instalado em sua máquina uma IDE, como o VsCode ou PyCharm (Onde você pode abrir os arquivos e ler o código);
* Possuir instalado em sua máquina o Erlang (é a linguagem de programação utilizada pelo RabbitMQ);
* Possuir instalado em sua máquina o RabbitMQ (Você pode começar a instalação pelo RabbitMQ, mas ele vai lhe informar a necessidade do Erlang e o redirecionar para baixar o instalador da linguagem);
* Clonar este repositório em sua máquina:

HTTPS:
```
git clone https://github.com/the-abreu/A3-SD-CloudAMPQ.git
```

## Como manusear o sistema
* Você encontrará dois arquivos, o Publisher.py e o Subscriber.py;
* O arquivo Publisher.py se refere a matriz, é a partir dele que enviaremos as mensagens.
* O arquivo Subscriber.py se refere a filial, é a partir dele que receberemos as mensagens enviadas pela matriz, mas que passam pelas filas do RabbitMQ.
* OBS:Para que sua experiência manuseando o sistema ocorra como o esperado, você deve executar os dois arquivos!

## Introdução as funcionalidades do sistema
Ao executar corretamente o arquivo da Matriz (Publisher.py) e da filial (Subscriber.py), você irá se deparar com as particularidades de cada um deles. Segue abaixo o que cada um pode realizar no sistema:
<details open>
  <summary>
    <b>Matriz</b>
  </summary>

- Funcionalidade: A partir do código de N° 1 você poderá enviar um lote de mensagens as filiais

- Obs: Dado ao contexto do enunciado do projeto, estamos lidando com uma rede de lavanderias, por isso as mensagens deste lote se referem a instruções da Matriz as filiais baseadas neste cenário.

- Funcionalidade: A partir do código de N° 2 você poderá enviar uma mensagem específica as filiais.

- Obs II: Esta segunda funcionalidade é uma forma didática de experenciar o envio e recebimento de mensagens.
</details>

<details open>
  <summary>
    <b>Filial</b>
  </summary>

- Funcionalidade: Este Script que se refere a filial pode apenas "escutar" as mensagens do canal, logo, é a partir dele que você poderá fazer a leitura dos dados recebidos.
</details>