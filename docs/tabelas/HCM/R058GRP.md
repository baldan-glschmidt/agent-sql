# R058GRP

## Descrição

Grupos de Coletores da Permissão de Acesso

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPrm | Number(005,0) | Não | Código da Permissão |
| CodGrr | Number(003,0) | Não | Código do Grupo de Coletores |
| CodFai | Number(003,0) | Sim | Código da Faixa Horária |

---

## Chave Primária

- CodPrm
- CodGrr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058GRP_000

**Tabela:** R058PRM

| Origem | Destino |
|--------|---------|
| CodPrm | CodPrm |

### IR_R058GRP_001

**Tabela:** R058GRR

| Origem | Destino |
|--------|---------|
| CodGrr | CodGrr |

