# R131CNC

## Descrição

Histórico Testes - Conhecimentos

---

## Resumo

- Campos: 9
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatIni | Date | Não | Data de Início do Teste |
| HorIni | Number(005,0) | Não | Hora de Início do Teste |
| FamCnc | String(004) | Não | Código da Família de Conhecimentos |
| CodCnc | String(005) | Não | Código do Conhecimento |
| NotCnc | Number(005,2) | Sim | Nota do Conhecimento |
| PerCnc | Number(005,2) | Sim | Percentual de Conhecimento |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni
- HorIni
- FamCnc
- CodCnc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R131CNC_004

**Tabela:** R131HTE

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatIni | DatIni |
| HorIni | HorIni |

### IR_R131CNC_006

**Tabela:** R125CNC

| Origem | Destino |
|--------|---------|
| FamCnc | FamCnc |
| CodCnc | CodCnc |

