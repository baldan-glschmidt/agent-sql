# R184OLO

## Descrição

PLR - Objetivos do Local

---

## Resumo

- Campos: 11
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CmpPpr | Date | Não | Competência de Cálculo do PPR |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CodObj | Number(004,0) | Não | Código do Objetivo |
| DatIni | Date | Sim | Data Início da Validade do Objetivo |
| DatFim | Date | Sim | Data Final da Validade do Objetivo |
| PesObj | Number(011,2) | Sim | Peso do Objetivo |
| SinObj | String(001) | Sim | Sinal de Operação (Soma ou Subtração) |
| SomPon | String(001) | Sim | Soma para Pontuação do Local |
| CodFlt | Number(003,0) | Sim | Código Regra |

---

## Chave Primária

- NumEmp
- CmpPpr
- TabOrg
- NumLoc
- CodObj

---

## Índices

### R184OLOIndice2

**Tipo:** Não unico

Campos:
- NumLoc

---

## Relacionamentos

### IR_R184OLO_001

**Tabela:** R182DEF

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CmpPpr | CmpPpr |

### IR_R184OLO_004

**Tabela:** R182OBJ

| Origem | Destino |
|--------|---------|
| CodObj | CodObj |

