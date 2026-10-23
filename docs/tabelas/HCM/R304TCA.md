# R304TCA

## Descrição

e-Sfinge Online - Tempos de Serviço da Concessão Aposentadoria

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
| NumEmp | Number(004,0) | Não | Código da Empresa |
| NumAto | String(016) | Não | Número do ato de pessoal |
| DatAto | Date | Não | Data do ato de pessoal |
| NumMat | String(016) | Não | Número da matrícula do servidor na unidade |
| NumCpf | Number(011,0) | Não | Código de identificação do contribuinte na receita federal |
| CodUni | Number(016,0) | Não | Código da unidade gestora do servidor |
| OrgTem | Number(003,0) | Não | Origem do tempo de serviço |
| DatItp | Date | Não | Data de início do tempo de serviço |
| SeqReg | Number(009,0) | Não | Sequência |
| DatFtp | Date | Sim | Data de fim do tempo de serviço |
| NumEdi | String(050) | Sim | Número do edital |
| NumPor | String(050) | Sim | Número da portaria de admissão |
| IndReg | String(001) | Sim | Indicativo regime próprio |
| QtdDia | Number(008,0) | Sim | Quantidade de dias |
| TipVin | Number(003,0) | Sim | Tipo de vínculo de origem |
| PidSta | String(030) | Sim | Pid status |

---

## Chave Primária

- NumEmp
- NumAto
- DatAto
- NumMat
- NumCpf
- CodUni
- OrgTem
- DatItp
- SeqReg

---

## Índices

### R304TCAIndice1

**Tipo:** Não unico

Campos:
- PidSta

---

## Relacionamentos

Nenhum relacionamento cadastrado.
