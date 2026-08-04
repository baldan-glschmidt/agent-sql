# E710ETR

## Descrição

Ficha - Roteiro - Estágios

---

## Resumo

- Campos: 16
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodRot | String(014) | Não | Código do Roteiro de Produção |
| CodEtg | Number(004,0) | Não | Código do Estágio de Produção agregado ao Roteiro |
| SfxEtr | Number(003,0) | Não | Opção do Estágio (1=Padrão, 2-999=Alternativas) |
| TmpFix | Number(010,4) | Sim | Quantidade de Dias (preparação, espera, etc.) gasto no Estágio independente da quantidade a produzir |
| TipPos | Number(001,0) | Não | Posicionamento (1=Inicia após fim do anterior, 2=inicia junto, 3=final) |
| CodSer | String(014) | Sim | Código do Serviço (Quando Estágio é realizado por Terceiros) |
| CodFor | Number(009,0) | Sim | Código Fornecedor do Serviço (Quando Estágio é realizado por Terceiros) |
| FilPro | Number(005,0) | Sim | Filial de Produção do Estágio |
| LotTec | Number(010,3) | Sim | Lote Técnico ideal, de fabricação a nível de Estágio |
| CodCel | String(004) | Sim | Código da Célula de Produção |
| MovOrp | String(001) | Sim | Indica se é controlado através de movimento (apontamento) por Ordens de Produção |
| DatAlt | Date | Sim | Data Geração ou Alteração do Estágio do Roteiro |
| QtdGop | Number(012,5) | Sim | Quantidade máxima para cada guia de produção do Estágio |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodRot
- CodEtg
- SfxEtr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E710ETR_001

**Tabela:** E710ROT

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodRot | CodRot |

### IR_E710ETR_002

**Tabela:** E093ETG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodEtg | CodEtg |

