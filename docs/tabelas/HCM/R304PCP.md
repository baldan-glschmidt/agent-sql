# R304PCP

## Descrição

e-Sfinge Online - Proventos da Concessão Pensão

---

## Resumo

- Campos: 14
- Chave Primária: 8 campo(s)
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
| SeqPro | Number(008,0) | Não | Sequencial do provento |
| SeqReg | Number(009,0) | Não | Sequência |
| ValPro | Number(015,2) | Sim | Valor do provento |
| TipPro | Number(002,0) | Sim | Tipo provento |
| DesPro | String(255) | Sim | Descrição do provento |
| AnoRef | Date | Sim | Ano/Mês de referência do provento |
| TipPde | Number(002,0) | Sim | Tipo provento desconto |
| PidSta | String(030) | Sim | Pid status |

---

## Chave Primária

- NumEmp
- NumAto
- DatAto
- NumMat
- NumCpf
- CodUni
- SeqPro
- SeqReg

---

## Índices

### R304PCPIndice1

**Tipo:** Não unico

Campos:
- PidSta

---

## Relacionamentos

Nenhum relacionamento cadastrado.
