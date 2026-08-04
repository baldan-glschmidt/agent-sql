# E069PSE

## Descrição

Tabelas - Seguros - Planos de seguro

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
| IdeCse | Number(009,0) | Não | Identificador do registro do cadastro de seguros |
| NumPar | Number(003,0) | Não | Parcelamento aceitável para o plano de seguro |
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

### E069PSEIndice2

**Tipo:** Não unico

Campos:
- IdeCse

---

## Relacionamentos

### IR_E069PSE_001

**Tabela:** E069CSE

| Origem | Destino |
|--------|---------|
| IdeCse | IdeUni |

