# E099PXU

## Descrição

Usuários da rotina de parametrização genérica

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
| IdePrm | Number(009,0) | Não | Identificador da rotina vinculada |
| CodUsu | Number(009,0) | Não | Usuário atual vinculado a parametrização |
| SitPrm | String(001) | Não | Situação da rotina para o usuário selecionado |
| UsuGer | Number(010,0) | Não | Usuário responsável pela geração do registro |
| DatGer | Date | Não | Data da geração do registro |
| HorGer | Number(005,0) | Não | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E099PXUIndice1

**Tipo:** Não unico

Campos:
- IdePrm

---

## Relacionamentos

### IR_E099PXU_001

**Tabela:** E099ROT

| Origem | Destino |
|--------|---------|
| IdePrm | IdeUni |

