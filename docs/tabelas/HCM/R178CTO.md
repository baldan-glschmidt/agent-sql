# R178CTO

## Descrição

Contas Totais

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
| FilCtb | Number(006,0) | Não | Filial Contábil |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodClc | Number(004,0) | Não | Código do CLC |
| HisPad | Number(004,0) | Sim | Código Histórico Padrão |
| GerGer | String(001) | Sim | Gerar Gerencial |

---

## Chave Primária

- NumEmp
- FilCtb
- TabEve
- CodClc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R178CTO_001

**Tabela:** R178DTO

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| FilCtb | FilCtb |

### IR_R178CTO_003

**Tabela:** R048CLC

| Origem | Destino |
|--------|---------|
| TabEve | TabEve |
| CodClc | CodClc |

