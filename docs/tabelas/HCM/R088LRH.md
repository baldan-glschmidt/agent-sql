# R088LRH

## Descrição

Lançamentos de Reembolso - Hodômetros

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
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
| HodIni | Number(007,0) | Sim | Quilometragem Inicial do Hodômetro na Data de Medição |
| HodFim | Number(007,0) | Sim | Quilometragem Final do Hodômetro na Data de Medição |
| ObsLrh | String(1500) | Sim | Observação do Lançamento da Medição |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- MedIni
- DatHod

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088LRH_003

**Tabela:** R088LRB

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| MedIni | MedIni |

