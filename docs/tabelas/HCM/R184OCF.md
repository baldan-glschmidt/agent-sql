# R184OCF

## Descrição

PLR - Objetivos do Colaborador - Faixas

---

## Resumo

- Campos: 10
- Chave Primária: 6 campo(s)
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
| CodObj | Number(004,0) | Não | Código do Objetivo |
| FaiObj | Number(002,0) | Não | Faixa do Objetivo |
| DesOfa | String(030) | Sim | Descrição da Faixa |
| VinOfa | Number(011,2) | Sim | Início da Faixa |
| VfiOfa | Number(011,2) | Sim | Fim da Faixa |
| QtdPto | Number(011,2) | Sim | Quantidade de Pontos da Faixa |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpPpr
- CodObj
- FaiObj

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R184OCF_004

**Tabela:** R184OCO

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CmpPpr | CmpPpr |
| CodObj | CodObj |

