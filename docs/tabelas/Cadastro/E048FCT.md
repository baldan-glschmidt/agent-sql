# E048FCT

## Descrição

Tabelas - Formas de Contabilização

---

## Resumo

- Campos: 8
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFct | String(005) | Não | Código da forma de contabilização |
| DesFct | String(040) | Não | Descrição da forma de contabilização |
| OriFct | String(003) | Não | Módulo de origem da forma de contabilização |
| BasFct | Number(001,0) | Não | Indicativo da tabela base da forma de contabilização para vendas e compras |
| SitReg | String(001) | Não | Situação do registro |
| ObsFct | String(250) | Sim | Observação da forma de contabilização |
| DatAlt | Date | Sim | Data da última alteração do registro |

---

## Chave Primária

- CodEmp
- CodFct

---

## Índices

### E048FCTIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodFct
- OriFct

---

## Relacionamentos

Nenhum relacionamento cadastrado.
