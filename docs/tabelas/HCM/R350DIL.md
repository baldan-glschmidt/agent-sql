# R350DIL

## Descrição

S-2299 - eSocial - Estabelecimento/Lotação das diferenças de remuneração

---

## Resumo

- Campos: 16
- Chave Primária: 9 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro |
| SeqDes | Number(009,0) | Não | Sequência |
| SeqRec | Number(009,0) | Não | Sequência |
| SeqDis | Number(009,0) | Não | Sequência |
| SeqDpr | Number(009,0) | Não | Sequência |
| SeqDil | Number(009,0) | Não | Sequência |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte |
| CodLot | String(030) | Sim | Código atribuído pela empresa para a lotação |
| IndSim | Number(001,0) | Sim | Indicador de Contribuição Substituída |
| GraExp | Number(001,0) | Sim | Grau de exposição a agentes nocivos |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqDes
- SeqRec
- SeqDis
- SeqDpr
- SeqDil

---

## Índices

### R350DILIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
