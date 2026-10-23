# R098RTE

## Descrição

Revisão de Tipo de Equipamentos

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipEqp | Number(003,0) | Não | Código Tipo de Equipamento |
| TipSvc | Number(003,0) | Não | Tipo de Serviço |
| QtdDia | Number(005,0) | Sim | Quantidade de Dias para Revisão |
| RegAnt | Number(003,0) | Sim | Código da Regra Antes |
| RegDep | Number(003,0) | Sim | Código da Regra Depois |

---

## Chave Primária

- TipEqp
- TipSvc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R098RTE_000

**Tabela:** R098TEQ

| Origem | Destino |
|--------|---------|
| TipEqp | TipEqp |

### IR_R098RTE_001

**Tabela:** R098SVC

| Origem | Destino |
|--------|---------|
| TipSvc | TipSvc |

