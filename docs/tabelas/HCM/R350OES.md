# R350OES

## Descrição

S-2399 - eSocial - Desligamento Trabalhador Sem Vínculo - Informação de múltiplos vínculos

---

## Resumo

- Campos: 14
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro |
| SeqRsv | Number(009,0) | Não | Sequência |
| SeqMvs | Number(009,0) | Não | Sequência |
| SeqOes | Number(009,0) | Não | Sequência |
| SeqOcs | String(010) | Sim | Seq. Outros Contratos |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição (CNPJ/CPF) - Obsoleto |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte |
| CodCat | Number(004,0) | Sim | Código da categoria atribuída ao trabalhador |
| ValRem | Number(014,2) | Sim | Valor da remuneração recebida pelo trabalhador na outra empresa/atividade |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqRsv
- SeqMvs
- SeqOes

---

## Índices

### R350OESIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
