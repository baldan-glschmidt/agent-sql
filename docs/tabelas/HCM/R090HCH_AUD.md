# R090HCH_AUD

## Descrição

Auditoria Histórico de Crachás de Visitantes

---

## Resumo

- Campos: 10
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqReg | Number(015,0) | Não | Sequencia do Registro |
| VerSeq | Number(010,0) | Não | Versão da Sequencia |
| TipDoc | Number(001,0) | Não | Tipo do Documento do Visitante |
| NumDoc | String(020) | Não | Número do Documento do Visitante |
| DatIni | Date | Não | Data de Início do Uso do Crachá |
| HorIni | Number(005,0) | Não | Hora de Início do Uso do Crachá |
| SeqEnt | Number(002,0) | Não | Sequência do Registro |
| NumCra | Number(012,0) | Sim | Número do Crachá do Visitante |
| DatFim | Date | Sim | Data Final do Uso do Crachá |
| HorFim | Number(005,0) | Sim | Hora Final do Uso do Crachá |

---

## Chave Primária

- SeqReg
- VerSeq
- TipDoc
- NumDoc
- DatIni
- HorIni
- SeqEnt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
