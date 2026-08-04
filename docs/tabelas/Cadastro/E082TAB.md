# E082TAB

## Descrição

Tabelas - Tabelas de Preços de Fornecedores - Dados Gerais

---

## Resumo

- Campos: 8
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTpr | String(004) | Não | Código da tabela de preço de fornecedor |
| DesTpr | String(030) | Não | Descrição da tabela de preço do fornecedor |
| AbrTpr | String(010) | Não | Abreviatura da tabela de preço do fornecedor |
| CodMoe | String(003) | Não | Código da moeda |
| CodFor | Number(009,0) | Sim | Código do fornecedor |
| UtiPme | String(001) | Sim | Indicativo se utiliza preço médio como preço base dos itens da tabela de preço |
| ObsTab | String(100) | Sim | Dados Gerais - Observação |

---

## Chave Primária

- CodEmp
- CodTpr

---

## Índices

### E082TABIndice1

**Tipo:** Não unico

Campos:
- CodMoe

---

## Relacionamentos

### IR_E082TAB_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E082TAB_004

**Tabela:** E031MOE

| Origem | Destino |
|--------|---------|
| CodMoe | CodMoe |

