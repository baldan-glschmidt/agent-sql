# R070TMP

## Descrição

Eventos recebidos pela CSM

---

## Resumo

- Campos: 10
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatRec | Date | Não | Data de recebimento |
| HorRec | Number(005,0) | Não | Hora de recebimento |
| SeqRec | Number(009,0) | Não | Sequência de recebimento |
| VlrRec | Image | Sim | Valor recebido |
| StaRec | String(001) | Sim | Status do recebimento |
| DatPro | Date | Sim | Data do processamento |
| HorPro | Number(005,0) | Sim | Hora do processamento |
| SeqPro | Number(002,0) | Sim | Sequência do processamento |
| TipEvM | Number(001,0) | Sim | Tipo do evento de marcação |
| VerAdp | Number(008,0) | Sim | Versão do aplicativo Adapter (comunicação Digicon) - G6 |

---

## Chave Primária

- DatRec
- HorRec
- SeqRec

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
