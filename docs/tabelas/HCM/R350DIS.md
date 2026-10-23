# R350DIS

## Descrição

S-2299 - eSocial - Identificação do Acordo/Convenção/Dissídio

---

## Resumo

- Campos: 13
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
| SeqDes | Number(009,0) | Não | Sequência |
| SeqRec | Number(009,0) | Não | Sequência |
| SeqDis | Number(009,0) | Não | Sequência |
| DatAco | Date | Sim | Data do acordo, convenção ou dissídio |
| TipAco | String(001) | Sim | Tipo de acordo |
| DatEft | Date | Sim | Data de Efeito do acordo, convenção ou dissídio |
| ObsDis | String(255) | Não | Descrição do instrumento/situação que originou o pagamento das verbas |
| CmpAcc | Date | Sim | Comp. obrig. efeitos remuneratórios/ac. colet./conv. colet./sentença normativa |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqDes
- SeqRec
- SeqDis

---

## Índices

### R350DISIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
