# R350SOF

## Descrição

S-1000 - eSocial - Informações da Software House

---

## Resumo

- Campos: 19
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| CodFil | Number(006,0) | Não | Código da Filial |
| SeqEmp | Number(009,0) | Não | Sequência |
| SeqSof | Number(009,0) | Não | Sequência |
| CnpSof | Number(014,0) | Sim | CNPJ da Software House |
| CfjIns | String(014) | Sim | CNPJ da Software House |
| RazSof | String(080) | Sim | Razão Social da Software House |
| ConSof | String(070) | Sim | Nome do contato na Software House |
| TelSof | String(013) | Sim | Informar o número do telefone, com DDD da Software House |
| EmaSof | String(060) | Sim | Endereço eletrônico da Software House |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| TipOpe | Number(001,0) | Sim | Tipo operação do leiaute. |
| LayOut | String(006) | Sim | Leiaute |
| DdiTel | Number(003,0) | Sim | USO EXCLUSIVO SENIOR |
| DddTel | Number(003,0) | Sim | USO EXCLUSIVO SENIOR |
| NumTel | String(020) | Sim | USO EXCLUSIVO SENIOR |
| CodOem | Number(008,0) | Sim | Código Outra Empresa |
| DatIni | Date | Sim | Competência de início |

---

## Chave Primária

- NumEmp
- FilEmp
- CodFil
- SeqEmp
- SeqSof

---

## Índices

### R350SOFIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
