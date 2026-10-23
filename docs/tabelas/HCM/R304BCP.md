# R304BCP

## Descrição

e-Sfinge Online - Beneficiários da Concessão Pensão

---

## Resumo

- Campos: 20
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
| CpfBen | Number(011,0) | Não | Código de identificação do contribuinte na receita federal do beneficiário |
| SeqBen | Number(008,0) | Não | Sequencial do beneficiário |
| SeqReg | Number(009,0) | Não | Sequência |
| NomBen | String(100) | Sim | Nome do beneficiário |
| DatCer | Date | Sim | Data da certidão |
| ValCot | Number(015,2) | Sim | Valor da cota |
| DatNas | Date | Sim | Data de nascimento |
| TipDep | Number(003,0) | Sim | Tipo dependência econômica |
| IndOut | String(001) | Sim | Indicativo de outras pensões |
| DesOut | String(100) | Sim | Descrição das outras pensões |
| NumCer | String(100) | Sim | Número da certidão do beneficiário |
| PerCot | Number(015,2) | Sim | Percentual da cota |
| VlrPro | Number(015,2) | Sim | Valor do primeiro provento |
| PidSta | String(030) | Sim | Pid status |

---

## Chave Primária

- NumEmp
- NumAto
- DatAto
- NumMat
- NumCpf
- CodUni
- CpfBen
- SeqBen
- SeqReg

---

## Índices

### R304BCPIndice1

**Tipo:** Não unico

Campos:
- PidSta

---

## Relacionamentos

Nenhum relacionamento cadastrado.
