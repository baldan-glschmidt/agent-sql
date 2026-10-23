# R064EXT

## Descrição

Autorização Horas Extras

---

## Resumo

- Campos: 17
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| DatIni | Date | Não | Data Inicial da Hora Extra |
| HorIni | Number(005,0) | Não | Hora Inicial da Hora Extra |
| HorFim | Number(005,0) | Sim | Hora Final da Hora Extra |
| DatFim | Date | Sim | Data Final da Hora Extra |
| EmpAut | Number(004,0) | Sim | Código da Empresa do Autorizador da Hora Extra |
| TClAut | Number(001,0) | Sim | Tipo de Colaborador do Autorizador da Hora Extra |
| CadAut | Number(009,0) | Sim | Cadastro do Autorizador da Hora Extra |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou a Autorização |
| StaAcc | Number(001,0) | Sim | Status da Atualização na Tabela CONTROLE (Acesso On-Line) |
| TolAEA | Number(005,0) | Sim | Tolerância de Acesso na Entrada para Relógios de Acesso |
| TolAsa | Number(005,0) | Sim | Tolerância de Acesso na Saída para Relógios de Acesso |
| TolAEP | Number(005,0) | Sim | Tolerância de Acesso na Entrada para Relógios de Ponto |
| TolASP | Number(005,0) | Sim | Tolerância de Acesso na Saída para Relógios de Ponto |
| ObsExt | String(200) | Sim | Observação de Horas Extras |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R064EXT_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

