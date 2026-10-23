# R146EMP

## Descrição

Provisão - Empresas

---

## Resumo

- Campos: 2
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipPrv | Number(004,0) | Não | Tipo de Provisão |
| NumEmp | Number(004,0) | Não | Código da Empresa |

---

## Chave Primária

- TipPrv
- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R146EMP_000

**Tabela:** R146DEF

| Origem | Destino |
|--------|---------|
| TipPrv | TipPrv |

### IR_R146EMP_001

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

