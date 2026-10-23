# R104REU

## Descrição

JR - Réu(Pessoa Jurídica)

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodPrc | Number(007,0) | Não | Código da Ação |
| CodOem | Number(008,0) | Não | Código do Réu - código da empresa na tabela  outra empresa |
| SeqReu | Number(003,0) | Sim | Sequência do Réu |

---

## Chave Primária

- NumEmp
- CodPrc
- CodOem

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R104REU_001

**Tabela:** R104PRJ

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |

### IR_R104REU_002

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

