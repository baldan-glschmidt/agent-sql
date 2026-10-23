# R092QCL

## Descrição

Quadro Lotação p/ Posto de Trabalho - Calendário

---

## Resumo

- Campos: 4
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstPos | Number(003,0) | Não | Código da estrutura de postos de trabalho |
| CodPlv | Number(004,0) | Não | Código do Plano de Vagas |
| PerQcl | Number(001,0) | Não | Indica a periodicidade dos registros do calendário do quadro de vagas |
| DatQcl | Date | Não | Data-base para consulta do saldo do quadro de vagas |

---

## Chave Primária

- EstPos
- CodPlv
- PerQcl
- DatQcl

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R092QCL_001

**Tabela:** R017PLV

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| CodPlv | CodPlv |

