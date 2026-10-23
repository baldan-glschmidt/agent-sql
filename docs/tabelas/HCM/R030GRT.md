# R030GRT

## Descrição

Filiais da Empresa - Liminar Terceiro

---

## Resumo

- Campos: 14
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| TipGrp | Number(001,0) | Não | Tipo Grps |
| DatGrp | Date | Não | Data Grps |
| TerFpa | Number(004,0) | Não | Código do Terceiro da Liminar GPS |
| CodPro | Number(009,0) | Sim | Número do processo judicial |
| CodSus | Number(014,0) | Sim | Código de Suspensão |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| AbrEve | String(100) | Sim | Abrangência de Evento Mensal |
| Abr13s | String(100) | Sim | Abrangência de Evento 13º Salário |
| CmpAu1 | Number(011,2) | Sim | Campo Auxiliar 1 |
| CmpAu2 | Number(009,0) | Sim | Campo Auxiliar 2 |
| CmpAu3 | Date | Sim | Campo Auxiliar 3 |
| CmpAu4 | String(100) | Sim | Campo Auxiliar 4 |

---

## Chave Primária

- NumEmp
- CodFil
- TipGrp
- DatGrp
- TerFpa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030GRT_003

**Tabela:** R030GRP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| TipGrp | TipGrp |
| DatGrp | DatGrp |

