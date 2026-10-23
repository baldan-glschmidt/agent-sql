# R107EVD

## Descrição

PDI - Evidências do plano de desenvolvimento

---

## Resumo

- Campos: 12
- Chave Primária: 9 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| TipCol | Number(001,0) | Não | Tipo de colaborador |
| NumCad | Number(009,0) | Não | Cadastro |
| CodPln | Number(004,0) | Não | Código do Plano de Desenvolvimento |
| CodObj | Number(002,0) | Não | Código do Objetivo |
| CodAco | Number(002,0) | Não | Código da Ação |
| SeqAco | Number(002,0) | Não | Sequência da Ação |
| DatEvd | Date | Não | Data da evidência |
| SeqEvd | Number(002,0) | Não | Sequência da Evidência |
| DesEvd | String(500) | Sim | Descrição da evidência |
| Imagem | Image | Sim | Imagem |
| NomArq | String(250) | Sim | Nome do Arquivo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodPln
- CodObj
- CodAco
- SeqAco
- DatEvd
- SeqEvd

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R107EVD_006

**Tabela:** R107ACO

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodPln | CodPln |
| CodObj | CodObj |
| CodAco | CodAco |
| SeqAco | SeqAco |

