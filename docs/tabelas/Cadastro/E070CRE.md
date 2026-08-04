# E070CRE

## Descrição

Parâmetros do Recebimento Eletrônico - Grupos de Campos - Campos

---

## Resumo

- Campos: 9
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| IdeGre | Number(009,0) | Não | Identificador do grupo de campos de recebimento eletrônico |
| NomCmp | String(006) | Não | Nome do campo |
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

### E070CREIndice1

**Tipo:** Unico

Campos:
- IdeGre
- NomCmp

---

## Relacionamentos

### IR_E070CRE_001

**Tabela:** E070GRE

| Origem | Destino |
|--------|---------|
| IdeGre | IdeUni |

