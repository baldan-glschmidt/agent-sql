# E070GRE

## Descrição

Parâmetros do Recebimento Eletrônico - Grupos de Campos

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| IdePre | Number(009,0) | Não | Identificador do parâmetro de recebimento eletrônico |
| DesGrp | String(020) | Não | Grupo de Campos |
| TipGrp | String(001) | Não | Tipo de Grupo |
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

### E070GREIndice1

**Tipo:** Unico

Campos:
- IdePre
- DesGrp

---

## Relacionamentos

### IR_E070GRE_001

**Tabela:** E070PRE

| Origem | Destino |
|--------|---------|
| IdePre | IdeUni |

