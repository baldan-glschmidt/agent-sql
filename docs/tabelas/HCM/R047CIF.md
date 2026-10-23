# R047CIF

## Descrição

Códigos de Integração Financeira

---

## Resumo

- Campos: 19
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCif | Number(003,0) | Não | Código de Integração Financeira |
| DesCif | String(020) | Sim | Descrição do CIF |
| TipTit | String(003) | Sim | Tipo de Título |
| TipTis | String(003) | Sim | Tipo de Título do ERP |
| DiaVnc | Number(002,0) | Sim | Dia de Vencimento |
| TipVen | String(001) | Sim | Tipo do Vencimento |
| UsoRat | String(001) | Sim | Rateio |
| TipAgr | String(001) | Sim | Tipo de Agrupamento |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| CodReg | Number(003,0) | Sim | Regra a ser executada antes de inserir uma pendência |
| TerFpa | Number(004,0) | Sim | Código do Terceiro do Convênio da GPS |
| DatEnt | String(001) | Sim | Data de Entrada do Título |
| DatEmi | String(001) | Sim | Data Emissão do Título |
| AtuAtr | String(001) | Sim | Atualiza Valor em Atraso |
| AgrMod | String(001) | Sim | Agrupar por Modo Pagamento |
| TipCif | Number(001,0) | Sim | Tipo de CIF INSS |
| CodRec | Number(004,0) | Sim | Código de Recolhimento - DARF |
| BusFor | String(001) | Sim | Fornecedor Individual |
| BasVen | Number(001,0) | Sim | Base para cálculo do vencimento |

---

## Chave Primária

- CodCif

---

## Índices

### R047CIFIndice2

**Tipo:** Não unico

Campos:
- TipTit

---

## Relacionamentos

Nenhum relacionamento cadastrado.
