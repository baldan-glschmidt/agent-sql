# R018CCR

## Descrição

Coletores/Funções Rateio C. Custo

---

## Resumo

- Campos: 5
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCcu | String(018) | Não | Código C.Custo |
| CodPlt | Number(005,0) | Não | Código do Site |
| CodRlg | Number(005,0) | Não | Código do Coletor p/Rateio |
| CodFnc | Number(002,0) | Não | Código da Função p/Rateio |

---

## Chave Primária

- NumEmp
- CodCcu
- CodPlt
- CodRlg
- CodFnc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R018CCR_001

**Tabela:** R018CCU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |

