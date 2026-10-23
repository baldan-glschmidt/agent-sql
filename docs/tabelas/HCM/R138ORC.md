# R138ORC

## Descrição

Orçamento por Centro de Custo

---

## Resumo

- Campos: 9
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCcu | String(018) | Não | Código Centro Custo Contábil |
| AnoBas | Number(004,0) | Não | Ano Base do Orçamento |
| CodIdm | Number(003,0) | Sim | Código do Índice Conversão |
| TipOrc | Number(001,0) | Sim | Tipo de Orçamento |
| CodUsu | Number(010,0) | Sim | Código do Usuário que gerou o Orçamento |
| TipCol | Number(001,0) | Sim | Tipo do Colaborador Responsável |
| NumCad | Number(009,0) | Sim | Cadastro do Responsável |
| ObsCur | String(200) | Sim | Observações |

---

## Chave Primária

- NumEmp
- CodCcu
- AnoBas

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R138ORC_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

