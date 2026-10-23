# R058TAA

## Descrição

Terminais de Autoatendimento

---

## Resumo

- Campos: 16
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodDsp | Number(009,0) | Não | Código do Dispositivo |
| DesDsp | String(050) | Sim | Descrição do Dispositivo |
| LeiCra | Number(001,0) | Sim | Tipo de Leitora |
| CodCen | Number(002,0) | Sim | Central de Gerenciamento do Acesso |
| EntVis | String(001) | Sim | Permite a entrada de visitantes por meio do terminal de autoatendimento |
| ProFun | String(001) | Sim | Conceder crachás provisórios para empregados pelo terminal de autoatendimento |
| ProTer | String(001) | Sim | Concede crachás provisórios para terceiros pelo terminal de autoatendimento |
| ProPar | String(001) | Sim | Conceder crachás provisórios para parceiros pelo terminal de autoatendimento |
| IniVis | Number(012,0) | Sim | Faixa Inicial de Crachá de Visitante |
| FimVis | Number(012,0) | Sim | Faixa Final de Crachá de Visitante |
| IniCol | Number(012,0) | Sim | Faixa Inicial de Crachá Provisório de Colaborador |
| FimCol | Number(012,0) | Sim | Faixa Final de Crachá Provisório de Colaborador |
| CodMsc | Number(002,0) | Sim | Código Mapa Smart Card |
| PorCom | String(010) | Sim | Porta de Comunicação |
| Usa2Di | String(001) | Sim | Utiliza 2 dispensers |
| PorVis | String(010) | Sim | Porta COM Visitante |

---

## Chave Primária

- CodDsp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
