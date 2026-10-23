# R161ATE

## Descrição

Bs - Atendimentos

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
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| DatIni | Date | Não | Data Inicial do Atendimento |
| HorIni | Number(005,0) | Não | Hora Inicial do Atendimento |
| DatFim | Date | Sim | Data Final do Atendimento |
| HorFim | Number(005,0) | Sim | Hora Final do Atendimento |
| CodAtn | Number(003,0) | Sim | Código da Atendente |
| DatAge | Date | Sim | Data Agendamento |
| HorAge | Number(005,0) | Sim | Hora Agendamento |
| CodSlc | Number(003,0) | Sim | Código da Solicitação |
| HisSlc | String(3899) | Sim | Histórico Solicitação |
| CodSlo | Number(003,0) | Sim | Código da Solução |
| DatSlo | Date | Sim | Data da Solução |
| HisSlo | String(1899) | Sim | Histórico Solução |
| CodUsu | Number(010,0) | Sim | Código do Usuário que incluiu o lote |

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

### IR_R161ATE_010

**Tabela:** R161SLC

| Origem | Destino |
|--------|---------|
| CodSlc | CodSlc |

