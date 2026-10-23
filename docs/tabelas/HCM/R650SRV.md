# R650SRV

## Descrição

Servidores CFTV

---

## Resumo

- Campos: 13
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SrvCFT | Number(002,0) | Não | Servidor de Câmeras CFTV |
| EIPSrv | String(015) | Sim | Número IP do Servidor de Câmeras CFTV |
| NomSrv | String(024) | Sim | Nome do Servidor de Câmeras CFTV |
| PorCom | Number(005,0) | Sim | Porta Comunicação |
| UsuCFT | String(019) | Sim | Nome do Usuário do Sistema de CFTV Integrador |
| SenCFT | String(019) | Sim | Senha do Usuário do Sistema CFTV |
| FabSrv | Number(002,0) | Sim | Fabricante do servidor CFTV |
| IntFab | String(001) | Sim | Integra com o Fabricante |
| TimSvr | Number(005,0) | Sim | Time out de comunicação com o servidor de CFTV (milissegundos) |
| PorSec | Number(005,0) | Sim | Porta Secundária |
| ResCFT | String(015) | Sim | Resolução configurada para o servidor |
| QuaCFT | String(010) | Sim | Qualidade configurada para o servidor |
| LAYPAD | Number(003,0) | Sim | Layout do servidor CFTV |

---

## Chave Primária

- SrvCFT

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
