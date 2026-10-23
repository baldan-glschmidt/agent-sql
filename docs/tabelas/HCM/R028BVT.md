# R028BVT

## Descrição

Embarque Vale Transporte

---

## Resumo

- Campos: 6
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmb | Number(004,0) | Não | Código do Embarque |
| NomEmb | String(020) | Sim | Nome do Embarque |
| CodCid | Number(007,0) | Sim | Código da Cidade de Embarque |
| CodBai | Number(004,0) | Sim | Código do Bairro de Embarque |
| CodLin | Number(005,0) | Sim | Linha do VTR |
| CodOem | Number(008,0) | Sim | Empresa do VTR |

---

## Chave Primária

- CodEmb

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R028BVT_003

**Tabela:** R074BAI

| Origem | Destino |
|--------|---------|
| CodCid | CodCid |
| CodBai | CodBai |

### IR_R028BVT_004

**Tabela:** R028LVT

| Origem | Destino |
|--------|---------|
| CodLin | CodLin |

### IR_R028BVT_005

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

