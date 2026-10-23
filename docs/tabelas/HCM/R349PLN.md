# R349PLN

## Descrição

S-5002 - eSocial - Plano de saúde coletivo

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
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| CpfTra | Number(011,0) | Não | CPF do trabalhador |
| SeqTab | Number(009,0) | Não | Sequência |
| SeqCpl | Number(009,0) | Não | Sequência |
| SeqPln | Number(009,0) | Não | Sequência |
| NumIns | Number(014,0) | Sim | Número do CNPJ da Operadora de Plano Privado Coletivo Empresarial de Assistência à Saúde |
| CfjIns | String(014) | Sim | Número do CNPJ da Operadora de Plano Privado Coletivo Empresarial de Assistência à Saúde |
| RegAns | String(006) | Sim | Registro na Agência Nacional de Saúde - ANS |
| VlrDed | Number(014,2) | Sim | Valor relativo à dedução do rendimento tributável correspondente a pagamento a plano de saúde do titular |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- SeqTab
- SeqCpl
- SeqPln

---

## Índices

### R349PLNIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
