# E015MED

## Descrição

Cadastros - Unidades de Medida

---

## Resumo

- Campos: 12
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| UniMed | String(003) | Não | Unidade de medida |
| DesMed | String(040) | Não | Descrição da unidade de medida |
| QtdDec | Number(001,0) | Sim | Quantidade de decimais utilizada para a unidade de medida (Até 5) |
| CodReg | Number(004,0) | Sim | Código da regra |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para integração |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |
| TipInt | Number(001,0) | Sim | Tipo de Integração |
| IndPes | String(001) | Sim | Indicativo se no Varejo é obrigatória a pesagem do produto antes de |
| UniFis | String(006) | Sim | Unidade de medida fiscal |
| UniEcf | String(002) | Sim | Unidade de medida para ECF |
| IntPos | String(001) | Sim | Indicativo se o registro integra no Gestão Safra |

---

## Chave Primária

- UniMed

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
