# R142DIA

## Descrição

Diagnósticos Treinamento

---

## Resumo

- Campos: 15
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodDia | Number(009,0) | Não | Código do Diagnóstico |
| DesDia | String(060) | Sim | Descrição do Diagnóstico |
| NumEmp | Number(004,0) | Sim | Código da Empresa do Responsável |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Código do Local |
| TipCol | Number(001,0) | Sim | Tipo de Colaborador Responsável |
| NumCad | Number(009,0) | Sim | Cadastro do Responsável |
| CodUsu | Number(010,0) | Sim | Código do Usuário que gerou o Diagnóstico |
| DatDia | Date | Sim | Data do Diagnóstico |
| DatLim | Date | Sim | Data do Limite |
| CodPri | Number(001,0) | Sim | Código da Prioridade |
| CodMcu | Number(003,0) | Sim | Motivo do Curso |
| DesPrb | String(250) | Sim | Descrição do Problema |
| DscCau | String(250) | Sim | Descrição da Causa |
| NomArq | String(250) | Sim | Arquivo |

---

## Chave Primária

- CodDia

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R142DIA_004

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R142DIA_011

**Tabela:** R128MCU

| Origem | Destino |
|--------|---------|
| CodMcu | CodMcu |

