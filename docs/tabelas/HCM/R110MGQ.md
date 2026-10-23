# R110MGQ

## Descrição

Histórico de Grupos de Questionário - Itens

---

## Resumo

- Campos: 7
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código Empresa |
| CodFic | Number(009,0) | Não | Código da Ficha Médica |
| CodGrq | Number(003,0) | Não | Código do Grupo Questionário |
| DatGrq | Date | Não | Data Respostas |
| CodItq | Number(003,0) | Não | Código do Item Questionário |
| CodRsp | Number(003,0) | Não | Código da Resposta |
| AnoRsp | String(4000) | Sim | Anotações da Resposta |

---

## Chave Primária

- NumEmp
- CodFic
- CodGrq
- DatGrq
- CodItq
- CodRsp

---

## Índices

### R110MGQIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- CodFic

---

## Relacionamentos

### IR_R110MGQ_003

**Tabela:** R110MHQ

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFic | CodFic |
| CodGrq | CodGrq |
| DatGrq | DatGrq |

