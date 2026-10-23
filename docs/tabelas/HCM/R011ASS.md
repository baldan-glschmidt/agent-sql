# R011ASS

## Descrição

Compensação dos Lançamentos do Banco de Horas

---

## Resumo

- Campos: 11
- Chave Primária: 10 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodBHr | Number(005,0) | Não | Banco de Horas |
| DatCre | Date | Não | Data do Crédito da Compensação |
| SitCre | Number(003,0) | Não | Situação do Crédito Da Compensação |
| OriCre | String(001) | Não | Origem Crédito |
| DatDeb | Date | Não | Data do Débito da Compensação |
| SitDeb | Number(003,0) | Não | Situação do Débito da Compensação |
| OriDeb | String(001) | Não | Origem Débito |
| QtdAss | Number(010,0) | Sim | Quantidade de Horas Associadas |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodBHr
- DatCre
- SitCre
- OriCre
- DatDeb
- SitDeb
- OriDeb

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R011ASS_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R011ASS_003

**Tabela:** R011BHR

| Origem | Destino |
|--------|---------|
| CodBHr | CodBHr |

