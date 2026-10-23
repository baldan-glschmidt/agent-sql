# R350PSC

## Descrição

S-1210 - eSocial - Plano de saúde coletivo - Identificação da(s) operadora(s)

---

## Resumo

- Campos: 12
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| SeqPrt | Number(009,0) | Não | Sequência |
| SeqInf | Number(009,0) | Não | Sequência |
| SeqPsc | Number(009,0) | Não | Sequência |
| CnpjOp | Number(014,0) | Sim | CNPJ da operadora de plano privado coletivo empresarial de assistência à saúde |
| CfjIns | String(014) | Sim | CNPJ da operadora de plano privado coletivo empresarial de assistência à saúde |
| RegANS | Number(006,0) | Sim | Registro na Agência Nacional de Saúde - ANS |
| VlrTit | Number(014,2) | Sim | Valor relativo à dedução do rendimento tributável correspondente a pagamento a plano de saúde do titular |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- IndApu
- SeqPrt
- SeqInf
- SeqPsc

---

## Índices

### R350PSCIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
