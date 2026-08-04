# E051SUS

## Descrição

Tabelas - Impostos - Suspensão de Exigibilidade

---

## Resumo

- Campos: 13
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodDfs | Number(006,0) | Não | Código do dispositivo fiscal |
| CodSus | Number(014,0) | Sim | Codigo da Suspensão |
| IndSus | Number(002,0) | Sim | Indicador de suspensão da exigibilidade |
| DatDec | Date | Sim | Data da Decisão |
| IndDep | String(001) | Sim | Indicativo de depósito do montante integral |
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

### E051SUSIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodDfs

---

## Relacionamentos

### IR_E051SUS_002

**Tabela:** E051DIS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodDfs | CodDfs |

