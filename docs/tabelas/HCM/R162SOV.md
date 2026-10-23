# R162SOV

## Descrição

BS - Solicitação Avulsa de Vales - Valor das Cédulas

---

## Resumo

- Campos: 8
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Número do Colaborador |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodVal | Number(004,0) | Não | Código do Tipo do Vale |
| DatSoc | Date | Não | Data Solicitação do Vale |
| VlrCed | Number(011,2) | Não | Valor da Cédula |
| QtdCed | Number(003,0) | Sim | Quantidade de Cédulas |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- TabEve
- CodVal
- DatSoc
- VlrCed

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R162SOV_005

**Tabela:** R162SOC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| TabEve | TabEve |
| CodVal | CodVal |
| DatSoc | DatSoc |

