# R056RCS

## Descrição

Fgts Rescisão

---

## Resumo

- Campos: 82
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| TipRcs | Number(001,0) | Não | Tipo Rescisão |
| PagRcs | Date | Não | Data Pagto Rescisão |
| SitRec | String(001) | Sim | Situação da Rescisão |
| FadDep | Number(011,2) | Sim | Valor FGTS Depósito Rescisão - Mês Anterior |
| Fad13s | Number(011,2) | Sim | Valor FGTS 13° Salário Rescisão - Mês Anterior |
| FadJam | Number(011,2) | Sim | Valor FGTS JAM Rescisão - Mês Anterior |
| FadMul | Number(011,2) | Sim | Valor FGTS Multa Rescisão - Mês Anterior |
| FadBas | Number(011,2) | Sim | Base FGTS Depósito Rescisão - Mês Anterior |
| FadB13 | Number(011,2) | Sim | Base FGTS 13° Salário Rescisão - Mês Anterior |
| FadVlr | Number(012,2) | Sim | Valor do FGTS Recolhido - Mês Anterior |
| FadVla | Number(012,2) | Sim | Valor do FGTS Adicional Recolhido - Mês Anterior |
| FadJmu | Number(012,2) | Sim | JAM/Multa s/ Vlr FGTS Recolhido - Mês Anterior |
| FrdDep | Number(011,2) | Sim | Valor FGTS Depósito Rescisão - Mês Rescisão |
| Frd13s | Number(011,2) | Sim | Valor FGTS 13° Salário Rescisão - Mês Rescisão |
| FrdJam | Number(011,2) | Sim | Valor FGTS JAM Rescisão - Mês Rescisão |
| FrdMul | Number(011,2) | Sim | Valor FGTS Multa Rescisão - Mês Rescisão |
| FrdBas | Number(011,2) | Sim | Base FGTS Depósito Recolhido - Mês Rescisão |
| FrdB13 | Number(011,2) | Sim | Base FGTS 13° Salário Rescisão - Mês Rescisão |
| FrdVlr | Number(011,2) | Sim | Valor FGTS Recolhido - Mês Rescisão |
| FrdVla | Number(011,2) | Sim | Valor FGTS Adicional Recolhido - Mês Rescisão |
| FrdJmu | Number(011,2) | Sim | JAM/Multa s/ Valor FGTS Recolhido - Mês Rescisão |
| FmdDep | Number(011,2) | Sim | Valor FGTS Depósito Rescisão - Multa |
| Fmd13s | Number(011,2) | Sim | Valor FGTS 13° Salário Rescisão - Multa |
| FmdJam | Number(011,2) | Sim | Valor FGTS JAM Rescisão - Multa |
| FmdMul | Number(011,2) | Sim | Valor FGTS Multa Rescisão - Multa |
| FmdBas | Number(011,2) | Sim | Base FGTS Depósito Rescisão - Multa |
| FmdB13 | Number(011,2) | Sim | Base FGTS 13° Salário Rescisão - Multa |
| FmdVlr | Number(011,2) | Sim | Valor FGTS Recolhido - Multa |
| FmdVla | Number(011,2) | Sim | Valor FGTS Adicional Recolhido - Multa |
| FmdJmu | Number(011,2) | Sim | JAM/Multa s/ Valor FGTS Recolhido - Multa |
| FviDep | Number(011,2) | Sim | Valor FGTS Depósito Rescisão - Verbas Indenizatórias |
| Fvi13s | Number(011,2) | Sim | Valor FGTS 13° Salário Rescisão - Verbas Indenizatórias |
| FviJam | Number(011,2) | Sim | Valor FGTS JAM Rescisão - Verbas Indenizatórias |
| FviMul | Number(011,2) | Sim | Valor FGTS Multa Rescisão - Verbas Indenizatórias |
| FviBas | Number(011,2) | Sim | Base FGTS Depósito Rescisão - Verbas Indenizatórias |
| FviB13 | Number(011,2) | Sim | Base FGTS 13° Salário Rescisão - Verbas Indenizatórias |
| FviVlr | Number(011,2) | Sim | Valor FGTS Recolhido - Verbas Indenizatórias |
| FviVla | Number(011,2) | Sim | Valor FGTS Adicional Recolhido - Verbas Indenizatórias |
| FviJmu | Number(011,2) | Sim | JAM/Multa s/ Vlr FGTS Recolhido - Verbas Indenizatórias |
| FarDep | Number(011,2) | Sim | Valor FGTS Depósito Rescisão - Mês Anterior |
| Far13s | Number(011,2) | Sim | Valor FGTS 13° Salário Rescisão - Mês Anterior |
| FarJam | Number(011,2) | Sim | Valor FGTS JAM Rescisão - Mês Anterior |
| FarMul | Number(011,2) | Sim | Valor FGTS Multa Rescisão - Mês Anterior |
| FarBas | Number(011,2) | Sim | Base FGTS Depósito Rescisão - Mês Anterior |
| FarB13 | Number(011,2) | Sim | Base FGTS 13° Salário Rescisão - Mês Anterior |
| FarVlr | Number(011,2) | Sim | Valor FGTS Recolhido - Mês Anterior |
| FarVla | Number(011,2) | Sim | Valor FGTS Adicional Recolhido - Mês Anterior |
| FarJmu | Number(011,2) | Sim | JAM/Multa s/ Valor Recolhido - Mês Anterior |
| FrrDep | Number(011,2) | Sim | Valor FGTS Depósito Rescisão - Mês Rescisão |
| Frr13s | Number(011,2) | Sim | Valor FGTS 13° Salário Rescisão - Mês Rescisão |
| FrrJam | Number(011,2) | Sim | Valor FGTS JAM Rescisão - Mês Rescisão |
| FrrMul | Number(011,2) | Sim | Valor FGTS Multa Rescisão - Mês Rescisão |
| FrrBas | Number(011,2) | Sim | Base FGTS Depósito Rescisão - Mês Rescisão |
| FrrB13 | Number(011,2) | Sim | Base FGTS 13° Salário Rescisão - Mês Rescisão |
| FrrVlr | Number(011,2) | Sim | Valor FGTS Recolhido - Mês Rescisão |
| FrrVla | Number(011,2) | Sim | Valor FGTS Adicional Recolhido - Mês Rescisão |
| FrrJmu | Number(011,2) | Sim | JAM/Multa s/ Valor FGTS Recolhido - Mês Rescisão |
| FmrDep | Number(011,2) | Sim | Valor FGTS Depósito Rescisão - Multa |
| Fmr13s | Number(011,2) | Sim | Valor FGTS 13° Salário Rescisão - Multa |
| FmrJam | Number(011,2) | Sim | Valor FGTS JAM Rescisão - Multa |
| FmrMul | Number(011,2) | Sim | Valor FGTS Multa Rescisão - Multa |
| FmrBas | Number(011,2) | Sim | Base FGTS Depósito Rescisão - Multa |
| FmrB13 | Number(011,2) | Sim | Base FGTS 13° Salário Rescisão - Multa |
| FmrVlr | Number(011,2) | Sim | Valor FGTS  Recolhido - Multa |
| FmrVla | Number(011,2) | Sim | Valor FGTS Adicional Recolhido - Multa |
| FmrJmu | Number(011,2) | Sim | JAM/Multa s/ Valor FGTS Recolhido - Multa |
| FvrDep | Number(011,2) | Sim | Valor FGTS Depósito Rescisão - Verbas Indenizatórias |
| Fvr13s | Number(011,2) | Sim | Valor FGTS 13° Salário Rescisão - Verbas Indenizatórias |
| FvrJam | Number(011,2) | Sim | Valor FGTS JAM Rescisão |
| FvrMul | Number(011,2) | Sim | Valor FGTS Multa Rescisão - Verbas Indenizatórias |
| FvrBas | Number(011,2) | Sim | Base FGTS Depósito Rescisão - Verbas Indenizatórias |
| FvrB13 | Number(011,2) | Sim | Base FGTS 13° Salário Rescisão - Verbas Indenizatórias |
| FvrVlr | Number(011,2) | Sim | Valor FGTS Recolhido - Verbas Indenizatórias |
| FvrVla | Number(011,2) | Sim | Valor FGTS Adicional Recolhido - Verbas Indenizatórias |
| FvrJmu | Number(011,2) | Sim | JAM/Multa s/ Valor FGTS Recolhido - Verbas Indenizatórias |
| BasIns | Number(011,2) | Sim | Base INSS Rescisão |
| ValIns | Number(011,2) | Sim | Valor INSS Rescisão |
| ValSfa | Number(011,2) | Sim | Valor Salário Família Rescisão |
| ValDed | Number(011,2) | Sim | Valor Deduções |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- TipRcs
- PagRcs

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R056RCS_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

