# R350DLT

## Descrição

S-2299 - eSocial - Estabelecimento/Lotação do trabalhador no período de apuração

---

## Resumo

- Campos: 14
- Chave Primária: 7 campo(s)
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
| SeqDlt | Number(009,0) | Não | Sequência |
| CodIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição da lotação |
| InsLot | Number(015,0) | Sim | Número de inscrição do contribuinte da Lotação |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte da Lotação |
| CodLot | String(030) | Sim | Código da Lotação tributária. |
| GraExp | Number(001,0) | Sim | Código que Representa o Grau de Exposição  Agentes Nocivos |
| OpcSim | Number(001,0) | Sim | Indicador de contribuição substituída |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqDes
- SeqRec
- SeqDlt

---

## Índices

### R350DLTIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
