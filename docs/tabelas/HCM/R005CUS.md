# R005CUS

## Descrição

Custos do Acidente

---

## Resumo

- Campos: 7
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodAci | Number(005,0) | Não | Código do Acidente |
| CodSeq | Number(002,0) | Não | Código da Sequência |
| CodTDe | Number(002,0) | Sim | Código do Tipo de Despesa |
| ResCus | Number(001,0) | Sim | Responsável |
| ValCus | Number(011,2) | Sim | Valor do Custo |
| PagCus | Date | Sim | Data de Pagamento do Custo |
| ObsCus | String(2500) | Sim | Observação |

---

## Chave Primária

- CodAci
- CodSeq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R005CUS_000

**Tabela:** R005ACI

| Origem | Destino |
|--------|---------|
| CodAci | CodAci |

### IR_R005CUS_002

**Tabela:** R005DES

| Origem | Destino |
|--------|---------|
| CodTDe | CodTDe |

