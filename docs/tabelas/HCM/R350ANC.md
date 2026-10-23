# R350ANC

## Descrição

S-1270 - eSocial - Contratação Avulso Não Portuário - Contratante

---

## Resumo

- Campos: 18
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| SeqAnp | Number(009,0) | Não | Sequência |
| SeqTra | Number(009,0) | Não | Sequência Trabalhador Avulso |
| CodLot | String(030) | Sim | Código Lotação |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte |
| BasCon | Number(014,2) | Sim | Base Contribuição |
| Bas15A | Number(014,2) | Sim | Base Contribuição SAT 15 Anos |
| Bas20A | Number(014,2) | Sim | Base Contribuição SAT 20 Anos |
| Bas25A | Number(014,2) | Sim | Base Contribuição SAT 25 Anos |
| Bas13s | Number(014,2) | Sim | Base Contribuição 13º Salário |
| BasFgt | Number(014,2) | Sim | Base Contribuição FGTS |
| ConDes | Number(014,2) | Sim | Contribuição Descontada |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- IndApu
- SeqAnp
- SeqTra

---

## Índices

### R350ANCIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
