# R069EMC

## Descrição

Solicitação de Crachás de Colaboradores

---

## Resumo

- Campos: 16
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Titular |
| DatSol | Date | Não | Data da Solicitação de Emissão de Crachá |
| HorSol | Number(005,0) | Não | Hora da Solicitação de Emissão de Crachá |
| DatIni | Date | Sim | Data de Início do Histórico de Crachá |
| HorIni | Number(005,0) | Sim | Hora de Início do Histórico de Crachá |
| DatFim | Date | Sim | Data Final do Histórico de Crachá |
| HorFim | Number(005,0) | Sim | Hora Final do Histórico de Crachá |
| DatEmi | Date | Sim | Data da Emissão do Crachá |
| HorEmi | Number(005,0) | Sim | Hora da Emissão do Crachá |
| ViaCra | Number(002,0) | Sim | Número da Via do Crachá Emitido |
| NumCra | Number(012,0) | Sim | Número do Crachá Emitido |
| OriSol | Number(001,0) | Sim | Origem da Solicitação |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Realizou a Solicitação |
| USU_MOTSOL | String(001) | Sim | Motivo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatSol
- HorSol

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R069EMC_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

