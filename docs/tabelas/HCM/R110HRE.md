# R110HRE

## Descrição

Ficha Médica - Remanejamento

---

## Resumo

- Campos: 12
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código Empresa |
| CodFic | Number(009,0) | Não | Código da Ficha Médica |
| DatIni | Date | Não | Data início do remanejamento |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Local do Organograma |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Código do Cargo |
| DatTer | Date | Sim | Data término(encerramento) da subnormalidade |
| ObsRmj | String(500) | Sim | Observação sobre o remanejamento |
| DesMot | String(040) | Sim | Motivo do Remanejamento |
| CodAte | Number(006,0) | Sim | Código do Atendente |
| ConPPP | String(001) | Sim | Considera este remanejamento p/perfil profissiográfico previdenciário |

---

## Chave Primária

- NumEmp
- CodFic
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110HRE_001

**Tabela:** R110FIC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFic | CodFic |

### IR_R110HRE_006

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

