# R512PAR

## Descrição

Consulta Web - Parâmetros

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPer | Number(004,0) | Não | Perfil de Consulta Web |
| IdeECW | Number(009,0) | Não | Identificador do elemento |
| SeqPar | Number(003,0) | Não | Sequência do parâmetro |
| NomPar | String(040) | Sim | Nome do parâmetro |
| TipPCW | Number(001,0) | Sim | Tipo do parâmetro |

---

## Chave Primária

- CodPer
- IdeECW
- SeqPar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R512PAR_001

**Tabela:** R512LAY

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |
| IdeECW | IdeECW |

