# E000LEP

## Descrição

Automatismos de processos - Métricas

---

## Resumo

- Campos: 15
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | String(050) | Não | Identificador único alfanumérico |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| DatIni | Date | Sim | Data e hora inicial da execucao |
| DatFim | Date | Sim | Data e hora final da execucao |
| CodPra | Number(004,0) | Não | Código do processo automático |
| ProOri | Number(009,0) | Sim | Processo Origem 1. 1 = Fila Principal, 2 = Fila Secundária |
| QtdPro | Number(009,0) | Sim | Quantidade a gerar |
| QtdGer | Number(009,0) | Sim | Quantidade de documentos gerados |
| QtdErr | Number(009,0) | Sim | Quantidade de documentos processados que geraram erro |
| NivPar | Number(009,0) | Sim | Nível do paralelismo do processo (1..10) |
| SeqPar | Number(009,0) | Sim | Sequencia do paralelismo do processo (1..10) |
| UltAlt | Date | Sim | Data e hora da última atualização |
| RotOri | String(050) | Sim | Nome da rotina origem |
| NomSrv | String(255) | Sim | Nome do servidor/máquina e PID de execução |

---

## Chave Primária

- IdeUni

---

## Índices

### E000LEPIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- DatIni

---

## Relacionamentos

Nenhum relacionamento cadastrado.
