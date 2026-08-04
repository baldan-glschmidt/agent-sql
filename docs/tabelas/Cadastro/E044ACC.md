# E044ACC

## Descrição

Agrupamentos de Centros de Custo

---

## Resumo

- Campos: 8
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodAcc | String(005) | Não | Código de agrupamento de Centros de Custo |
| DesAcc | String(080) | Não | Descrição do centro de custos |
| AbrAcc | String(020) | Não | Abreviatura do centro de custos |
| TipAcc | Number(001,0) | Sim | Tipo de agrupamento |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |

---

## Chave Primária

- CodEmp
- CodAcc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E044ACC_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

