# R174CCU

## Descrição

Contas C. Custo

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCcu | String(018) | Não | Código do C.Custo Contábil |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodClc | Number(004,0) | Não | Código do CLC |
| HisPad | Number(004,0) | Sim | Código Histórico Padrão |
| GerGer | String(001) | Sim | Gerar Gerencial |

---

## Chave Primária

- NumEmp
- CodCcu
- TabEve
- CodClc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R174CCU_001

**Tabela:** R018CCU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |

### IR_R174CCU_003

**Tabela:** R048CLC

| Origem | Destino |
|--------|---------|
| TabEve | TabEve |
| CodClc | CodClc |

