# R060PFE

## Descrição

Perda Fériias Definições da Integração

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodSit | Number(003,0) | Não | Código da Situação de Perda Férias |
| TipLim | String(001) | Não | Tipo de Limite da Situação |

---

## Chave Primária

- NumEmp
- CodSit
- TipLim

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R060PFE_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R060PFE_001

**Tabela:** R010SIT

| Origem | Destino |
|--------|---------|
| CodSit | CodSit |

