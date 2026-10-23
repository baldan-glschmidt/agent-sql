# R056SFP

## Descrição

Valores SEFIP

---

## Resumo

- Campos: 28
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CmpRef | Date | Não | Competência SEFIP |
| CodCal | Number(005,0) | Não | Código do Cálculo |
| TipCol | Number(001,0) | Não | Tipo do Colabolador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| BasFgt | Number(011,2) | Sim | Base de FGTS Mensal |
| ValFgt | Number(011,2) | Sim | Valor de FGTS Mensal |
| ValAFg | Number(011,2) | Sim | Valor de FGTS Adicional Mensal |
| BasF13 | Number(011,2) | Sim | Base de FGTS de 13° Salário |
| ValF13 | Number(011,2) | Sim | Valor de FGTS de 13° Salário |
| ValA13 | Number(011,2) | Sim | Valor de FGTS Adicional 13° Salário |
| BasIns | Number(011,2) | Sim | Base de INSS Mensal |
| ValIns | Number(011,2) | Sim | Valor de INSS Mensal |
| BasI13 | Number(011,2) | Sim | Base de INSS de 13° Salário |
| ValI13 | Number(011,2) | Sim | Valor de INSS de 13° Salário |
| BasInP | Number(011,2) | Sim | Base de INSS Mensal sem Patronal |
| ValMat | Number(011,2) | Sim | Valor Salário Maternidade Mensal |
| ValM13 | Number(011,2) | Sim | Valor Salário Maternidade 13° Salário |
| ValFam | Number(011,2) | Sim | Valor Salário Família Mensal |
| FgtAnt | String(001) | Sim | FGTS Mês Anterior |
| Fil13s | Number(006,0) | Sim | Filial do Cálculo de 13° Salário |
| BasAvi | Number(011,2) | Sim | Base de INSS Mensal Aviso Prévio Indenizado |
| BasA13 | Number(011,2) | Sim | Base de INSS de 13° Salário Aviso Prévio Indenizado |
| BaFAvi | Number(011,2) | Sim | Base de FGTS Mensal Aviso Prévio Indenizado |
| BaFA13 | Number(011,2) | Sim | Base de FGTS de 13° Salário Aviso Prévio Indenizado |
| Cmp13s | String(001) | Sim | INSS de 13º pagamento competência 13 |
| CmpAu1 | Number(011,2) | Sim | Campo Auxiliar 1 |
| CmpAu2 | Number(011,2) | Sim | Campo Auxiliar 1 |

---

## Chave Primária

- NumEmp
- CmpRef
- CodCal
- TipCol
- NumCad

---

## Índices

### R056SFPIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- CodCal
- TipCol
- NumCad

---

## Relacionamentos

Nenhum relacionamento cadastrado.
