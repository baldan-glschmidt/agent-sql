# R102TBR

## Descrição

Trabalhos do SESMT

---

## Resumo

- Campos: 9
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodTbr | Number(006,0) | Não | Código do Trabalho |
| DatTbr | Date | Sim | Data do Trabalho |
| HorTbr | Number(005,0) | Sim | Hora do Trabalho |
| TipTbr | Number(003,0) | Sim | Código do Tipo de trabalho |
| DesTbr | String(8000) | Sim | Descrição do Trabalho |
| OriTbr | Number(002,0) | Sim | Código da origem |
| CodFil | Number(006,0) | Sim | Código da filial de realização do trabalho |
| CodSmt | Number(004,0) | Sim | Código do SESMT |

---

## Chave Primária

- NumEmp
- CodTbr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R102TBR_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R102TBR_004

**Tabela:** R102TTB

| Origem | Destino |
|--------|---------|
| TipTbr | TipTbr |

