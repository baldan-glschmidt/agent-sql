# R349CSE

## Descrição

S-5011 - eSocial - Informações das Contribuições Sociais Consolidadas por Contribuinte

---

## Resumo

- Campos: 23
- Chave Primária: 5 campo(s)
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
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição (CNPJ/CPF) - Obsoleto |
| CfjIns | String(014) | Sim | CNPJ Alfanumérico |
| RecBas | String(040) | Sim | Número do recibo do arquivo de origem (S-4000/1299) |
| ExiVal | Number(009,0) | Sim | Indicativo de existência de valores de bases e de contribuições sociais |
| TotDes | Number(014,2) | Sim | Valor total da contribuição descontada dos segurados |
| TotCon | Number(014,2) | Sim | Valor total calculado relativa à contribuição dos segurados |
| ClaTri | Number(002,0) | Sim | Código Correspondente à Classificação Tributária do Contribuinte |
| IndCoo | Number(001,0) | Sim | Indicativo de Cooperativa |
| IndCon | Number(001,0) | Sim | Indicativo de Construtora |
| IndSub | Number(001,0) | Sim | Indicativo de substituição patronal |
| PerRed | Number(005,2) | Sim | Percentual de redução |
| FatMes | Number(005,2) | Sim | Fator cálculo da contribuição patronal do mês |
| Fat13s | Number(005,2) | Sim | Fator cálc. da contrib. patronal do décimo terceiro |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| PerTra | Number(001,0) | Sim | Informe o percentual de contribuição social devida |
| InfPis | String(001) | Sim | Indicador de tributação sobre a folha de pagamento - PIS e PASEP |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- SeqTab

---

## Índices

### R349CSEIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
