# R349ITF

## Descrição

S-5003 - eSocial - Informações relativas à matrícula e categoria do trabalhador

---

## Resumo

- Campos: 25
- Chave Primária: 9 campo(s)
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
| CpfTra | Number(011,0) | Não | CPF do trabalhador |
| SeqTab | Number(009,0) | Não | Sequência |
| SeqEoc | Number(009,0) | Não | Sequência Identificação do Estabelecimento |
| SeqIlt | Number(009,0) | Não | Sequência Identificação da Lotação |
| SeqItf | Number(009,0) | Não | Sequência Matrícula e Categoria do Trabalhador |
| MatTra | String(030) | Sim | Matrícula atribuída ao trabalhador pela empresa |
| CodCat | Number(004,0) | Sim | Código da categoria do trabalhador |
| CatOri | Number(004,0) | Sim | Código da categoria de origem do dirigente sindical ou do trabalhador cedido |
| RegTra | Number(001,0) | Sim | Tipo de regime trabalhista |
| RemSuc | String(001) | Sim | Remuneração é relativa a verbas devidas pela empresa sucessora |
| DatDes | Date | Sim | Data de desligamento do vínculo |
| MotDes | Number(002,0) | Sim | Código do Motivo do Desligamento |
| DatTer | Date | Sim | Data do Término |
| MotTsv | Number(002,0) | Sim | Motivo do desligamento do TSVE |
| ProJud | String(020) | Sim | Processo judicial que suspende a exigibilidade da Contribuição Social Rescisória |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição (CNPJ/CPF) - Obsoleto |
| CfjIns | String(014) | Sim | Número de inscrição (CNPJ/CPF) |
| MatAnt | String(030) | Sim | Matrícula do trabalhador no empregador anterior |
| DatAdm | Date | Sim | Data de admissão do trabalhador |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- CpfTra
- SeqTab
- SeqEoc
- SeqIlt
- SeqItf

---

## Índices

### R349ITFIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
