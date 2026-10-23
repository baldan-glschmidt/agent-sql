# R110RSD

## Descrição

Medicamentos - Saldo Diário

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRem | Number(006,0) | Não | Código do Medicamento |
| CodPos | Number(007,0) | Não | Código do posto de atendimento |
| DatSdo | Date | Não | Data do saldo |
| QtdSdo | Number(010,4) | Sim | Saldo do medicamento na data |
| FusHor | Number(002,0) | Sim | Fuso Horário |

---

## Chave Primária

- CodRem
- CodPos
- DatSdo

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110RSD_000

**Tabela:** R110REM

| Origem | Destino |
|--------|---------|
| CodRem | CodRem |

