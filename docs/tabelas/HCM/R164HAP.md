# R164HAP

## Descrição

Histórico de Anexos do Plano

---

## Resumo

- Campos: 4
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodOem | Number(008,0) | Não | Código Outra Empresa |
| CodPla | Number(003,0) | Não | Código do Plano |
| DatAlt | Date | Não | Data da alteração do histórico |
| TipAca | String(001) | Não | Indica se é inclusão, alteração ou exclusão no plano |

---

## Chave Primária

- CodOem
- CodPla
- DatAlt
- TipAca

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R164HAP_000

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

### IR_R164HAP_001

**Tabela:** R164PLA

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |
| CodPla | CodPla |

