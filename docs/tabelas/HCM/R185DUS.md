# R185DUS

## Descrição

Revisão Ativa - por Empresa/Usuário

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodUsu | Number(010,0) | Não | Código do Usuário |
| AnoBas | Number(004,0) | Sim | Ano base da versão/revisão ativa de cálculo do orçamento |
| VerOrc | Number(004,0) | Sim | Versão ativa do orçamento |
| RevOrc | Number(004,0) | Sim | Revisão  ativa do orçamento |

---

## Chave Primária

- NumEmp
- CodUsu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R185DUS_004

**Tabela:** R185REV

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| AnoBas | AnoBas |
| VerOrc | VerOrc |
| RevOrc | RevOrc |

