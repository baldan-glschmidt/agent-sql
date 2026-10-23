# R151PJU

## Descrição

Vínculo de Pessoas Jurídicas e Legislação

---

## Resumo

- Campos: 12
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCgc | Number(015,0) | Sim | Número da Inscrição - Obsoleto |
| CfjIns | String(014) | Não | Número da Inscrição |
| CodLeg | Number(003,0) | Não | Código da legislação |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| CodFil | Number(006,0) | Sim | Código de Filial |
| CodOem | Number(008,0) | Sim | Código outra empresa |
| DatInc | Date | Sim | Data Integração BDCC |
| DatIni | Date | Sim | Data de início da vigência |
| HorIni | Number(005,0) | Sim | Hora início da vigência |
| DatFim | Date | Sim | Data fim da vigência |
| HorFim | Number(005,0) | Sim | Hora fim da vigência |
| Status | Number(001,0) | Sim | Status do vínculo |

---

## Chave Primária

- CfjIns
- CodLeg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
