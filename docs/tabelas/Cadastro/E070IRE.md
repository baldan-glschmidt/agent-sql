# E070IRE

## Descrição

Parâmetros do Recebimento Eletrônico - Itens

---

## Resumo

- Campos: 11
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| IdePre | Number(009,0) | Não | Identificador do parâmetro de recebimento eletrônico |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTns | String(005) | Não | Código da transação |
| CodFor | Number(009,0) | Não | Código do Fornecedor |
| DatGer | Date | Não | Data da geração do registro |
| HorGer | Number(005,0) | Não | Hora da geração do registro |
| UsuGer | Number(010,0) | Não | Usuário responsável pela geração do registro |
| DatAlt | Date | Não | Data da última alteração do registro |
| HorAlt | Number(005,0) | Não | Hora da última alteração do registro |
| UsuAlt | Number(010,0) | Não | Usuário responsável pela última alteração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E070IREIndice1

**Tipo:** Unico

Campos:
- IdePre
- CodTns
- CodFor

---

## Relacionamentos

### IR_E070IRE_001

**Tabela:** E070PRE

| Origem | Destino |
|--------|---------|
| IdePre | IdeUni |

