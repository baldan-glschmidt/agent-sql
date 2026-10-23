# R206DML

## Descrição

PLR Paquetá - Dados Mensais p/ Loja

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CmpRef | Date | Não | Competência dos Dados da Loja |
| ValFat | Number(011,2) | Sim | Valor do Faturamento da Loja |
| PerPlr | Number(005,2) | Sim | Percentual PLR s/ Faturamento |
| ValPlr | Number(011,2) | Sim | Valor do PLR (Faturamento * percentual / 100) |
| QtdCol | Number(004,0) | Sim | Quantidade de Colaboradores |

---

## Chave Primária

- NumEmp
- TabOrg
- NumLoc
- CmpRef

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R206DML_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R206DML_002

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

