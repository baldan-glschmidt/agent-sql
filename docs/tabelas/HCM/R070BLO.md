# R070BLO

## Descrição

Históricos de Bloqueio

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
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Titular |
| DatBlo | Date | Não | Data do Bloqueio do Acesso |
| HorBlo | Number(005,0) | Não | Hora do Bloqueio do Acesso |
| CodMot | Number(002,0) | Sim | Código do Motivo do Bloqueio |
| EmpAut | Number(004,0) | Sim | Código da Empresa do Autorizador da Liberação |
| TClAut | Number(001,0) | Sim | Tipo de Colaborador do Autorizador da Liberação |
| CadAut | Number(009,0) | Sim | Cadastro do Autorizador da Liberação |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Bloqueou o Colaborador |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| DatLib | Date | Sim | Data de Liberação |
| HorLib | Number(005,0) | Sim | Hora de Liberação |
| ObsBlo | String(080) | Sim | Observação Bloqueio/Liberação |
| UsuLib | Number(010,0) | Sim | Código do Usuário que Liberou o Colaborador |
| StaAcc | Number(001,0) | Sim | Status da Atualização na Tabela CONTROLE (Acesso On-Line) |
| Integr | String(001) | Sim | Bloqueio do acesso integrado com o Ronda senior X |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatBlo
- HorBlo

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R070BLO_005

**Tabela:** R070MBL

| Origem | Destino |
|--------|---------|
| CodMot | CodMot |

