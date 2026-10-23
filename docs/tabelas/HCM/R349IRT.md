# R349IRT

## Descrição

S-5002 - eSocial - Imposto de Renda Retido na Fonte por Trabalhador

---

## Resumo

- Campos: 12
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| CpfTra | Number(011,0) | Não | CPF do trabalhador |
| SeqTab | Number(009,0) | Não | Sequência |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| RecBas | String(040) | Sim | Número do recibo do arquivo de origem (S-1210) |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição (CNPJ/CPF) - Obsoleto |
| CfjIns | String(014) | Sim | Número de inscrição (CNPJ/CPF) |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| VlrDep | Number(014,2) | Sim | Valor dedução base de cálculo do IRRF dos dependentes do beneficiário do pgto. |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- SeqTab

---

## Índices

### R349IRTIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
