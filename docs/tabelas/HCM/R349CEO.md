# R349CEO

## Descrição

S-5011 - eSocial - Identificação do estabelecimento ou obra de construção civil

---

## Resumo

- Campos: 22
- Chave Primária: 6 campo(s)
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
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte |
| CodCna | Number(007,0) | Sim | Código do CNAE 2.0 |
| AliRat | Number(001,0) | Sim | Alíquota definida no decreto 3.048/99 para a atividade (CNAE) preponderante |
| AliRa2 | Number(001,0) | Sim | Alíquota RAT definida na legislação vigente. |
| FatFap | Number(005,4) | Sim | Fator acidentário de prevenção |
| FatFa2 | Number(005,4) | Sim | Fator acidentário de prevenção estabelecido pelo órgão governamental competente. |
| RatAju | Number(005,4) | Sim | Alíquota após ajuste pelo FAP |
| RatAj2 | Number(005,4) | Sim | Alíquota de referência após ajuste pelo FAP |
| IndSub | Number(001,0) | Sim | Indicativo de Substituição da Contribuição Patronal de Obra de Construção Civil |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| CnpRes | Number(014,0) | Sim | CNPJ responsável pela inscrição no cadastro de obras da RFB |
| CfjRes | String(014) | Sim | CNPJ responsável pela inscrição no cadastro de obras da RFB |
| BasPis | Number(014,2) | Sim | Base PIS/PASEP |
| BPisSu | Number(014,2) | Sim | Base PIS/PASEP Suspensa |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- SeqTab
- SeqCeo

---

## Índices

### R349CEOIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
