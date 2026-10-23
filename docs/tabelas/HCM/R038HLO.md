# R038HLO

## Descrição

Histórico Local

---

## Resumo

- Campos: 11
- Chave Primária: 4 campo(s)
- Índices: 2
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatAlt | Date | Não | Data da Alteração do Local |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Novo Local |
| NumLoc | Number(009,0) | Sim | Novo Local do Organograma |
| ConTov | String(001) | Sim | Considerar p/ Cálculo do Turn-Over na Entrada |
| ConTos | String(001) | Sim | Considerar p/ Cálculo do Turn-Over na Saída |
| StaHis | Number(001,0) | Sim | Status do Histórico |
| LocTra | Number(007,0) | Sim | Município do Local de Trabalho RAIS |
| MotAlt | Number(003,0) | Sim | Motivo da Alteração do Local |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAlt

---

## Índices

### R038HLOIndice2

**Tipo:** Não unico

Campos:
- TabOrg
- NumLoc

### R038HLOIndice3

**Tipo:** Não unico

Campos:
- StaHis
- DatAlt

---

## Relacionamentos

### IR_R038HLO_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R038HLO_004

**Tabela:** R016ORE

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |

### IR_R038HLO_005

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

