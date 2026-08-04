# E000OBI

## Descrição

Insights - Observações

---

## Resumo

- Campos: 8
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodIsg | Number(009,0) | Não | Código do insight de processo automático |
| SeqObs | Number(003,0) | Não | Sequência da observação do insight |
| CodMot | Number(006,0) | Sim | Código do motivo da reprovação do insight de processo automático |
| TipObs | String(001) | Não | Tipo da observação |
| ObsIsg | String(250) | Não | Texto da observação do insight |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodIsg
- SeqObs

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
