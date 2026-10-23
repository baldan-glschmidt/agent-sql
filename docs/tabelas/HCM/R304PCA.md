# R304PCA

## Descrição

e-Sfinge Online - Proventos da Concessão Aposentadoria

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
| NumAto | String(016) | Não | Número do Ato de Pessoal |
| DatAto | Date | Não | Data do Ato de Pessoal |
| NumMat | String(016) | Não | Número da matrícula do Servidor na Unidade |
| NumCpf | Number(011,0) | Não | Código de identificação do contribuinte na Receita Federal |
| CodUni | Number(016,0) | Não | Código da Unidade Gestora do Servidor |
| SeqPro | Number(008,0) | Não | Sequencial do Provento |
| SeqReg | Number(009,0) | Não | Sequência |
| ValPro | Number(015,2) | Sim | Valor do Provento |
| TipPro | Number(002,0) | Sim | Tipo Provento |
| DesPro | String(255) | Sim | Descrição do Provento |
| TipPde | Number(002,0) | Sim | Tipo Provento Desconto |
| AnoRef | Date | Sim | Ano/Mês de referência do provento |
| PidSta | String(030) | Sim | Pid Status |

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

### R304PCAIndice1

**Tipo:** Não unico

Campos:
- PidSta

---

## Relacionamentos

Nenhum relacionamento cadastrado.
