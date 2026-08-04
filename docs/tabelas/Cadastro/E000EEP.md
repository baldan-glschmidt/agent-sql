# E000EEP

## Descrição

Parâmetros de execução de processos para fechamento da Controladoria

---

## Resumo

- Campos: 5
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| IdeHep | Number(009,0) | Não | Identificador do histórico do processo |
| TipEep | Number(002,0) | Não | Tipo de mensagem |
| MsgEep | String(1000) | Sim | Mensagem ocorrida na execução do processo |
| DatEep | Date | Não | Data/hora em que o evento ocorreu |

---

## Chave Primária

- IdeUni

---

## Índices

### E000EEPIndice1

**Tipo:** Não unico

Campos:
- IdeHep

---

## Relacionamentos

### IR_E000EEP_001

**Tabela:** E000HEP

| Origem | Destino |
|--------|---------|
| IdeHep | IdeUni |

