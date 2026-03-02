 Z@P – Real-Time Messaging Application

Aplicação de mensagens em tempo real inspirada no WhatsApp, desenvolvida com React no front-end e Flask no back-end, utilizando WebSocket para comunicação bidirecional entre cliente e servidor.

📌 Descrição

O Z@P é uma aplicação full-stack focada em comunicação instantânea entre múltiplos usuários conectados simultaneamente.

O projeto demonstra:

Integração entre front-end e back-end

Comunicação persistente via WebSocket

Gerenciamento de conexões ativas

Atualização dinâmica da interface

As mensagens são transmitidas em tempo real, sem necessidade de recarregar a página, garantindo baixa latência e experiência fluida.

🚀 Tecnologias Utilizadas
🔹 Front-end

React

JavaScript 

CSS

🔹 Back-end

Flask

Python

🔹 Comunicação

WebSocket

Arquitetura

A aplicação segue o modelo cliente-servidor:

O cliente React estabelece conexão WebSocket com o servidor.

O servidor Flask mantém as conexões ativas.

Ao receber uma mensagem, o servidor a transmite para os demais clientes conectados.

A interface é atualizada automaticamente.
