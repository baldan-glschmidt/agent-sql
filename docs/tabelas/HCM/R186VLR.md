# R186VLR

## Descrição

PLR - Resultado Colaborador

---

## Resumo

- Campos: 10
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Número do Colaborador |
| CmpPpr | Date | Não | Competência de Cálculo do PPR |
| TotPon | Number(011,2) | Sim | Total de Pontos Possíveis |
| PonLoc | Number(011,2) | Sim | Pontuação Conquistada pelo Local |
| PonFun | Number(011,2) | Sim | Pontuação Conquistada pelo Colaborador |
| PerLoc | Number(005,2) | Sim | Percentual que Representa no Local |
| VlrDis | Number(013,4) | Sim | Valor da Distribuição |
| ExpCal | String(030) | Sim | Expressão de Cálculo dos Pontos do Local |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpPpr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R186VLR_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

