# R055ANT

## Descrição

Antecipações Cesantías(Colômbia)

---

## Resumo

- Campos: 12
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| SisCes | Number(001,0) | Não | Sistema Cesantía |
| CmpAnt | Date | Não | Competência Antecipação |
| TabEve | Number(003,0) | Sim | Código da Tabela de Eventos |
| EveAnt | Number(004,0) | Sim | Evento Antecipação |
| ValAnt | Number(011,2) | Sim | Valor Antecipado |
| EveJur | Number(004,0) | Sim | Evento Juros |
| ValJur | Number(011,2) | Sim | Juros Pagos |
| NroDoc | String(020) | Sim | Número do documento de aprovação da antecipação |
| ObsAnt | String(2500) | Sim | Informações adicionais à antecipação |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- SisCes
- CmpAnt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
