# R960PRT

## Descrição

Portas dos serviços

---

## Resumo

- Campos: 21
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PRVID | Number(004,0) | Não | Identificador do provedor de serviços |
| SRVID | Number(004,0) | Não | Identificador do serviço |
| PRTID | Number(004,0) | Não | ID seqüêncial da porta |
| PRMSEQ | Number(002,0) | Não | Sequencial de quebra dos parâmetros |
| PRTNAM | String(255) | Sim | Nome da porta |
| PRTDES | String(255) | Sim | Descrição da porta |
| PRTDTO | Number(005,0) | Sim | Time out padrão |
| PRTRUL | Number(001,0) | Sim | Porta é um serviço de regra |
| PRTAUT | Number(001,0) | Sim | Tipo de autenticação da porta |
| RESMOD | Number(001,0) | Sim | Modo de retorno dos parâmetros |
| PRMDEF | String(8001) | Sim | Definição dos parâmetros de entrada e saída |
| PRTURI | String(255) | Sim | Identificador universal da porta |
| PRTACT | String(255) | Sim | Soap Action |
| PRTENC | String(255) | Sim | Estilo de codificação da porta |
| PRTVST | Number(001,0) | Sim | Status da versão da porta |
| PRTSPT | String(001) | Sim | Enviar o tipo de dado dos parâmetros na chamada de web services terceiros |
| PRTATV | Number(001,0) | Sim | Porta está ativa |
| FLGLOG | Number(003,0) | Sim | Valores: -1: Não gravar; 0: Gravar e não remover; x: Grava e remove em x dias |
| PRTXNM | String(255) | Sim | Nome externo da porta |
| PRMDTM | Date | Sim | Data da última modificação dos parâmetros da porta de serviço |
| TIPSER | String(255) | Sim | Tipo do serviço |

---

## Chave Primária

- PRVID
- SRVID
- PRTID
- PRMSEQ

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
