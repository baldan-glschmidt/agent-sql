# R195FUN

## Descrição

Cenário - Ficha Básica Colaborador

---

## Resumo

- Campos: 14
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| NomFun | String(040) | Sim | Nome do Colaborador |
| DatAdm | Date | Sim | Data de Admissão |
| TipCon | Number(002,0) | Sim | Tipo de Contrato |
| GerCol | String(001) | Sim | Origem da geração do colaborador |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Local do Organograma |
| CodFil | Number(006,0) | Sim | Código da Filial |
| CodCcu | String(018) | Sim | Centro Custo |
| CodEsc | Number(009,0) | Sim | Código da Escala |
| CodVin | Number(002,0) | Sim | Código do Vínculo |

---

## Chave Primária

- NumEmp
- CodCen
- TipCol
- NumCad

---

## Índices

### R195FUNIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- CodCen
- TipCol
- NumCad
- GerCol

---

## Relacionamentos

### IR_R195FUN_001

**Tabela:** R195CEN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCen | CodCen |

