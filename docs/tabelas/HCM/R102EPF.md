# R102EPF

## Descrição

Epi da Brigada - por função

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número Empresa |
| CodFnb | Number(003,0) | Não | Função da Brigada |
| CodEpi | Number(008,0) | Não | Código do Equipamento |

---

## Chave Primária

- NumEmp
- CodFnb
- CodEpi

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R102EPF_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R102EPF_001

**Tabela:** R102FNB

| Origem | Destino |
|--------|---------|
| CodFnb | CodFnb |

### IR_R102EPF_002

**Tabela:** R096EPI

| Origem | Destino |
|--------|---------|
| CodEpi | CodEpi |

