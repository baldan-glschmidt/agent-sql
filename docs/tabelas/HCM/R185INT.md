# R185INT

## Descrição

Orçamento Individual - Definiçoes de Integração de Valores

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código Empresa |
| AnoBas | Number(004,0) | Não | Ano base de cálculo do orçamento |
| VerOrc | Number(004,0) | Não | Versão do orçamento |
| RevOrc | Number(004,0) | Não | Revisão  da versão do orçamento |
| CodUsu | Number(010,0) | Não | Código do Usuário |
| AnoInt | Number(004,0) | Sim | Ano base para integração de valores |
| VerInt | Number(004,0) | Sim | Versão para integração de valores do cenário |
| Revint | Number(004,0) | Sim | Revisão  para integração dos valores do cenário. |
| IntFin | String(001) | Sim | Os valores do orçamento foram integrados com o Financeiro (S/N)? |
| ObsInt | String(2000) | Sim | Observações de integração |

---

## Chave Primária

- NumEmp
- AnoBas
- VerOrc
- RevOrc
- CodUsu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R185INT_002

**Tabela:** R185VER

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| AnoBas | AnoBas |
| VerOrc | VerOrc |

