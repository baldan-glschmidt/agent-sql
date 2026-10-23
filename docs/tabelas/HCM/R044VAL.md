# R044VAL

## Descrição

Vales / Compras

---

## Resumo

- Campos: 17
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| DatPag | Date | Não | Data de Pagamento do Vale |
| SeqVal | Number(002,0) | Não | Sequência do Vale no Dia |
| TabEve | Number(003,0) | Sim | Código da Tabela de Eventos |
| TipVal | Number(004,0) | Sim | Tipo do Vale (Tab. Vales) |
| CmpIni | Date | Sim | Competência Início Desconto |
| TdcVal | String(001) | Sim | Tipo de Desconto do Vale/Compra |
| CalIrf | String(001) | Sim | Calculou imposto de renda |
| QtdPcl | Number(003,0) | Sim | Quantidade de parcelas |
| ForDig | String(001) | Sim | Forma Digitação (L,B,S) |
| OriVal | String(001) | Sim | Origem do Vale (I,D) |
| ValBru | Number(011,2) | Sim | Valor bruto do adiantamento |
| ValIrf | Number(011,2) | Sim | Valor IR do adiantamento |
| ValLiq | Number(011,2) | Sim | Valor líquido do adiantamento |
| NroDoc | String(015) | Sim | Número documento do vale |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatPag
- SeqVal

---

## Índices

### R044VALIndice2

**Tipo:** Não unico

Campos:
- TabEve
- TipVal

---

## Relacionamentos

### IR_R044VAL_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R044VAL_005

**Tabela:** R008EVM

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |

### IR_R044VAL_006

**Tabela:** R044TVL

| Origem | Destino |
|--------|---------|
| TabEve | TabEve |
| TipVal | CodVal |

