# E017REL

## Descrição

Tabelas - Configuração de leiaute do Recebimento Eletrônico - Registros

---

## Resumo

- Campos: 12
- Chave Primária: 1 campo(s)
- Índices: 3
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| IdeLre | Number(009,0) | Não | Identificador de registro |
| CodRel | String(060) | Não | Código do registro no leiaute |
| DesRel | String(100) | Não | Descrição do registro no leiaute |
| IdeSup | Number(009,0) | Sim | Identificador do registro superior |
| CodReg | Number(004,0) | Sim | Código da Regra |
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

### E017RELIndice1

**Tipo:** Unico

Campos:
- IdeLre
- CodRel
- IdeSup

### E017RELIndice2

**Tipo:** Não unico

Campos:
- IdeLre

### E017RELIndice3

**Tipo:** Não unico

Campos:
- IdeSup

---

## Relacionamentos

### IR_E017REL_001

**Tabela:** E017LRE

| Origem | Destino |
|--------|---------|
| IdeLre | IdeUni |

