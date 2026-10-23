# R032INS

## Descrição

Valores utilizados de Base de INSS de Outro Contrato - Terceiros

---

## Resumo

- Campos: 20
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| CmpPte | Date | Não | Competência Pagto Terceiro |
| SeqTab | Number(009,0) | Não | Sequência |
| TipIns | Number(001,0) | Sim | Tipo de Inscrição |
| NumIns | Number(015,0) | Sim | Número Inscrição |
| CfjIns | String(014) | Sim | Número Inscrição |
| CateSo | Number(004,0) | Sim | Código da categoria eSocial |
| ConDes | String(001) | Sim | Primeira Contribuição Descontada |
| BmeIns | Number(011,2) | Sim | Base do INSS Mensal |
| VmeIns | Number(011,2) | Sim | Valor do INSS Mensal |
| B13Ins | Number(011,2) | Sim | Base do INSS 13° Salário |
| V13Ins | Number(011,2) | Sim | Valor do INSS 13° Salário |
| OutEmp | Number(004,0) | Não | Empresa Outro Contrato |
| OutTip | Number(001,0) | Não | Tipo Colaborador Outro Contrato |
| OutCad | Number(009,0) | Não | Cadastro Colaborador Outro Contrato |
| AjuDes | String(020) | Sim | Descrição |
| AjuDat | Date | Sim | Data |
| AjuVal | Number(011,2) | Sim | Valor |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpPte
- SeqTab

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
