- RFC 3164 - The BSD syslog protocol
- RFC 5424 - The Syslog Protocol
- RFC 5425 - Transport Layer Security (TLS) Transport Mapping for Syslog
- RFC 5426 - Transmission of Syslog Messages over UDP
-
- https://datatracker.ietf.org/doc/html/rfc5424
- https://en.wikipedia.org/wiki/Syslog
- https://en.wikipedia.org/wiki/Syslog-ng
- https://www.dataset.com/blog/the-10-commandments-of-logging/

# The Doença Protocol

## Objetivo:
    - Monitorar determinado sistema
        .Saber quais ações estão sendo executadas
        .Quais erros estão acontecendo
        .Como está a saúde do sistema
        .Como está a saúde/desempenho da máquina
    - Precisa ser aplicável tanto no caso de o sistema rodar em um Monolito, quanto no cenário de termos uma 
    arch de Microserviços

## LEVELS

## Não faça isso:
    Não botar info sensível (nº de cartão, senhas)
    Não logar Debug em Prod
    Não colocar Estruturas de Dados complexas, pra não atrapalhar o parser

### - Info:
    Evento que possui relevância de negócio    
    ex:
        "Transação executada"
        "Compra efetuada"
        "Ações do usuário"
### - Debug:
    .Tracing -> Classe/função executado
    .Tempo de execução
### - Warning:
    .Algo que pode ou não ser um problema
    .Security (varias req não autenticadas)
    .Possível timeout
    .Refazer alguma operação. Tentar de novo algo que deu errado
    .Valores não previstos causando estranheza no sistema
### - Error:
    .Status 500
    .Algo que atrapalhou a operação do negócio
    .Deu erro, mas o sistema não caiu
### - Critical:
    .Subir o stack-trace
    .Aplicação não iria se recuperar sozinha
    .Derruba o sistema

## Log Structure
Data Time Facility Level Message

2013-01-12 17:49:37,656 app[email-wrkr.1] INFO User plays {'user':1334563, 'card':'4 of spade', 'game':23425656}

## FACILITY

| Facility Code | Keyword | Description                     | 
|---------------|---------|---------------------------------|
| 0             | rout    | Routes messages                 | 
| 0             | hook    | Webhook messages                |
| 0             | fin     | Financial transactions messages |
| 0             | usr     | User registration messages      |
| 0             | usr     | Mail messages                   |

