# E095LLT

## Descrição

Cadastros - Ligação da Lotação Tributária x Fornecedor por Filial

---

## Resumo

- Campos: 13
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| IdeLot | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do Fornecedor |
| ValIni | Date | Não | Validade Inicial |
| ValFim | Date | Não | Validade Final |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E095LLTIndice1

**Tipo:** Unico

Campos:
- IdeLot
- CodEmp
- CodFil
- CodFor
- ValIni
- ValFim

### E095LLTIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodFor

---

## Relacionamentos

Nenhum relacionamento cadastrado.
