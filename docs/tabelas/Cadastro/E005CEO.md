# E005CEO

## Descrição

Tabelas - Ligação Célula X Estágio/Operação

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodCel | String(004) | Não | Código da Célula de Produção(Grupos de Trabalho) |
| CodEtg | Number(004,0) | Não | Código do Estágio ao qual a Célula está Vinculada |
| SitCeo | String(001) | Não | Situação do Relacionamento entre a Célula e o Estágio/Operação |

---

## Chave Primária

- CodEmp
- CodCel
- CodEtg

---

## Índices

### E005CEOIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodEtg

---

## Relacionamentos

### IR_E005CEO_001

**Tabela:** E005CEL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCel | CodCel |

### IR_E005CEO_002

**Tabela:** E093ETG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodEtg | CodEtg |

