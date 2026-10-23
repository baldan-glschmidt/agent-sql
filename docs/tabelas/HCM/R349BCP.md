# R349BCP

## Descrição

S-5011 - eSocial - Informações da Comercialização da produção rural da pessoa física

---

## Resumo

- Campos: 13
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| PerApu | Date | Não | Período Apuração |
| SeqTab | Number(009,0) | Não | Sequência |
| SeqCeo | Number(009,0) | Não | Sequência |
| SeqBcp | Number(009,0) | Não | Sequência |
| IndCom | Number(001,0) | Sim | Indicativo de Comercialização |
| BasCom | Number(014,2) | Sim | Valor total da comercialização |
| ConSus | Number(014,2) | Sim | Valor da Contribuição Previdenciária com exigibilidade suspensa |
| RatSus | Number(014,2) | Sim | Valor da contribuição para Gilrat com exigibilidade suspensa |
| SenSus | Number(014,2) | Sim | Valor da contribuição destinada ao SENAR com elegibilidade suspensa |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- SeqTab
- SeqCeo
- SeqBcp

---

## Índices

### R349BCPIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
