# E069FIL

## Descrição

Tabelas - Convênios - Ligação Convênio x Filial

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodCnv | Number(004,0) | Não | Código do convênio |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| SitReg | String(001) | Sim | Situação do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E069FILIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodCnv

---

## Relacionamentos

Nenhum relacionamento cadastrado.
