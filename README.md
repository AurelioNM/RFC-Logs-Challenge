Uma rfc precisa ter:
- Objetivo, pra que serve, oq vc espera conseguir...
- E um guia do como fazer
- Razões que levaram a essas decisões

- tenham clato q a RCF fala muito sobre oq deve ser logado (level, tipo de msg, código de erro, tamanho de cada campo, source, tracer, oq é obrigatório, optional), sobre boas práticas (como lidar com isso, qdo usar cada level, qdo e como logar stack, sources, tracers, facilities) como deve ser logado (json, csv, tsv, xml, text) e onde (stdout, file, tcp, udp, http)
- no passado, falamos de forma superficial de como uma aplicação deve gerar seus logs, como esses logs devem ser trabalhados e armazenados, mas era um momento em que todos aqui ainda estavam muito imaturos nesse tipo de coisa, agora q esse tipo de situação se tornou cotidiana, é muito importante abordarmos esse assunto com maior profundidade, então eu pedi para que tds aqui pensem sobre isso e escrevam uma RFC (documentação de referência técnica) sobre o assunto, assim já pegam o jeito de como esse tipo de documentação funciona e abordamos com propriedade o assunto, falando de boas práticas, arquiteturas envolvidas, de vida real e como isso tudo se conversa.... é um assunto bem vasto e rico, onde temos muito a estudar e aprender... já q não existe uma só maneira de fazer mas existem MUITAS práticas ruins aí no meio.... resumindo é isso, a ideia é apresentar essa RFC essa semana, falar sobre isso, na semana q vem chegaremos a um modelo onde todos estejam fluentes e aí vamos colocar a mão na massa e fazer uma arch q coloque isso td em prática, para vermos nossa RFC funcionando... ficou claro?
- eu prefiro q vcs façam essa com calma, pensem em caminhos diferentes, entendam pq vão por um ou por outro
- não tem resposta muito certa, não tem receita de bolo, mas tem muitas respostas erradas e armadilhas, o importante é o caminho q vcs percorreram para entender...
- isso toca em arch, dev, sec, infra, cloud e etc....

- RFC 3164 - The BSD syslog protocol
- RFC 5424 - The Syslog Protocol
- RFC 5425 - Transport Layer Security (TLS) Transport Mapping for Syslog
- RFC 5426 - Transmission of Syslog Messages over UDP

- https://datatracker.ietf.org/doc/html/rfc5424
- https://en.wikipedia.org/wiki/Syslog
as- https://en.wikipedia.org/wiki/Syslog-ng
- https://www.dataset.com/blog/the-10-commandments-of-logging/


FACILITY

    - Níveis de ??segurança?? bem definidos, com exatamento o que deve ser logado
    - Tamanho das mensagens
    - Definir códigos/keywords para os logs estarem mais sucintos

| Facility Code | Keyword | Description | 
| ------------- | --------| ----------- |
| 0             | mem    | Consumo de memória | 
| 0             | cpu    | Consumo de cpu | 
| 0             | rout    | Routes messages | 
| 0             | hook    | Webhook messages | 
| 0             | fin     | Financial transactions messages | 
| 0             | usr     | User registration messages |



The Mororó Protocol


Objetivo:
    - Monitorar determinado sistema
        .Saber quais ações estão sendo executadas
        .Quais erros estão acontecendo
        .Como está a saúde do sistema
        .Como está a saúde/desempenho da máquina
        
        .É comum usarmos os próprios logs do Servidor para Segurança / Performance
        .Logs do linux
        .O cloud já pega informações de performance / rotas / ports / segurança. Eu devo me preocupar com esses caras então?
        .Backup e compressão

    - Precisa ser aplicável tanto no caso de o sistema rodar em um Monolito, quanto no cenário de termos uma arch de Microserviços

O log precisa conter:
    - Infra
        .De onde vem (qual server / qual cluster / qual worker)
    - Sistema
        .Origem, classe/função ou 
        .Qual função está sendo executado

Error/Critical/Emergency no cenário ideal:
    - Precisa acionar o time de alguma forma (slack)
    - É gerado uma task de HotFix

Cloud:
    - Politica de backup de logs
    - ??Onde eles vão estar localizados??

Infra:
    - Como vai ser a saída dos logs. TCP / UDP / STDOUT
    - Quantidade e especificação dos Atores. Quem coleta / trata / gerencia / quem faz os dashboards

    











