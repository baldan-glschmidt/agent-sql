# R184OLF

## Descrição

PLR - Objetivos do Local - Faixas

---

## Resumo

- Campos: 10
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CmpPpr | Date | Não | Competência de Cálculo do PPR |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CodObj | Number(004,0) | Não | Código do Objetivo |
| FaiObj | Number(002,0) | Não | Faixa do Objetivo |
| DesOfa | String(030) | Sim | Descrição da Faixa |
| VinOfa | Number(011,2) | Sim | Início da Faixa |
| VfiOfa | Number(011,2) | Sim | Fim da Faixa |
| QtdPto | Number(011,2) | Sim | Quantidade de Pontos da Faixa |

---

## Chave Primária

- NumEmp
- CmpPpr
- TabOrg
- NumLoc
- CodObj
- FaiObj

---

## Índices

### R184OLFIndice2

**Tipo:** Não unico

Campos:
- NumLoc

---

## Relacionamentos

### IR_R184OLF_004

**Tabela:** R184OLO

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CmpPpr | CmpPpr |
| TabOrg | TabOrg |
| NumLoc | NumLoc |
| CodObj | CodObj |

