# R088LRE

## Descrição

Lançamentos de Reembolso - Eventos

---

## Resumo

- Campos: 12
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa do Colabolador Usuário do Veículo |
| TipCol | Number(001,0) | Não | Tipo do Colabolador Usuário do Veículo |
| NumCad | Number(009,0) | Não | Cadastro do Colabolador Usuário do Veículo |
| MedIni | Date | Não | Medição Inicial do Reembolso |
| DatHod | Date | Não | Data de Medição do Hodômetro |
| CodCid | Number(007,0) | Não | Código da Cidade |
| CodTab | Number(003,0) | Não | Código da Tabela Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| DatAlt | Date | Sim | Data da Alteração do Usuário do Veículo |
| HodEve | Number(007,0) | Sim | Quilometragem Realizada no Evento |
| ValEve | Number(014,2) | Sim | Valor do Evento do Lançamento de Reembolso |
| ObsEve | String(1500) | Sim | Observação do Lançamento da Medição - Evento |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- MedIni
- DatHod
- CodCid
- CodTab
- CodEve

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088LRE_004

**Tabela:** R088LRH

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| MedIni | MedIni |
| DatHod | DatHod |

