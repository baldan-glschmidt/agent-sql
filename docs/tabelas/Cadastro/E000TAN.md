# E000TAN

## Descrição

Tabelas - Integrações com autenticador externo - Registro  das movimentações dos títulos

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
| SeqReg | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumTit | String(015) | Não | Número do título a receber |
| CodTpt | String(003) | Não | Código do tipo de título a receber |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| SitExp | String(001) | Sim | Situação do processamento da pendência de integração |
| FilBai | Number(005,0) | Sim | Código da filial que realizou a baixa |
| NumPdv | Number(003,0) | Sim | Número do que efetuou a baixa |
| DatBai | Date | Sim | Data que foi realizada a baixa |
| ChvLot | String(024) | Sim | Chave do lote de baixa |
| DatExp | Date | Sim | Data da exportação |
| HorExp | Number(005,0) | Sim | Hora da exportacao do registro |
| FilCan | Number(005,0) | Sim | Código da filial que realizou o cancelamento da baixa |
| TipOco | Number(001,0) | Sim | Tipo da ocorrência armazenada |

---

## Chave Primária

- SeqReg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
