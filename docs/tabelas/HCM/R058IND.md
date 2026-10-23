# R058IND

## Descrição

Indisponibilidades do Dispositivo

---

## Resumo

- Campos: 9
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodDsp | Number(009,0) | Não | Código do Dispositivo |
| DatInd | Date | Não | Data da indisponibilidade do dispositivo |
| HorInd | Number(005,0) | Não | Hora da indisponibilidade do dispositivo |
| DatPrv | Date | Sim | Data de previsão de retorno do dispositivo |
| HorPrv | Number(005,0) | Sim | Hora de previsão de retorno do dispositivo |
| DatRet | Date | Sim | Data de retorno do dispositivo |
| HorRet | Number(005,0) | Sim | Hora de retorno do dispositivo |
| MotInd | String(100) | Sim | Motivo da indisponibilidade do dispositivo |
| Protcl | String(036) | Sim | Protocolo do evento retornado pela ADE-02 |

---

## Chave Primária

- CodDsp
- DatInd
- HorInd

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
