# R040BTF

## Descrição

Valores utilizados de Base de INSS de Outro Contrato - Férias

---

## Resumo

- Campos: 21
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| IniPer | Date | Não | Data Início do Período |
| IniFer | Date | Não | Data Início das Férias |
| TipCon | String(001) | Não | Tipo Outro Contrato de Trabalho |
| OrdCal | Number(009,0) | Não | Ordem Cálculo |
| ConInd | Number(001,0) | Sim | Contribuinte Individual |
| BasIns | Number(011,2) | Sim | Base do INSS Mensal |
| VlrIns | Number(011,2) | Sim | Valor do INSS Mensal |
| DevIns | Number(011,2) | Sim | Valor Devolução Inss |
| BasTri | Number(011,2) | Sim | Base Tributada Mensal |
| BasOut | Number(011,2) | Sim | Base Outros Contratos Mensal |
| OriInf | String(001) | Sim | Origem da informação |
| CmpAu1 | Number(011,2) | Sim | Campo Auxiliar 1 |
| CmpAu2 | Number(011,2) | Sim | Campo Auxiliar 2 |
| CmpAu3 | Number(011,2) | Sim | Campo Auxiliar 3 |
| CmpAu4 | Number(002,0) | Sim | Campo Auxiliar 4 |
| CmpAu5 | Date | Sim | Campo Auxiliar 5 |
| CmpAu6 | String(001) | Sim | Campo Auxiliar 6 |
| CmpAu7 | String(300) | Sim | Campo Auxiliar 7 |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- IniPer
- IniFer
- TipCon
- OrdCal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
