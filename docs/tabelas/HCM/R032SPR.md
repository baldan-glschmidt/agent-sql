# R032SPR

## Descrição

Serviços Contidos na Nota Fiscal - Serviço Prestado

---

## Resumo

- Campos: 9
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFIl | Number(006,0) | Não | Código da Filial |
| CodRat | Number(009,0) | Não | Código do Rateio |
| CmpRcb | Date | Não | Competência Serviço Prestado |
| SeqRcb | Number(003,0) | Não | Sequência Serviço Prestado |
| NumIte | Number(003,0) | Não | Número do Item |
| TipSer | Number(002,0) | Sim | Tipo Serviço Prestado |
| ValBru | Number(014,2) | Sim | Valor Bruto |
| BasRet | Number(014,2) | Sim | Base Retenção |

---

## Chave Primária

- NumEmp
- CodFIl
- CodRat
- CmpRcb
- SeqRcb
- NumIte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
