# R046AFM

## Descrição

Acumulados Ficha Financeira - p/ Mês

---

## Resumo

- Campos: 11
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| PerRef | Date | Não | Competência dos Acumulados |
| FerPag | Number(014,2) | Sim | Valor das Férias Pagas no Mês |
| TerPag | Number(014,2) | Sim | Valor do 1/3 Férias Pagas no Mês |
| Pag13s | Number(014,2) | Sim | Valor do 13° Salário Pago (Integral ou Rescisão) no Mês |
| Adt13s | Number(014,2) | Sim | Valor do 13° Salário Adiantado no Mês |
| Ind13s | Number(014,2) | Sim | Valor do 13° Salário Indenizado no Mês |
| Mat13s | Number(014,2) | Sim | Valor do 13° Salário Auxílio Maternidade no Mês |
| ValRem | Number(011,2) | Sim | Valor da Remuneração |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- PerRef

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R046AFM_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

