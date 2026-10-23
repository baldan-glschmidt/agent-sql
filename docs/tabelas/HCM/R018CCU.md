# R018CCU

## Descrição

Centros de Custo

---

## Resumo

- Campos: 23
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCcu | String(018) | Não | Código Centro Custo Contábil |
| NomCcu | String(080) | Sim | Descrição do C.Custo |
| FilCtb | Number(006,0) | Sim | Filial Contábil |
| FilGrp | Number(006,0) | Sim | Filial GPS |
| OutEmp | Number(004,0) | Sim | Código da Outra Empresa |
| OutCcu | String(018) | Sim | Código Outro C. Custo |
| TipCta | String(001) | Sim | Tipos de Contas |
| CodRat | Number(009,0) | Sim | Código de Rateio do C.Custo |
| CcuTxt | String(032) | Sim | Código Texto C.Custo p/ Exportação |
| DatCri | Date | Sim | Data de Criação do Centro de Custo |
| DatExt | Date | Sim | Data de Extinção do Centro de Custo |
| CodFil | Number(006,0) | Sim | Código da Filial a ser utilizada no cálculo do orçamento |
| PosCcu | String(024) | Sim | Posição do Centro de Custo |
| CodAgr | Number(009,0) | Sim | Agrupamento do centro de custo |
| USU_DirCcu | Number(002,0) | Sim | Diretoria Responsavel |
| USU_CodResp | Number(003,0) | Sim | Responsavel C.Custo |
| USU_CodCla | Number(002,0) | Sim | Código da Classificação Centro de Custo |
| USU_IdeSeg | Number(003,0) | Sim | Identificação da Segmentação |
| USU_CodDir | Number(004,0) | Sim | Código da Diretoria |
| USU_CodGer | Number(004,0) | Sim | Código da Gerência |
| USU_CodSet | Number(004,0) | Sim | Código do Setor |
| USU_CodAre | Number(004,0) | Sim | Código da Área |

---

## Chave Primária

- NumEmp
- CodCcu

---

## Índices

### R018CCUIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- NomCcu

---

## Relacionamentos

### IR_R018CCU_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

