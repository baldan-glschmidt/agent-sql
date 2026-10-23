# R016ORN

## Descrição

Locais do Organograma

---

## Resumo

- Campos: 13
- Chave Primária: 2 campo(s)
- Índices: 3
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| NomLoc | String(060) | Sim | Descrição do Local |
| CodRat | Number(009,0) | Sim | Código de Rateio do Local |
| DatCri | Date | Sim | Data Criação do Local |
| DatExt | Date | Sim | Data Extinção do Local |
| ConPPP | String(001) | Sim | Considera este local na emissão do PPP |
| TabFeD | Number(004,0) | Sim | Tabela de Feriados Diurna |
| TabFeN | Number(004,0) | Sim | Tabela de Feriados Noturna |
| FerOfD | Number(004,0) | Sim | Tabela Oficial de Feriados Diurna |
| FerOfN | Number(004,0) | Sim | Tabela Oficial de Feriados Noturna |
| USU_NumEmp | Number(004,0) | Sim | Código da Empresa |
| USU_CodCcu | String(018) | Sim | Código Centro Custo Contábil |

---

## Chave Primária

- TabOrg
- NumLoc

---

## Índices

### R016ORNIndice2

**Tipo:** Não unico

Campos:
- TabOrg
- NomLoc

### R016ORNIndice3

**Tipo:** Unico

Campos:
- NumLoc

### R016ORNIndice4

**Tipo:** Não unico

Campos:
- TabOrg
- CodRat

---

## Relacionamentos

### IR_R016ORN_000

**Tabela:** R016ORE

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |

