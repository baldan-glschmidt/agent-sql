# R235AGE

## Descrição

Compromissos - Agenda

---

## Resumo

- Campos: 8
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeCom | String(020) | Não | Identificador do compromisso |
| CodRec | Number(010,0) | Não | Recurso |
| DatIni | Date | Sim | Início do compromisso |
| HorIni | Number(005,0) | Sim | Hora de início |
| AssAge | String(020) | Sim | Assunto do agendamento |
| DatFim | Date | Sim | Fim do compromisso |
| HorFim | Number(005,0) | Sim | Hora término |
| DesAge | String(1999) | Sim | Descrição do agendamento |

---

## Chave Primária

- IdeCom
- CodRec

---

## Índices

### R235AGEIndice1

**Tipo:** Não unico

Campos:
- CodRec
- DatIni
- HorIni
- DatFim
- HorFim

---

## Relacionamentos

### IR_R235AGE_000

**Tabela:** R235COM

| Origem | Destino |
|--------|---------|
| IdeCom | IdeCom |

### IR_R235AGE_001

**Tabela:** R235REC

| Origem | Destino |
|--------|---------|
| CodRec | CodRec |

