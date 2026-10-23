# R349CIT

## Descrição

S-5002 - eSocial - Pgto. beneficiário residente fiscal no exterior (versão 2.5)

---

## Resumo

- Campos: 17
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
| SeqIrc | Number(009,0) | Não | Sequência |
| SeqCit | Number(009,0) | Não | Sequência |
| CodPai | Number(009,0) | Sim | Identificação do País onde foi efetuado o pagamento |
| IndNif | Number(001,0) | Sim | Indicativo do Número de Identificação Fiscal |
| NumFis | String(020) | Sim | Número de Identificação Fiscal |
| DesLog | String(100) | Sim | Descrição do logradouro |
| NroLog | String(010) | Sim | Número do logradouro |
| ComLog | String(030) | Sim | Complemento do logradouro |
| BaiRro | String(090) | Sim | Nome do bairro/distrito |
| NomCid | String(050) | Sim | Nome da cidade |
| CodPos | String(012) | Sim | Código de Endereçamento Postal |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- SeqTab
- SeqIrc
- SeqCit

---

## Índices

### R349CITIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
