# E099UPA

## Descrição

Cadastros - Usuários - Tabela processos executados por usuário

---

## Resumo

- Campos: 9
- Chave Primária: 1 campo(s)
- Índices: 3
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodUsu | Number(010,0) | Não | Identificador do usuário |
| TipPro | Number(003,0) | Não | Tipo de Processamento |
| CmpPro | Date | Não | Competência de Processamento |
| SitPro | String(001) | Sim | Situação do Processamento |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E099UPA_FKIndex1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil

### E099UPA_FKIndex2

**Tipo:** Não unico

Campos:
- CodUsu

### E099UPAIndice2

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodUsu
- TipPro
- CmpPro

---

## Relacionamentos

Nenhum relacionamento cadastrado.
